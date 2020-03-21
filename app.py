from flask import Flask
from config import Config
import os
import time
from chardet import detect
from flask import render_template, flash, redirect, request, send_from_directory, url_for
from werkzeug.utils import secure_filename


app = Flask(__name__)
app.config.from_object(Config)
SECRET_KEY = os.environ.get('SECRET_KEY') or 'S23ADSafdpojkfldşsşjş21312409udjoş2349'
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'srt'])
target_format = 'UTF-8'


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def upload_form():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No file selected for uploading')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            with open(file_path, 'rb') as f:  # Detecting Encoding
                raw_data = f.read()
            source_format = detect(raw_data)['encoding']
            print(source_format)

            with open(file_path, 'rU', encoding=source_format) as sf:  # replacing characters
                content = sf.read()
                replaced_content = content.replace('Ý', 'İ').replace('ý', 'ı').replace('þ', 'ş').replace('ð',
                                                                                                         'ğ').replace(
                    'Þ', 'Ş').replace('Ð', 'Ğ')

                with open(file_path, 'w', encoding=target_format) as tf:  # writing replaced content to the file
                    tf.write(replaced_content)
                    time.sleep(2)

            return redirect(url_for('download_file', filename=filename))

    else:
        flash('Allowed file types are txt,srt')
        return redirect(request.url)


@app.route('/uploads/<path:filename>', methods=['GET', 'POST'])
def download_file(filename):
    downloads = os.path.join(app.config['UPLOAD_FOLDER'])
    return send_from_directory(directory=downloads, filename=filename)


if __name__ == '__main__':
    app.run()
