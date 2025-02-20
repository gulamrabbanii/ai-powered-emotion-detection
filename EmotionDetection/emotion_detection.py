import requests
import json

def emotion_detector(text_to_analyse):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(URL, json=input_json, headers=headers)
    formatted_json = json.loads(response.text)

    if response.status_code == 200:
        return data_formatting(formatted_json)
    elif response.status_code == 400:
        formatted_json = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
        return formatted_json

def data_formatting(formatted_json):
    if "emotionPredictions" in formatted_json:
        emotion_predictions = formatted_json["emotionPredictions"]
        if len(emotion_predictions) > 0 and "emotion" in emotion_predictions[0]:
            emotions = emotion_predictions[0]["emotion"]
            dominant_emotion_value = -float('inf')
            dominant_emotion = None
            for emotion, value in emotions.items():
                if value >= dominant_emotion_value:
                    dominant_emotion_value = value
                    dominant_emotion = emotion
            emotions['dominant_emotion'] = dominant_emotion
            return emotions
