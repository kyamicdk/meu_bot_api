from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return "API funcionando!"

@app.route("/bypass", methods=["POST"])
def bypass():
    data = request.get_json()
    link = data.get("link")
    return jsonify({"status": "ok", "result": f"Link recebido: {link}"})
