import os
import csv
import shutil
from collections import defaultdict

# Define the sound classes and their associated keywords
sound_classes = {
    0: ["woman speaking"],
    1: ["man speaking"],
    2: ["clapping", "applause", "person clapping"],
    3: ["telephone ringing", "cellphone", "telephone"],
    4: ["laughing"],
    5: ["dishes", "vacuum cleaner", "kitchen dishes", "dish washing", "brooming"],
    6: ["running on", "walking on", "walking", "footsteps"],
    7: ["door opening", "door closing", "door asmr", "door creak"],
    8: ["music band", "orchestra"],
    9: ["musical instrument", "guitarist", "violinist", "piano", "drum", "cello"],
    10: ["faucet", "running water", "bathroom sink", "water tap"],
    11: ["doorbell"],
    12: ["door knock", "knock table"]
}

# Paths
metadata_file = "/Users/adrianromanguzman/Downloads/flickr30k_images/results.csv"  # Path to the Flickr30k metadata file
images_dir = "/Users/adrianromanguzman/Downloads/flickr30k_images/flickr30k_images"  # Path to the Flickr30k images directory
output_dir = "flickr30k_images_per_class"  # Path to the output directory where images will be categorized

# Create output directories for each class
for class_id in sound_classes.keys():
    os.makedirs(os.path.join(output_dir, f"Class_{class_id}"), exist_ok=True)

# Function to find matching class based on keywords
def find_matching_classes(caption, sound_classes):
    matching_classes = []
    for class_id, keywords in sound_classes.items():
        if any(keyword.lower() in caption.lower() for keyword in keywords):
            matching_classes.append(class_id)
    return matching_classes

# Process the metadata file
image_to_classes = defaultdict(list)

with open(metadata_file, "r", encoding="utf-8") as csv_file:
    reader = csv.reader(csv_file, delimiter="|")
    for row in reader:
        if len(row) < 3:
            continue

        image_name = row[0].strip()
        caption = row[2].strip()

        matching_classes = find_matching_classes(caption, sound_classes)
        if matching_classes:
            image_to_classes[image_name].extend(matching_classes)

# Copy matching images to respective class directories
for image_name, class_ids in image_to_classes.items():
    image_path = os.path.join(images_dir, image_name)

    if not os.path.exists(image_path):
        print(f"Warning: Image {image_name} not found in {images_dir}")
        continue

    for class_id in set(class_ids):  # Use set to avoid duplicate copies
        class_dir = os.path.join(output_dir, f"Class_{class_id}")
        shutil.copy(image_path, class_dir)

print("Dataset generation completed.")

