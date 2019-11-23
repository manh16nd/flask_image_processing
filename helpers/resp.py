def send_response(app, data, status):
    response = app.response_class(
        response=data, status=status,      mimetype='application/json')
    return response
