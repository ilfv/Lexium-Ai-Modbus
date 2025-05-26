# LexiumAI

**LexiumAI** is an intelligent vision-based application designed to process real-time video from a webcam using a neural network. It determines the angle of rotation of detected objects and communicates control data to a Twido PLC via the Modbus RTU protocol.

---

## 🔧 Installation & Setup

### 1. Extract the Archive
Unpack the contents of the archive to a convenient location on your computer.

### 2. Install Python (version 3.8.9+)

> ⚠️ During installation `Add Python to system PATH`

### 3. Install Dependencies
Once Python is installed, run the provided `setup.bat` script. You can double-click it or run it from the command line.  
This script will automatically install all necessary Python libraries required to run the program.

### 4. Run the Application
After installation, launch the program from the command line using:

```bash
python main.py
````

---

## ⚙️ Configuration

### Camera Selection

If you have multiple webcams connected, open the `config.json` file and set:

```json
"camera.cv2_index": 0
```

Change the `0` to the index of the camera you want to use (`0` to `n-1`).

### Modbus RTU Settings

To configure PLC communication, edit parameter `modbus` value(config.json) 

---

## ⚠️ Recommendations for Accurate Detection

Due to the neural network’s training data:

* Avoid wearing **green or red clothing**, especially **green shirts** or holding **ping-pong balls**.
* These items may be falsely detected as the target object.
* The system attempts to filter out such artifacts, but following these tips will improve detection accuracy and performance.

---

## ✅ Features

* Real-time webcam image processing
* Object detection with angle estimation
* Direct PLC control via Modbus RTU
* Easily configurable via `config.json`
