# app.py

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
        return jsonify({'error': 'No video ID provided'}), 400

    # Get the transcript
    transcript = get_transcript(video_id, formatted=True, output_format='text')

    # Log the transcript data
    logging.debug(f"Transcript: {transcript}")

    # Check if transcript retrieval was successful
    if "No transcripts" in transcript or not transcript:
        return jsonify({'error': 'No transcripts available for this video'}), 400

    # Return the transcript in the response
    return jsonify({'success': 'Transcript extracted', 'transcript': transcript})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)