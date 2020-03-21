import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'S23ADSafdpojkfldşsşjş21312409udjoş2349'
    UPLOAD_FOLDER = 'static/uploads'
    FILE_EXTENSIONS = set(['txt', 'srt'])