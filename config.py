import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'very-very-secret-key-123789456'
    UPLOAD_FOLDER = 'static/uploads'
    ALLOWED_EXTENSIONS = set(['txt', 'srt'])
