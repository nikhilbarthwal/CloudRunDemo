import os
import shutil
import requests
import tempfile

from flask import Flask, after_this_request, render_template, request, send_file
from subprocess import call

UPLOAD_FOLDER = '/tmp'
ALLOWED_EXTENSIONS = set(['doc', 'docx', 'xls', 'xlsx'])

app = Flask(__name__)


# Convert using Libre Office
def convert_file(output_dir, input_file):
    call('libreoffice --headless --convert-to pdf --outdir %s %s ' %
         (output_dir, input_file), shell=True)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def api():
    work_dir = tempfile.gettempdir()
    file_name = 'document'
    input_file_path = os.path.join(work_dir, file_name)
    # Libreoffice is creating files with the same name but .pdf extension
    output_file_path = os.path.join(work_dir, file_name + '.pdf')

    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return 'No file provided'
        file = request.files['file']
        if file.filename == '':
            return 'No file provided'
        if file and allowed_file(file.filename):
            file.save(input_file_path)

    if request.method == 'GET':
        url = request.args.get('url', type=str)
        if not url:
            return render_template('index.html')
        # Download from URL
        response = requests.get(url, stream=True)
        with open(input_file_path, 'wb') as file:
            shutil.copyfileobj(response.raw, file)
        del response

    convert_file(work_dir, input_file_path)

    @after_this_request
    def cleanup(response):
        if os.path.exists(input_file_path):
            os.remove(input_file_path)
        return response

    return send_file(output_file_path, mimetype='application/pdf')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
