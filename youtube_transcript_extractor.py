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
        # Set a custom user agent
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }

        # Fetch the transcript with custom headers
        transcript = YouTubeTranscriptApi.get_transcript(video_id, headers=headers)

        if output_format == 'text':
            formatter = TextFormatter()
            return formatter.format_transcript(transcript)

        return transcript

    except Exception as e:
        return str(e)
