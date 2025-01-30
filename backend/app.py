from flask import Flask, request, jsonify
import os
from dotenv import load_dotenv
from openai import AzureOpenAI
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow frontend to communicate with backend

# Load environment variables
load_dotenv()
azure_oai_endpoint = os.getenv("AZURE_OAI_ENDPOINT")
azure_oai_key = os.getenv("AZURE_OAI_KEY")
azure_oai_deployment = os.getenv("AZURE_OAI_DEPLOYMENT")

# Initialize Azure OpenAI client
client = AzureOpenAI(
    azure_endpoint=azure_oai_endpoint,
    api_key=azure_oai_key,
    api_version="2024-02-15-preview"
)

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.json
        user_input = data.get("prompt")

        if not user_input:
            return jsonify({"error": "Empty input"}), 400

        messages_array = [
            {"role": "system", "content": "I am a hiking enthusiast named Forest."},
            {"role": "user", "content": user_input}
        ]

        response = client.chat.completions.create(
            model=azure_oai_deployment,
            temperature=0.7,
            max_tokens=1200,
            messages=messages_array
        )

        generated_text = response.choices[0].message.content

        return jsonify({"response": generated_text})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
