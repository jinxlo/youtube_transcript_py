# youtube_transcript_extractor.py

import logging
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
from youtube_transcript_api.exceptions import VideoNotAvailable, NoTranscriptFound

# Set up logging
logging.basicConfig(level=logging.DEBUG)

def get_transcript(video_id, formatted=False, output_format='text'):
    """
    Fetches the transcript for a given YouTube video ID.
    Parameters:
    - video_id: str, the ID of the YouTube video.
    - formatted: bool, option to format the output.
    - output_format: str, 'text' or 'json', determines the format of the output.

    Returns:
    - Transcript as a string or list of dictionaries, or an error message.
    """
    try:
        # Fetch the transcript
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        
        if output_format == 'text':
            formatter = TextFormatter()
            return formatter.format_transcript(transcript)
        
        return transcript

    except VideoNotAvailable:
        logging.error(f"Video {video_id} is not available.")
        return {'error': 'Video not available'}
    except NoTranscriptFound:
        logging.warning(f"No transcript found for video {video_id}.")
        return {'error': 'No transcript found for this video'}
    except Exception as e:
        logging.error(f"Error retrieving transcript: {e}")
        return {'error': 'Internal server error', 'message': str(e)}

def save_transcript_to_file(transcript, file_name="transcript.txt"):
    """
    Saves the transcript to a text file.
    Parameters:
    - transcript: str, the transcript text.
    - file_name: str, the name of the file to save the transcript to.
    """
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(transcript)
