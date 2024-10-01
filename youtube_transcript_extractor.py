import requests
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

def get_transcript(video_id, formatted=False, output_format='text'):
    """
    Fetches the transcript for a given YouTube video ID.
    Parameters:
    - video_id: str, the ID of the YouTube video.
    - formatted: bool, option to format the output.
    - output_format: str, 'text' or 'json', determines the format of the output.

    Returns:
    - Transcript as a string or list of dictionaries.
    """
    try:
        # Fetch the transcript using YouTubeTranscriptApi
        transcript = YouTubeTranscriptApi.get_transcript(video_id)

        if output_format == 'text':
            formatter = TextFormatter()
            return formatter.format_transcript(transcript)

        return transcript

    except Exception as e:
        # If there's an error, return it as a string
        return str(e)

def get_transcript_via_request(video_id):
    url = f'https://www.youtube.com/api/timedtext?&video_id={video_id}&hl=en'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.text
    else:
        return f'Error: {response.status_code}'

# Example usage of the new function
if __name__ == "__main__":
    video_id = 'YQHsXMglC9A'  # Replace with the desired video ID
    print(get_transcript_via_request(video_id))
