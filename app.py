import logging
from flask import Flask, request, jsonify
from youtube_transcript_extractor import get_transcript

app = Flask(__name__)

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

    except Exception as e:
        app.logger.error(f"Error retrieving transcript: {e}")
        return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
