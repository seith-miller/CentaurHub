from flask import Blueprint, request, jsonify, current_app
from openai import OpenAI
client = OpenAI()

bp = Blueprint('llm_api', __name__)

@bp.route('/send_prompt', methods=['POST'])
def send_prompt():
    prompt = request.form['prompt']
    api_key = current_app.config['OPENAI_API_KEY']

    try:
        response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ]
        )
        
        text_response = response.choices[0].message.content.strip()
    except Exception as e:
        text_response = f"Unhandled exception: {e}"

    return jsonify({'response': text_response})
