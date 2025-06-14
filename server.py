"""
Web application for emotion detection in text. Uses Watson AI API.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def em_detector():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detector()
        function.
    '''
    # Take input text
    text_to_analyze = request.args.get('textToAnalyze')

    # Send text for detection
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    # Format output
    output = f"For the given statement, the system response is \
    'anger': {response['anger']}, 'disgust': {response['disgust']}, 'fear': {response['fear']}, \
    'joy': {response['joy']} and 'sadness': {response['sadness']}. \
    The dominant emotion is {response['dominant_emotion']}."

    return output

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template("index.html")

if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000, debug=True)
