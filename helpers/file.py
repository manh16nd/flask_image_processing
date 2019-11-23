import os
from werkzeug import secure_filename


def save_file(file):
    filename = secure_filename(file.filename)  # save file
    filepath = os.path.join(os.getcwd(), 'storage', filename)
    file.save(filepath)

    return filepath
