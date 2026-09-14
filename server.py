# Use the following command  to test use the followingh curl command
#   "curl -X GET -i http://localhost:5000/emotionDetector?textToAnalyze=I%20love%20stuff"

"""Output URL request response

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

    # If not text the entered return and report this
    if text_to_analyze == "":
        return "No text submitted! Try again."

    # Pass text_to_analyzer to sentiment_analyzer then store returned directory in response object.
    response = emotion_detector(text_to_analyze)

    # Return a formatted string with response and dominant_emotion label.
    result = f"For the given statement, the system response is 'anger': {response['anger']}, 'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': {response['joy']}, 'sadness': {response['sadness']}. The dominant emotion is {response['dominant_emotion']}."
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