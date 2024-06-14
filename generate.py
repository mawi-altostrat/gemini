from flask import Flask, request, jsonify
from google.cloud import aiplatform

app = Flask(__name__)

@app.route('/generate_text', methods=['POST'])
def generate_text():
    data = request.get_json()
    prompt = data['prompt']

    aiplatform.init(project="YOUR_PROJECT_ID", location="YOUR_REGION")
    model = aiplatform.Model("YOUR_GEMINI_PRO_MODEL_NAME")

    response = model.predict(
        prompt=prompt,
        max_output_tokens=1024,
        temperature=0.7,
    )

    return jsonify(response)
