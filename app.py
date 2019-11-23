from flask import Flask, request
from helpers.file import save_file
from helpers.resp import send_response, send_error
from image_processing import parse_img

app = Flask('IMAGE_PROCESSING')


@app.route("/")
def main():
    return "Welcome!"


@app.route('/img', methods=['GET', 'POST'])
def img():
    try:
        if request.method == 'POST':
            file = request.files['img']  # save file
            filepath = save_file(file)
            value = parse_img(filepath)
            return send_response(app, value, 200)
        else:
            return 'Hello World'
    except Exception as e:
        return send_error(app, str(e))


if __name__ == "__main__":
    app.run(debug=True)
