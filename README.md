# SELDVisualSynth

**SELDVisualSynth** is a Python tool designed to generate synthetic visual mixtures tailored for the audio-visual DCASE Challenge Task 3. This tool creates 360-degree synthetic videos based on DCASE CSV metadata files, which provide per-frame information about sound event locations in 3D space. For each sound event specified in the metadata, SELDVisualSynth randomly selects a corresponding visual representation from a library of video and image assets. These assets are then spatially positioned in the video according to their specified coordinates, simulating the visual side of sounds in a dynamic and immersive way.

---

## Table of Contents

1. [Setup Steps](#setup-steps)  
   1.1 [Download 360-degree Image Canvas](#1---download-360-degree-image-canvas)  
   1.2 [Download Image Assets](#2---download-image-assets)  
   1.3 [Download Video Assets](#3---download-video-assets)  
      - [Download Pre-recorded Videos](#31---download-our-pre-recorded-videos)   
      - [YouTube Video Scraping Script](#32---youtube-video-scraping)  
2. [Usage Instructions](#usage-instructions)  
3. [Citation](#citation)

---

## Setup Steps
> [!IMPORTANT] 
> Please follow the steps below. Note that Step 2 and Step 3 require users to collect their own data and ensure that all collected images and videos are correctly categorized according to the 13 DCASE sound event classes. We recommend reviewing your dataset to confirm that the assets in each category directory aligns with the appropriate category. (Refer to [Sound event classes](https://dcase.community/challenge2023/task-sound-event-localization-and-detection-evaluated-in-real-spatial-sound-scenes))

### 1 - Download 360-degree Image Canvas

Please download the 360-degree image assets to use as canvas/background for the 360 image generation > [Download](https://drive.google.com/drive/u/0/folders/1TJNLzU3QpCZAXWk2mU7-MS7RjcBeP-Lf)

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

**Note:** Some classes, such as "Water tap, faucet," "Bell," and "Knock," may lack sufficient examples in the Flickr30k dataset. We recommend augmenting these categories by sourcing additional images online or from other datasets. Use the same categorization approach as described for Flickr30k.

### 3 - Download Video Assets

#### 3.1 - Download Our Pre-recorded Videos

[Temporary Download URL](<temp-url>)

#### 3.2 - YouTube Video Scraping

This Python script helps you find YouTube videos that match your specified sound event classes.

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

Finally: Include the downloaded YT videos into a unified directory structure as the one from [Download Pre-recorded Videos](#3.1---download-sample-pre-recorded-videos)


## Usage Instructions

1. Generate synthetic spatial audio data using [SpatialScaper](https://github.com/iranroman/SpatialScaper)
2. Define your configuration file for the visual data generator.
    - Define input paths to video and image assets.
        - **Important**: include path to the metadata directory generated by SpatialScaper in Step 1.
    - Define output paths for the generated videos.
    - Define parameters for the visual generator (default is recommended)

Execute SELD visual synthesizer by:

```
python visual_synth.py --config configs/visual_config.yaml
```

## Citation

If you find our work useful, please cite our paper:

```
TBD
```

```
@article{roman2024enhanced,
  title={Enhanced Sound Event Localization and Detection in Real 360-degree audio-visual soundscapes},
  author={Roman, Adrian S and Balamurugan, Baladithya and Pothuganti, Rithik},
  journal={arXiv preprint arXiv:2401.17129},
  year={2024}
}
```

