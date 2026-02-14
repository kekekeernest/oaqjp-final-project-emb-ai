from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET', 'POST'])
def emotionDetector():
    # POST Method
    if request.method == 'POST':
        text_to_analyze = request.form.get('textToAnalyze', '').strip()
    else:  # GET method
        text_to_analyze = request.args.get('textToAnalyze', '').strip()

    # Run emotion detection
    result = emotion_detector(text_to_analyze)

    # Handle blank input
    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"  # <-- return 200 instead of 400

    # response
    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} and 'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )
    return response_text


if __name__ == "__main__":
    # Listen on all interfaces for cloud IDE
    # app.run(host='localhost', port=5000, debug=True)
    app.run(host='0.0.0.0', port=5000, debug=True)
