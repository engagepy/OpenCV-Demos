# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Environment Setup

This is an OpenCV test scripts repository containing various computer vision experiments. The project uses Python 3 with virtual environments for dependency management.

### Setup Commands
```bash
# Create virtual environment
python3 -m venv env

# Activate virtual environment (Mac/Linux)
source env/bin/activate

# Activate virtual environment (Windows)
env/Scripts/activate.bat

# Install dependencies
pip3 install -r requirements.txt
```

### Running Scripts
```bash
# Basic execution pattern for most scripts
python3 <script_name>.py

# For corners.py (requires video file argument)
python3 corners.py /path/to/video/file.mp4
```

## Code Architecture

This repository contains standalone OpenCV demonstration scripts, each focusing on different computer vision techniques:

### Core Script Categories

**Real-time Camera Processing Scripts:**
- `face_eye_detect.py` - Face and eye detection using Haar cascades
- `alarm.py` - Motion detection with audio alerts using pygame
- `contour_drawing.py` - Motion detection with contour visualization
- `mask.py` - HSV color-based object masking and filtering
- `scroll.py` - Color-based gesture recognition with pyautogui integration

**Video Analysis Scripts:**
- `corners.py` - Lucas-Kanade optical flow tracking with ShiTomasi corner detection

### Common Patterns Across Scripts

**Camera Initialization:**
All real-time scripts use `cv2.VideoCapture(0)` for webcam access and follow this pattern:
```python
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    # Processing logic
    cv2.imshow('window_name', frame)
    if cv2.waitKey(10) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
```

**Motion Detection Architecture:**
Scripts like `alarm.py` and `contour_drawing.py` use frame differencing:
1. Capture two consecutive frames
2. Calculate absolute difference
3. Convert to grayscale and apply Gaussian blur
4. Apply binary thresholding and dilation
5. Find and process contours

**Color-based Detection:**
Scripts like `mask.py` and `scroll.py` use HSV color space for object detection:
1. Convert BGR to HSV
2. Define lower/upper color bounds
3. Create mask using `cv2.inRange()`
4. Apply mask or find contours

### Dependencies

- **numpy**: Array operations and mathematical computations
- **opencv-python**: Core computer vision functionality
- **pygame**: Audio playback for alarm system
- **pyautogui**: System automation for gesture control (scroll.py only)

### Key Technical Notes

- All scripts use 'q' key to quit video streams
- Motion detection uses contour area thresholding (typically 5000+ pixels)
- Audio files (`ocean.mp3`, `alert.wav`, `whistle.mp3`) are used for alarm notifications
- Camera resolution is dynamically retrieved using `cap.get(3)` and `cap.get(4)`
- HSV color bounds are manually tuned for specific lighting conditions

### Development Workflow

When adding new OpenCV scripts:
1. Follow the established camera initialization pattern
2. Use consistent window naming and exit conditions
3. Add any new dependencies to `requirements.txt`
4. Test with different lighting conditions for color-based detection
5. Consider adding audio feedback for interactive applications