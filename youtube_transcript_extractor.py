from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

def get_transcript(video_id, formatted=False, output_format='text'):
    """
    Fetches the transcript for a given YouTube video ID.
    
    Parameters:
    - video_id: str, the ID of the YouTube video.
    - formatted: bool, option to format the output (default: False).
    - output_format: str, 'text' or 'json', determines the format of the output (default: 'text').

    Returns:
    - Transcript as a string (if formatted) or a list of dictionaries (if output_format is 'json').
    """
    try:
        # Fetch the transcript
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        
        if output_format == 'text':
            formatter = TextFormatter()
            return formatter.format_transcript(transcript)
        
        return transcript  # This returns the raw transcript if 'json' is specified.

    except Exception as e:
        # Return a generic error message
        return f"An error occurred: {str(e)}"

def save_transcript_to_file(transcript, file_name="transcript.txt"):
    """
    Saves the transcript to a text file.
    
    Parameters:
    - transcript: str, the transcript text.
    - file_name: str, the name of the file to save the transcript to (default: 'transcript.txt').
    """
    try:
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(transcript)
    except Exception as e:
        return f"An error occurred while saving the transcript: {str(e)}"
