# Use the following command  to test use the followingh curl command
#   "curl -X GET -i http://localhost:5000/emotionDetector?textToAnalyze=I%20love%20stuff"
"""Flask server that call package EmotionDetection to 
   analysis emotional sentment of an imput sting.
   Calls: EmotionDetection package
   Loads: emotion_detection python library
   Runs : emotion_detector(<string>) defined function 
   Output : Emotions attributed weighte by a give number

   Emotion analysed are:
   Anger, 
   Disgust, 
   Fear, 
   Joy, 
   Sadness
   
   Dominant emotion also indicated.
"""
from flask import Flask, render_template, request

from EmotionDetection.emotion_detection import emotion_detector

# Instantiate Flask functionality
app = Flask("__name__")

# If server called with /emotionDetector" decorator paramater is mapped to sent_detector()
@app.route("/emotionDetector")

def sent_detector():
    """Detector of emotion in text

    Args:
    string: The text to analyze.

    # Use the following command  to test use the followingh curl command
    #   "curl -X GET -i http://localhost:5000/emotionDetector?textToAnalyze=I%20love%20stuff"

    Returns:
    String: Do notes emotion  statement.
    """

    # When decorator used get extract text argumment and stored in virable text_to_analyze.
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass text_to_analyzer to sentiment_analyzer then store returned directory in response object.
    response = emotion_detector(text_to_analyze)

    if  response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    # Return a formatted string with response and dominant_emotion label.
    result_string = "For the given statement, the system response is "
    result_string += " 'anger': {response['anger']},"
    result_string += " 'disgust': {response['disgust']},"
    result_string += " 'fear': {response['fear']},"
    result_string += " 'joy': {response['joy']},"
    result_string += " 'sadness': {response['sadness']}."
    result_string += " The dominant emotion is {response['dominant_emotion']}."
    result = result_string
    return result

# If call the server is to "/" the render the GUI tenplate index.htm;.
@app.route("/")
def render_index_page():
    """Call render template package function to render index.html file
    Povides GUI front end
    """
    return render_template('index.html')


# If run as python script __name__ = "__main__"  call app.run() funntion
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
