# SELDVisualSynth

**SELDVisualSynth** is a Python tool designed to generate synthetic visual mixtures tailored for the audio-visual DCASE Challenge Task 3. This tool creates 360-degree synthetic videos based on DCASE CSV metadata files, which provide per-frame information about sound event locations in 3D space. For each sound event specified in the metadata, SELDVisualSynth randomly selects a corresponding visual representation from a library of video and image assets. These assets are then spatially positioned in the video according to their specified coordinates, simulating the visual side of sounds in a dynamic and immersive way.

---

## Table of Contents

1. [Setup Steps](#setup-steps)  
   1.1 [Download 360-degree Image Canvas](#1---download-360-degree-image-canvas)  
   1.2 [Download Image Assets](#2---download-image-assets)  
   1.3 [Download Video Assets](#3---download-video-assets)  
      - [Download Pre-recorded Videos](#step-1-download-sample-pre-recorded-videos)  
      - [YouTube Video Scraping Script](#step-2-youtube-video-scraping-script-scrape_ytpy)  
2. [Usage Instructions](#usage-instructions)  
3. [License](#license)

---

## Setup Steps

### 1 - Download 360-degree Image Canvas

Instructions for downloading or generating the 360-degree image canvas.

### 2 - Download Image Assets

Steps for obtaining the image assets.

### 3 - Download Video Assets

#### (Step 1) Download Sample Pre-recorded Videos

[Temporary Download URL](<temp-url>)

#### (Step 2) YouTube Video Scraping Script: `scrape_yt.py`

This Python script helps you find YouTube videos that match your specified sound event classes.

##### Features

- Searches YouTube for videos matching 13 sound event classes.
- Uses the YouTube Data API to perform searches.
- Provides timestamps for each video (start and end).
- Outputs results in CSV format.
- Filters for shorter videos (under 10 minutes) for cleaner sound examples.


##### Setup Instructions

1. Install required packages:

```
pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib pandas
```

2. You'll need YouTube API credentials. You can either:

 - Use an API key (simpler but rate-limited)
 - Set up OAuth 2.0 authentication (more complex but higher quotas)

3. For API key:

 - Go to the Google Cloud Console
 - Create a new project or select an existing one
 - Enable the YouTube Data API v3
 - Create an API key under "Credentials"

4. For OAuth (if you don't specify an API key):

 - Download the OAuth client configuration file as "`client_secret.json`"
 - Place it in the same directory as the script
 - Follow the authorization prompts when running the script


##### Usage

```
python scrape_yt.py --api_key YOUR_API_KEY --results 5 --output youtube_sound_events.csv
```

Parameters:

`--api_key`: Your YouTube API key (optional if using OAuth)
`--results`: Number of results to fetch per class (default: 5)
`--output`: Output CSV file name (default: `youtube_sound_events.csv`)

The script will create two files:

- A CSV file with just the link, start, end, and class (matching your format)
- A detailed CSV that includes video titles and descriptions

##### Data download

Run the download script pointing to your generated YT csv file

```
python download.py
```

