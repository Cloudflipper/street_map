# 🗺️ Street Map Generator

## 📖 Overview
**Street Map Generator** is a Python-based automation tool that can **generate high-resolution city map mosaics**.  
It uses Selenium to automatically navigate Baidu Maps at specific coordinates, capture screenshots of urban areas, crop them precisely, and merge them into one complete stitched map.

This tool can be used for:
- City visualization and topographic studies  
- Urban planning or UI prototyping  
- Background map generation for data visualization  
- Simulation environments for robotics or autonomous systems  

See SHANGHAI_RAW.png as an example.
---

## 🧩 Features
- 🌐 **Automated map capture** using Selenium and ChromeDriver  
- 📸 **Precise image cropping** with OpenCV to remove browser frames  
- 🧱 **Automatic image stitching** via Pillow  
- ⚙️ **Configurable coordinate range and resolution**  
- 🧮 **Extensible coordinate base** for different cities (e.g., Shanghai, Suzhou)  

---

## 🧠 File Descriptions

| File | Description |
|------|--------------|
| `get_pic.py` | Main script — handles map fetching, cropping, and stitching |
| `visit.py` | Early version for coordinate-based automated browsing |
| `click_test.py` | Mouse coordinate debugging tool for calibration |

---

## 🧰 Dependencies

Install required packages via pip:

```bash
pip install selenium opencv-python pillow tqdm pyautogui pywin32
```

You will also need:
- **Google Chrome**
- **ChromeDriver** (version must match your Chrome browser)

---

## ⚙️ Usage

### 1️⃣ Set Parameters
In `get_pic.py`, adjust parameters such as base coordinates and step size:

```python
# Base coordinates for Baidu Map
BASE_X = 13386335    # Suzhou
BASE_Y = 3583355

# Step size in map units
STEP_X = 7000
STEP_Y = 4000

# Capture grid size
for index_x in range(19):      # horizontal range
    for index_y in range(41):  # vertical range
        get_original_pic(index_x, index_y)
```

### 2️⃣ Run the Program

```bash
python get_pic.py
```

The script will:
1. Automatically open Chrome and navigate to target coordinates  
2. Take screenshots and save them to `pics3/`  
3. Automatically stitch them into one large image, e.g. `Suzhou.png`  

---

## 🖼️ Output Example
The final resolution depends on the number of rows and columns as well as image dimensions.  
Example: with `19 × 41` tiles of `1236×706` pixels → about **23,484 × 28,946 px** stitched image.

---

## ⚠️ Notes
- Excessive requests may trigger anti-bot mechanisms — use random `sleep()` delays.  
- The script will open many browser windows; do **not** close them manually.  
- Works best on **Windows** (uses `win32api` and `ctypes.windll` for mouse control).  
  Mac/Linux users need to replace mouse-related calls.

---


## 👤 Author
**Mingrui Li**  
University of Michigan – Computer Science
📧 cldflpr@umich.edu
