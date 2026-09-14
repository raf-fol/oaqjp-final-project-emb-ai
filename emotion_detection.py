"""emotion_detection python program

Functions:
emotion_detector()
"""

# Import the requests library to handle HTTP requests
import requests, json

def emotion_detector(text_to_analyze):
    """Emotion detector function 


    Args:
    text_to_analyze(strings)
    
    Returns:
    response_text(string)
    """

    # URL to  the emotion detection Watson API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Set the headers required for the API request API POST call
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Create a dictionary with the text to be analyzed which has label "raw_document" pointing to a dictionary labelled  text"
    # the nested direct point to the text to ne analyised by the emotion detector.
    input_json = { "raw_document": { "text": text_to_analyze } }

    # Send a POST request to the API with the text and headers
    response = requests.post(url, json = input_json, headers=header)
    
    # Return the response text only  part of the response  from the API
    response_text = response.text

    # Convert text string attribute of requests response into a json dictionary format  
    response_json = json.loads(response_text)

    # Extract emotion dictionary

    # Return text attribute of response converted to dictionary

    response_emotions = response_json['emotionPredictions'][0]['emotion']

    response_emotions_max_value = max(response_emotions.values())

    response_emotions_max_report = response_emotions

    for emotion in response_emotions:
        if response_emotions[emotion] ==  response_emotions_max_value:
            response_emotions_max_report.update({'dominant_emotion':emotion})
            break
    return response_emotions_max_report