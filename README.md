# Sign_Language



## 1. download_videos.py

This code download video files from URLs listed in a metadata DataFrame (which contains video metadata like URLs and data sources). 

The script organizes the download process into three main functions: download_video, download_video_from_link, and download_video_from_metadata

    1.download_video(video_url, save_path) 
   
       This function downloads single video from a specified URL (video_url) and saves it to a specified path (save_path).
       It sends an HTTP GET request to the video URL and writes the content (video) to a file if the request is successful.
   
    2.download_video_from_link(link, output_path)
   
       Download a video from a URL and save it to a file
       This function uses a streaming approach to download the video content, chunking the download in smaller pieces (8 KB by default) to avoid excessive memory usage 
       If an error occurs during the download, it catches the exception and prints the error message.
   
    3.download_video_from_metadata(metadata, data_source, output_path)
       This function takes a DataFrame (metadata), filters the data based on a given data_source, and downloads videos based on the provided video URLs.
       The video files are saved using a name derived from the data source and the video's index.


***************************************************************************************************************************************************************************************************************
## 2 _FinalScraping.ipynb_
The code is a Python script that downloads videos from multiple data sources for a given list of words. Here's a breakdown of how the code works:
1.	### Define Data Sources and Words:
    o	The data sources (INES, V-Librasil, SignBank) are defined, along with a list of words to download videos for.
2.	### Iterate Over Words:
    o	The program iterates over each word in the words_to_download list.
3.	### Download Videos for Each Word:
    o	For each word, it calls download_videos_for_word, which: 
        	-Checks for metadata related to the word from each data source.
          -Extracts the video URLs and downloads the videos using download_video_from_link.
4.	### Saving Videos:
    o	The videos are saved in a directory structure like: base_path/{data_source}/videos/review/{word}.

Example:
•	When the program is executed, it will: 
    o	Look for metadata CSV files in directories corresponding to INES, V-Librasil, and SignBank.
    o	For each word (e.g., "VACINA", "Prevenção"), it will download the videos associated with that word and save them in a folder like Healthbrazil/INES/videos/review/VACINA

## Functions:

_download_video_from_link(video_url, save_path)_

Download a video from a URL and save it to a file


_download_videos_for_word(word, data_sources, base_path)_ 

Download all videos for a specific word across all data sources.


_download_videos_for_words(words_to_download, data_sources, base_path)_

Download all videos for a list of words across all data sources




## Folder Structure:


```task-hub/
├── INES/   
│   ├── metadata.csv      # Metadata for INES
│   ├── videos/           # Original data
│   │   ├── review/       # Review folder
│   │   │   └── folders containing videos/  # Video files
│
├── VLibrasil/   
│   ├── metadata.csv      # Metadata for VLibrasil
│   ├── videos/           # Original data
│   │   ├── review/       # Review folder
│   │   │   └── folders containing videos/  # Video files
│
├── Signbank/   
│   ├── metadata.csv      # Metadata for Signbank
│   ├── videos/           # Original data
│   │   ├── review/       # Review folder
│   │   │   └── folders containing videos/  # Video files (No files yet as this needs a separate set of actions)
```



