"""Watson NLP emotion detection client."""

import requests


def emotion_detector(text_to_analyze):
    """Send text to Watson NLP and return the formatted emotion response."""
    url = (
        "https://sn-watson-emotion.labs.skills.network/"
        "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )
    header = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    payload = {"raw_document": {"text": text_to_analyze}}
    response = requests.post(url, headers=header, json=payload, timeout=30)
    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }
    parsed_response = response.json()
    emotions = parsed_response["emotionPredictions"][0]["emotion"]
    scores = {
        "anger": emotions["anger"],
        "disgust": emotions["disgust"],
        "fear": emotions["fear"],
        "joy": emotions["joy"],
        "sadness": emotions["sadness"],
    }
    return {**scores, "dominant_emotion": max(scores, key=scores.get)}
