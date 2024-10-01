import logging
from flask import Flask, request, jsonify
from youtube_transcript_extractor import get_transcript
from flask_cors import CORS
import youtube_transcript_api

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Set up logging
logging.basicConfig(level=logging.DEBUG)

@app.route('/run-transcript-extractor', methods=['POST'])
def run_transcript_extractor():
    data = request.json
    video_id = data.get('video_id')

    if not video_id:
        app.logger.error("No video ID provided in the request.")
        return jsonify({'error': 'No video ID provided'}), 400

    app.logger.debug(f"Attempting to retrieve transcript for video ID: {video_id}")
    
    try:
        # Log the version of youtube_transcript_api being used
        app.logger.debug(f"Using youtube_transcript_api version: {youtube_transcript_api.__version__}")

        # Get the transcript
        transcript = get_transcript(video_id, formatted=True, output_format='text')

        # Log the transcript data
        app.logger.debug(f"Transcript data: {transcript}")

        # Check if transcript retrieval was successful
        if "No transcripts" in transcript or not transcript:
            app.logger.warning("No transcripts available for this video.")
            return jsonify({'error': 'No transcripts available for this video'}), 400

        # Return the transcript in the response
        return jsonify({'success': 'Transcript extracted', 'transcript': transcript})

    except youtube_transcript_api._errors.TranscriptsDisabled as e:
        app.logger.error(f"Transcripts disabled for this video: {e}")
        return jsonify({'error': 'Transcripts are disabled for this video'}), 400

    except youtube_transcript_api._errors.VideoUnavailable as e:
        app.logger.error(f"Video unavailable: {e}")
        return jsonify({'error': 'The video is unavailable'}), 400

    except youtube_transcript_api._errors.TooManyRequests as e:
        app.logger.error(f"Rate limit exceeded: {e}")
        return jsonify({'error': 'Rate limit exceeded, try again later'}), 429

    except Exception as e:
        app.logger.error(f"Error retrieving transcript: {e}")
        return jsonify({'error': 'Internal server error'}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
