from flask import Flask, render_template, request, send_from_directory, jsonify
import os
import time
from model.ai_pipeline import restore_image

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "outputs"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/colorize", methods=["POST"])
def colorize():
    if "image" not in request.files:
        return jsonify({"error": "No image provided"}), 400

    file = request.files["image"]
    if file.filename == "":
        return jsonify({"error": "No file selected"}), 400

    # Get render_factor from form (default 35)
    try:
        render_factor = int(request.form.get("render_factor", 35))
        render_factor = max(10, min(45, render_factor))
    except (ValueError, TypeError):
        render_factor = 35

    filename = file.filename
    name, ext = os.path.splitext(filename)
    unique = str(int(time.time() * 1000))
    safe_name = f"{name}_{unique}{ext}"

    input_path = os.path.join(UPLOAD_FOLDER, safe_name)
    file.save(input_path)

    output_name = "colorized_" + safe_name
    output_path = os.path.join(OUTPUT_FOLDER, output_name)

    start = time.time()
    try:
        restore_image(input_path, output_path)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    elapsed = round(time.time() - start, 1)

    return jsonify({
        "original":      f"/uploads/{safe_name}",
        "colorized":     f"/outputs/{output_name}",
        "elapsed":       elapsed,
        "render_factor": render_factor
    })


@app.route("/uploads/<filename>")
def uploads(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)


@app.route("/outputs/<filename>")
def outputs(filename):
    return send_from_directory(OUTPUT_FOLDER, filename)


if __name__ == "__main__":
    app.run(debug=True)