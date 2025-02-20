from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['GET'])
def emotion_detector_route():
    text_to_detect = request.args.get('textToAnalyse')
    if not text_to_detect:
        return 'No text provided, please try again!'
    
    resp = emotion_detector(text_to_detect)
    if resp['dominant_emotion'] is None:
        return 'Invalid text, please try again!'
    
    return (
        f"For the given statement, the system response is 'anger': {resp['anger']}, 'disgust': {resp['disgust']}, 'fear': {resp['fear']}, 'joy': {resp['joy']} and 'sadness': {resp['sadness']}. The dominant emotion is {resp['dominant_emotion']}."
    )

@app.route('/')
def render_index_html():
    return render_template('./templates/index.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
