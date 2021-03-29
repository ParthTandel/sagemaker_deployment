import os
import flask
from simpleModel import SimpleModel

# flask aplication for the rest endpoint
app = flask.Flask(__name__)

"""
Sagmaker relies on two endpoint for its working

1) /ping:
    * this is sagemaker's way of checking the health of the application. If the process has stopped due to some failure,
    process not responding due to other issue etc.
    * this is a get endpoint which returns a simple 200 success status if everthing is working fine

2) /invocation
    * this is the endpoint where the actual inference happens
    * takes what ever custom input you want to sent and then outputs the prediction of the model
"""

@app.route('/ping', methods=['GET'])
def ping():

    # load the model to check if everything is working correctly
    health = SimpleModel.get_model()[0] is not None 
    status = 200 if health else 404
    category = "success" if health else "error"

    # return the status and message based on the health
    response = flask.jsonify(status = status, category = category)
    response.status_code = status
    return response

@app.route('/invocations', methods=['POST'])
def prediction():
    # takes in an input text as json and return a prediction

    # Checking if the request is valid or not
    # In my application I am only accepting json request 
    # hence checking if the content type is application/json
    if flask.request.content_type == 'application/json':
        data = flask.request.json
    else:
        # this will formulate a json reponse and send it back to the endpoint
        error_return = flask.jsonify(status = 400, 
                                     message = "Invalid content type. Only accepts json",
                                     category ="error")
        error_return.status_code = 400
        return error_return

    # In my application I am accepting request in format { "text" : "<input obsevation>"}
    # Hence checking if text field is present in the request or not
    if "text" not in data:
        # this will formulate a json reponse and send it back to the endpoint
        error_return = flask.jsonify(status = 400, 
                                     message = "Invalid Json text field not present",
                                     category ="error")
        error_return.status_code = 400
        return error_return

    # My model predict 2 labels 0 or 4
    # if label is 4 then the sentiment is positive
    # else the sentiment is negative

    prediction = SimpleModel.predict(data["text"])
    if prediction[0] == 4:
        pred = "positive"
        prob = prediction[1][1]
    else:
        pred = "negative"
        prob = prediction[1][0]
    
    # again here formulating the response
    response = flask.jsonify(status = 200, 
                            prediction = pred,
                            score = prob,
                            category ="success")
    # status code of success to 200
    response.status_code = 200

    # the reponse will look like this
    """
    {
        "status": 200,
        "prediction" : <the models prediction>
        "category" : "success"
    }
    """
    return response

# incase you want to test you flass application local when you are building it
# if __name__ == "__main__":
#     app.run()