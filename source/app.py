from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'

    file = request.files['file']

    if file.filename == '':
        return 'No selected file'

    if file:
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)
        return redirect(url_for('display_uploaded_file', filename=file.filename))
        #return filename  # Return the uploaded file's path



#@app.route('/uploads/<filename>')
# @app.route('/uploads')
@app.route('/uploads/<filename>')
def display_uploaded_file(filename):
    print("Filename in display_uploaded_file:", filename)
    return render_template('result.html', filename=filename)

@app.route('/static/<path:filename>')
def serve_static(filename):
    root_dir = os.path.abspath(os.path.dirname(__file__))
    return send_from_directory(os.path.join(root_dir, 'static'), filename)

if __name__ == '__main__':
    app.run(debug=True)
