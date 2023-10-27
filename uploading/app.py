from flask import Flask, render_template, request, send_from_directory
import os

app = Flask(__name__)

# Configure the directory to store uploaded files
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the "uploads" directory exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def upload_form():
    return render_template('upload.html', filename=None)

@app.route('/upload', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    if uploaded_file:
        filename = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
        uploaded_file.save(filename)
        return render_template('upload.html', filename=uploaded_file.filename)
    return 'No file uploaded.'

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)
