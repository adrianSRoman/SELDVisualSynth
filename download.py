import csv
from pytube import YouTube
from moviepy.video.io.VideoFileClip import VideoFileClip, AudioFileClip
import os
from pydub import AudioSegment
import yt_dlp

# Directory names for each class
class_directories = {
    '0': 'Class_0',
    '1': 'Class_1',
    '2': 'Class_2',
    '3': 'Class_3',
    '4': 'Class_4',
    '5': 'Class_5',
    '6': 'Class_6',
    '7': 'Class_7',
    '8': 'Class_8',
    '9': 'Class_9',
    '10': 'Class_10',
    '11': 'Class_11',
    '12': 'Class_12'
}

def ensure_directory_structure():
    if not os.path.exists(dataset_base_dir):
        os.mkdir(dataset_base_dir)

    for dir_name in class_directories.values():
        class_dir_path = os.path.join(dataset_base_dir, dir_name)
        if not os.path.exists(class_dir_path):
            os.mkdir(class_dir_path)


def download_and_trim(url, start_time, end_time, class_label, sequence_number):
    temp_filename = "temp_video.mp4"
    try:
        # Normalize URL for shorts
        if "youtube.com/shorts/" in url:
            video_id = url.split("/")[-1]
            url = f"https://www.youtube.com/watch?v={video_id}"

        # Download video using yt_dlp
        ydl_opts = {
            'outtmpl': temp_filename.replace(".mp4", ".%(ext)s"),  # Ensure correct extension
            'format': 'bestvideo+bestaudio/best',
            'merge_output_format': 'mp4',  # Ensure the final format is mp4
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        # Trim and save video
        output_directory = os.path.join(dataset_base_dir, class_directories[class_label])
        os.makedirs(output_directory, exist_ok=True)
        output_filename = os.path.join(output_directory, f"clip{sequence_number}.mp4")

        with VideoFileClip(temp_filename) as video:
            trimmed_video = video.subclip(start_time, end_time)
            trimmed_video.write_videofile(output_filename, codec="libx264", audio_codec="aac")

    except Exception as e:
        print(f"Error processing {url}: {e}")
    finally:
        # Clean up temporary files
        if os.path.exists(temp_filename):
            os.remove(temp_filename)

def convert_time(time_str):
    h, m, s = 0, 0, 0
    parts = time_str.split(':')
    if len(parts) == 3:
        h, m, s = map(int, parts)
    elif len(parts) == 2:
        m, s = map(int, parts)
    elif len(parts) == 1:
        s = int(parts[0])
    return h * 3600 + m * 60 + s

def process_csv(csv_file):
    ensure_directory_structure()

    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        video_counter = {}
        for row in reader:
            class_label = row['class']
            video_counter[class_label] = video_counter.get(class_label, 0) + 1

            start_seconds = convert_time(row['start'])
            end_seconds = convert_time(row['end'])
            download_and_trim(row['link'], start_seconds, end_seconds, class_label, video_counter[class_label])


# Set the base directory for the dataset
dataset_base_dir = "./downloaded_video_assets"
# Set YouTube CSV file to use for data download
csv_path = "./youtube_sound_events.csv"
process_csv(csv_path)

