from flask import Flask, request, render_template, jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)

# Home page serving index.html
@app.route('/')
def home():
    return render_template('index.html')

# POST endpoint for emotion detection
@app.route('/emotionDetector', methods=['POST'])
def emotionDetector():
    # Get text from the POST request (sent by JavaScript)
    text_to_analyze = request.form.get('text', '').strip()
    
    if not text_to_analyze:
        return "Error: No input text provided.", 400

    # Run emotion detection
    result = emotion_detector(text_to_analyze)

    # Format the response as requested
    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} and 'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return response_text

if __name__ == "__main__":
    # app.run(host='localhost', port=5000, debug=True)
    app.run(host='0.0.0.0', port=5000, debug=True)

