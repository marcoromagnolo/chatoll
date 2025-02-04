from flask import Flask, request, jsonify, render_template, Response
from flask_cors import CORS
import requests
import pidman
import logg
from settings import WEB_SETTINGS
import os

pidman.add_pid_file("webpush.pid")

logger = logg.create_logger('app')


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": WEB_SETTINGS["cors_origins"]}})

# URL di Ollama in locale
OLLAMA_URL = "http://localhost:11434/api/generate"

# Serve index.html alla root
@app.route("/")
def home():
    return render_template("index.html", name="Chatoll", settings=WEB_SETTINGS)

# API per la chat con risposte in streaming
@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.json
        prompt = data.get("prompt", "")
        model = data.get("model", "mymodel")  # Modello di default

        if not prompt:
            return jsonify({"error": "Prompt is required"}), 400

        # Send request to Ollama (No Streaming)
        response = requests.post(OLLAMA_URL, json={
            "model": model,
            "prompt": prompt,
            "stream": False  # Disable Streaming
        })

        # Process response
        if response.status_code == 200:
            json_response = response.json()
            logger.info("Response from OLLAMA: {}".format(json_response))
            return jsonify({"response": json_response.get("response", "No response from AI")})
        else:
            return jsonify({"error": "Failed to connect to Ollama"}), 500

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    print(f"Server is running. Access it at {WEB_SETTINGS['host']}:{WEB_SETTINGS['port']}")
    app.run(host=WEB_SETTINGS['host'],
            port=WEB_SETTINGS['port'],
            debug=WEB_SETTINGS['debug'],
            use_reloader=WEB_SETTINGS['use_reloader'])
