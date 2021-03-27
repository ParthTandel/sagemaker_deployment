import os
import flask
from simpleModel import SimpleModel

# flask aplication for the rest endpoint
app = flask.Flask(__name__)

"""
Sagmaker relies on two endpoint for its working

1) /ping:
    * this is sagemakers way of chekcing the health of the application, it the process has stopped due to some failer,
    process not responding due to other issue
    * this is a get endpoint which returns a simple 200 success status if everthing is working fine

2) /invocation
    * this is the endpoint where the actual inference happens
    * takes what ever custom input you want to sent and then outputs the prediction of the model
"""

@app.route('/ping', methods=['GET'])
def ping():

    # additional heath check can go here
    health = SimpleModel.get_model() is not None 
    status = 200 if health else 404
    category = "success" if health else "error"
    response = flask.jsonify(status = status, category = category)
    return response

@app.route('/invocations', methods=['POST'])
def prediction():
    # takes in an input text as json and return a prediction

    if flask.request.content_type == 'application/json':
        data = flask.request.json
    else:
        error_return = flask.jsonify(status = 400, 
                                     message = "Invalid content type. Only accepts json",
                                     category ="error")

        return error_return

    if "text" not in data:
        error_return = flask.jsonify(status = 400, 
                                     message = "Invalid Json text field not present",
                                     category ="error")
        error_return.status_code = 400
        return error_return

    if SimpleModel.predict(data["text"]) == 4:
        pred = "positive"
    else:
        pred = "negative"

    response = flask.jsonify(status = 200, 
                            prediction = pred,
                            category ="success")

    response.status_code = 200

    return response

# incase you want to test you flass application local when you are building it
# if __name__ == "__main__":
#     app.run()