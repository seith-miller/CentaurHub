import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key'
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY') or 'your_openai_api_key'
