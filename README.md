# 🎨 Chroma-AI — Premium Image Colorization

> Breathe color into history. Upload a black-and-white photograph and watch a deep neural network paint it with realistic, vibrant, and natural colors in seconds.

---

## ✦ Technology Stack

| Layer | Technology | Description |
| :--- | :--- | :--- |
| **Frontend** | HTML5 · Vanilla CSS3 · JavaScript | Premium cinematic dark theme, glassmorphism, responsive comparison slider. |
| **Backend** | Python 3.11+ · Flask | Fast RESTful API for handling uploads and streaming images. |
| **AI Model** | PyTorch · DeOldify | State-of-the-art Generative Adversarial Network (GAN) for image colorization. |

---

## ✦ Key Features

* **🎨 Advanced GAN Colorization** — Powered by DeOldify (NoColorGAN / Artistic models) for unmatched realism.
* **🎛️ Dynamic Render Factor** — Adjust render factor dynamically between `10` and `45` to optimize resolution, color intensity, and detail.
* **🔄 Live Interactive Slider** — Compare the original grayscale image and the colorized result side-by-side using an interactive slider.
* **📂 Drag & Drop Uploads** — Clean, drag-and-drop landing area with custom file validation.
* **⚡ Instant Downloads** — Download high-resolution colorized images with a single click.
* **📱 Responsive Design** — Works beautifully across desktops, laptops, tablets, and smartphones.

---

## ✦ Project Structure

```text
colorizer/
│
├── app.py                     # Flask web server (routes, file uploads, API endpoints)
│
├── requirements.txt           # Version-locked package dependencies
│
├── model/
│   └── ai_pipeline.py         # DeOldify AI model initialization and execution pipeline
│
├── static/
│   ├── style.css              # Premium dark-theme glassmorphism UI styles
│   └── script.js              # Frontend interactive state, API calls, and slider behavior
│
├── templates/
│   └── index.html             # Interactive HTML5 user interface template
│
├── uploads/                   # [Auto-generated] Holds uploaded grayscale images
└── outputs/                   # [Auto-generated] Holds generated colorized images
```

---

## ✦ Installation & Running Guide

### 1. Prerequisites
* **Python 3.11** (Highly Recommended)
* **pip** (Python package installer)
* ~1.5 GB free disk space (for PyTorch libraries and model weights)

### 2. Set Up Virtual Environment (Mandatory)
Because modern global Python environments can cause library conflicts, you **must** use a virtual environment.

```powershell
# Open terminal inside the "colorizer" directory:

# Create the virtual environment
python -m venv venv

# Activate it:
# On Windows (PowerShell):
.\venv\Scripts\Activate.ps1

# On macOS / Linux:
source venv/bin/activate
```

### 3. Install Dependencies
Ensure your environment is active, then run:
```bash
pip install -r requirements.txt
```

### 4. Run the Application
Start the Flask web server:
```bash
python app.py
```

Access the application in your browser:
👉 **[http://127.0.0.1:5000](http://127.0.0.1:5000)**

> ℹ️ **Note on First Run:** The application will automatically download the pre-trained DeOldify model weights (`ColorizeArtistic_gen.pth`, ~243MB) directly to your `models/` folder. This download happens only once and is cached locally for all subsequent operations.

---

## ✦ API Reference

### `POST /colorize`
Uploads and processes an image using the AI pipeline.

* **Content-Type:** `multipart/form-data`
* **Form Parameters:**
  * `image`: `file` (Required. PNG, JPG, JPEG, BMP, or WebP)
  * `render_factor`: `integer` (Optional. Between `10` and `45`. Default: `35`)

* **Success Response (`200 OK`):**
  ```json
  {
    "original": "/uploads/image_1716210000_123.jpg",
    "colorized": "/outputs/colorized_image_1716210000_123.jpg",
    "elapsed": 2.4,
    "render_factor": 35
  }
  ```

* **Error Response (`400 Bad Request` or `500 Internal Server Error`):**
  ```json
  {
    "error": "No image provided"
  }
  ```

### `GET /uploads/<filename>`
Serves the uploaded source image.

### `GET /outputs/<filename>`
Serves the colorized output image.

---

## ✦ Troubleshooting & Fixes

| Problem | Root Cause | Solution |
| :--- | :--- | :--- |
| **`VersionConflict` / `fastai` / `fasthtml` error** | Trying to run using the global system Python instead of the virtual environment. | Make sure to run `.\venv\Scripts\Activate.ps1` first or use `.\venv\Scripts\python.exe .\app.py`. |
| **Slow first request** | The DeOldify model weights are downloading (~243MB). | Wait for the download to complete in the console. Future runs will be near-instant. |
| **`CUDA Out of Memory`** | PyTorch is running out of GPU memory. | The system is configured to run on CPU by default in `ai_pipeline.py` which works flawlessly for standard sizes. |