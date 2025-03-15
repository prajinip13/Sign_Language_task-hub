import requests
import os
import pandas as pd
def download_video(video_url, save_path):
    # Send a GET request to the video URL
    response = requests.get(video_url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Extract video filename from URL
        video_name = video_url.split('/')[-1]  # This assumes that the video file name is at the end of the URL
        video_path = os.path.join(save_path, video_name)
        
        # Save the video content to the file
        with open(video_path, 'wb') as video_file:
            video_file.write(response.content)
        print(f"Downloaded video: {video_path}")
    else:
        print(f"Failed to download video from {video_url}. HTTP Status Code: {response.status_code}")


def download_video_from_link(link: str, output_path: str) -> None:
    """
    Download a video from a URL and save it to a file.
    Args:
        link (str): The URL of the video to download.
        output_path (str): The location where the video will be saved.
    """
    try:
        # Make a GET request to fetch the video content
        response = requests.get(link, stream=True)
        response.raise_for_status()  # Raise an error for bad responses

        # Open the output file in write-binary mode
        with open(output_path, 'wb') as video_file:
            for chunk in response.iter_content(chunk_size=8192):
                video_file.write(chunk)
        
        print(f"Video successfully downloaded to {output_path}")
    
    except requests.exceptions.RequestException as e:
        print(f"Error downloading video from {link}: {e}")
        

def download_video_from_metadata(metadata: pd.DataFrame, data_source: str, output_path: str) -> None:

    """
    Download all videos for one word from one data source.
    Args:
        metadata (pd.DataFrame): DataFrame containing metadata for videos (e.g., URLs).
        data_source (str): The name or identifier of the data source.
        output_path (str): The base location where videos will be saved.
    """
    # Filter metadata for the given data source
    filtered_metadata = metadata[metadata['data_source'] == data_source]
    
    if filtered_metadata.empty:
        print(f"No data found for source: {data_source}")
        return

    # Loop through each row in the filtered metadata
    for index, row in filtered_metadata.iterrows():
        video_link = row['video_url']
        video_name = f"{data_source}_{index + 1}.mp4"  # Naming video based on source and index
        video_path = os.path.join(output_path, video_name)
        
        print(f"Downloading video {index + 1} from {video_link}...")
        download_video_from_link(video_link, video_path)

# Example usage
if __name__ == "__main__":
    # Example metadata DataFrame
    data = {
        'data_source': ['source1'],
        'video_url': ['https://www.bing.com/videos/riverview/relatedvideo?&q=short+videos+of+beaches&&mid=334DD1F6162362D04F36334DD1F6162362D04F36&&FORM=VRDGAR'
                    ]
    }
    metadata_df = pd.DataFrame(data)

    # Specify the data source and output path
    download_video_from_metadata(metadata_df, 'source1', './videos/')
