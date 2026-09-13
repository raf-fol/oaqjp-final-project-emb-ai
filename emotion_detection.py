# Import the requests library to handle HTTP requests
import requests, json

def emotion_detector(text_to_analyse):

    # URL to  the emotion detection Watson API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Set the headers required for the API request API POST call
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Create a dictionary with the text to be analyzed which has label "raw_document" pointing to a dictionary labelled  text"
    # the nested direct point to the text to ne analyised by the emotion detector.
    input_json = { "raw_document": { "text": text_to_analyse } }

    # Send a POST request to the API with the text and headers
    response = requests.post(url, json = input_json, headers=header)
    
    # Return the response text only  part of the response  from the API
    response_text = response.text

    # Return the new diction call emotion_response from the function
    return response_text