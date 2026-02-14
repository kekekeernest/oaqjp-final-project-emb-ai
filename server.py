"""
server.py

Flask web application for NLP Emotion Detection.
Provides endpoints for analyzing text input and returning
detected emotions with their scores and dominant emotion.
"""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route('/')
def home():
    """
    Render the homepage of the NLP Emotion Detection app.

    Returns:
        str: HTML content of index.html
    """
    return render_template('index.html')


@app.route('/emotionDetector', methods=['GET', 'POST'])
def emotion_detector_endpoint():
    """
    Process user input and run emotion detection on the provided text.

    Handles both GET and POST requests. Returns the formatted emotion
    response. If input text is blank, returns a friendly error message.

    Returns:
        str: Formatted system response or error message
    """
    # Get text input from POST or GET
    if request.method == 'POST':
        text_to_analyze = request.form.get('textToAnalyze', '').strip()
    else:
        text_to_analyze = request.args.get('textToAnalyze', '').strip()

    # Run emotion detection
    result = emotion_detector(text_to_analyze)

    # Handle blank input
    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    # Prepare formatted response
    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} and 'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )
    return response_text


if __name__ == "__main__":
    # Entry point for the Flask application.
    # Listens on all interfaces to allow access from Cloud IDE preview.
    app.run(host='0.0.0.0', port=5000, debug=True)
