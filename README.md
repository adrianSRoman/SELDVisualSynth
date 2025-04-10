# SELDVisualSynth

[![arXiv](https://img.shields.io/badge/Arxiv-2401.03497-blueviolet?logo=arxiv)](https://arxiv.org/abs/2504.02988)
[![Platform](https://img.shields.io/badge/Platform-linux-lightgrey?logo=linux)](https://www.linux.org/)
[![Python](https://img.shields.io/badge/Python-3.8%2B-orange?logo=python)](https://www.python.org/)
[![CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)


<p align="center">
  <img src="figures/SELDVisualSynth_Figure.png" alt="SELDVisualSynth Visualization" width="800"/>
</p>

**SELDVisualSynth** is a Python tool designed to generate synthetic visual mixtures tailored for the audio-visual DCASE Challenge Task 3. This tool creates 360-degree synthetic videos based on DCASE CSV metadata files, which provide per-frame information about sound event locations in 3D space. For each sound event specified in the metadata, SELDVisualSynth randomly selects a corresponding visual representation from a library of video and image assets. These assets are then spatially positioned in the video according to their specified coordinates, simulating the visual side of sounds in a dynamic and immersive way.

---

## Table of Contents

0. [Installation](#installation)
1. [Setup Steps](#setup-steps)  
   1.1 [Download 360-degree Image Canvas](#1---download-360-degree-image-canvas)  
   1.2 [Download Image Assets](#2---download-image-assets)  
   1.3 [Download Video Assets](#3---download-video-assets)  
      - [Download Pre-recorded Videos](#31---download-our-pre-recorded-videos)   
      - [YouTube Video Scraping Script](#32---youtube-video-scraping)  
2. [Usage Instructions](#usage-instructions) 
3. [Recommended Datasets Structure](#recommended-datasets-structure)
4. [Citation](#citation)

---

## Installation

Create a Virtual Environment (Python 3.8+ is recommended)
```
python3 -m venv pyenv
```

Install requirements
```
pip install -r requirements.txt
```

## Setup Steps
> [!IMPORTANT] 
> Please follow the steps below. Note that Step 2 and Step 3 require users to collect their own data and ensure that all collected images and videos are correctly categorized according to the 13 DCASE sound event classes. We recommend reviewing your dataset to confirm that the assets in each directory align with the corresponding category. (Refer to [Sound event classes](https://dcase.community/challenge2023/task-sound-event-localization-and-detection-evaluated-in-real-spatial-sound-scenes))

### 1 - Download 360-degree Image Canvas

Please download the 360-degree image assets to use as canvas/background for the video generation

[Download](https://drive.google.com/drive/u/0/folders/1TJNLzU3QpCZAXWk2mU7-MS7RjcBeP-Lf)

### 2 - Download Image Assets

Download the [Flickr30k dataset](https://www.kaggle.com/datasets/hsankesara/flickr-image-dataset).

To categorize the data into the 13 DCASE classes, execute:

```bash
python categorize_flickr30k.py
```

<details>
  <summary>Click to expand</summary>

  Modify the paths within the script to point to your downloaded dataset:

  ```
  # Paths
  metadata_file = "path/to/flickr30k_images/results.csv"  # Path to the Flickr30k metadata file
  images_dir = "path/to/flickr30k_images/flickr30k_images"  # Path to the Flickr30k images directory
  output_dir = "path/to/destination/flickr30k_images_per_class"  # Path to the output directory where images will be categorized
  ```
</details>

> [!NOTE] 
> Some classes, such as "Water tap, faucet," "Bell," and "Knock," may lack sufficient examples in the Flickr30k dataset. We recommend augmenting these categories by sourcing additional images online or from other datasets. Use the same categorization approach as described for Flickr30k.

### 3 - Download Video Assets

#### 3.1 - Download Our Pre-recorded Videos

We provide some samples videos to illustrate the type of videos we use as video assets. These could be used for training, however, we recommend having more samples to achieve diverse visual synthesis. Refer to section 2 and 3.2.

[Download pre-recorded videos](https://drive.google.com/drive/folders/1Wwnzf2gv_E196yjDWIf47awtNLS-sFWr?usp=sharing)

#### 3.2 - YouTube Video Scraping

The script `scrape_yt.py` helps you find YouTube videos that match your specified sound event classes.

##### Features

<details>
  <summary>Click to expand</summary>
  
  - Searches YouTube for videos matching 13 sound event classes.
  - Uses the YouTube Data API to perform searches.
  - Provides timestamps for each video (start and end).
  - Outputs results in CSV format.
  - Filters for shorter videos (under 10 minutes) for cleaner sound examples.

</details>

##### Setup Instructions

<details>
  <summary>Click to expand</summary>
  
  1. Install required packages:

     ```bash
     pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib pandas
     ```

  2. You'll need YouTube API credentials. You can either:

     - Use an API key (simpler but rate-limited)
     - Set up OAuth 2.0 authentication (more complex but higher quotas)

  3. For API key:

     - Go to the [Google Cloud Console](https://console.cloud.google.com/)
     - Create a new project or select an existing one
     - Enable the YouTube Data API v3
     - Create an API key under "Credentials"

  4. For OAuth (if you don't specify an API key):

     - Download the OAuth client configuration file as `client_secret.json`
     - Place it in the same directory as the script
     - Follow the authorization prompts when running the script

</details>


##### Usage

```
python scrape_yt.py --api_key YOUR_API_KEY --results 5 --output youtube_sound_events.csv
```

<details>
    <summary>Click to expand</summary>

    Parameters:

    `--api_key`: Your YouTube API key (optional if using OAuth)
    `--results`: Number of results to fetch per class (default: 5)
    `--output`: Output CSV file name (default: `youtube_sound_events.csv`)

    The script will create two files:

    - A CSV file with just the link, start, end, and class (matching your format)
    - A detailed CSV that includes video titles and descriptions

</details>

##### Data download

Run the download script pointing to your generated YT csv file

```
python download.py
```

**Finally:** If you desire, combine both the pre-recorded videos and your downloaded videos into a unified directory structure as the one from [Download Pre-recorded Videos](#3.1---download-sample-pre-recorded-videos).

> [!NOTE]
> Some classes, such as "Footsteps," "Bell," "Knock," and "Music" may require manual inspection after downloding. Ideally you want the object playing the main role in a video, rather than a secondary role. Note you can adjust the start and end time in the csv file to trim the videos idurations as desired. Also, here you can get as creative as you want. For instance, you can record your own video scenes and adopt them as part of your visual data generation. 

## Usage Instructions

1. Generate synthetic spatial audio data using [SpatialScaper](https://github.com/iranroman/SpatialScaper)
2. Define your [configuration YAML file](configs/visual_config.yaml) for the visual data generator.
    - Define input paths to video and image assets.
        - **Important**: include path to the metadata directory generated by SpatialScaper in Step 1.
    - Define output paths for the generated videos.
    - Define parameters for the visual generator (default is recommended)
    - Note: to start, we recommend only modifying the fields under `input` and `output`. The fields under `processing` may require understanding how these parameters change the visual synthesis. For the most part, the comments should explain what they do.

Execute SELD visual synthesizer by:

```
python visual_synth.py --config configs/visual_config.yaml
```

## Recommended Datasets Structure

360-degree image backgrounds
```
image_360_path/
    ├── image1.jpg
    ├── image2.jpg
    ├── ...
```

360-degree video backgrounds (optional, but recommended)
```
video_360_path/
    ├── video1.mp4
    ├── video2.mp4
    ├── ...
```

Directory containing video assets by event class (video "tiles")
```
video_assets_dir/
    ├── Class_0/
    │   ├── video1.mp4
    │   ├── video2.mp4
    │   ├── ...
    ├── Class_1/
    │   ├── video1.mp4
    │   ├── video2.mp4
    │   ├── ...
    ├── ...
    ├── Class_12/
    │   ├── video1.mp4
    │   ├── video2.mp4
    │   ├── ...
```

Directory containing image assets by event class (image "tiles"). Both jpeg or png are supported.
```
image_assets_dir/
    ├── Class_0/
    │   ├── image1.jpeg
    │   ├── image2.png
    │   ├── ...
    ├── Class_1/
    │   ├── image1.jpeg
    │   ├── image2.png
    │   ├── ...
    ├── ...
    ├── Class_12/
    │   ├── image1.jpeg
    │   ├── image2.png
    │   ├── ...

```

Metadata directory containing metadata CSV files (DCASE-style metadata)
```
metadata_dir/
    ├── dev-train-synth/   # From SpatialScaper
    │   ├── file1.csv
    │   ├── ...
```

## Citation

If you find our work useful, please cite our paper:

```
@article{roman2025generating,
  title={Generating Diverse Audio-Visual 360º Soundscapes for Sound Event Localization and Detection},
  author={Roman, Adrian S and Chang, Aiden and Meza, Gerardo and Roman, Iran R},
  journal={arXiv},
  year={2025}
}
```

```
@inproceedings{roman2024spatial,
  title={Spatial Scaper: a library to simulate and augment soundscapes for sound event localization and detection in realistic rooms},
  author={Roman, Iran R and Ick, Christopher and Ding, Sivan and Roman, Adrian S and McFee, Brian and Bello, Juan P},
  booktitle={IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)},
  year={2024},
  organization={IEEE}
}
```

