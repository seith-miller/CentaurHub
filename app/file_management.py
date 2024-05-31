from flask import Blueprint, request, redirect, url_for, send_from_directory
import os

bp = Blueprint('file_management', __name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@bp.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file:
        filename = file.filename
        file.save(os.path.join(UPLOAD_FOLDER, filename))
        return redirect(url_for('routes.dashboard'))

@bp.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)
