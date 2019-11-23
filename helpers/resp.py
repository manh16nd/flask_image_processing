from helpers.json_dumps import json_dumps


def send_response(app, data, status):
    resp_data = {
        "success": True,
        "data": data,
    }
    response = app.response_class(response=json_dumps(
        resp_data), status=status, mimetype='application/json')
    return response


def send_error(app, err):
    resp_data = {
        "success": False,
        "message": err
    }
    response = app.response_class(response=json_dumps(
        resp_data), status=200, mimetype='application/json')
    return response
