# DIY Security Camera with Motion Detection

A simple motion detection security camera built with Python and OpenCV. The application monitors a webcam feed, detects changes between consecutive frames, and plays an alarm sound when significant movement is detected.

## Features

- **Real-Time Monitoring:** Captures live video from a webcam.
- **Motion Detection:** Uses image differencing to identify changes between consecutive frames.
- **Contour Filtering:** Ignores small detected regions using a minimum contour area threshold.
- **Alarm System:** Plays an alert sound when sufficiently large motion regions are detected.
- **Simple Controls:** Press `ESC` to close the application.

## Technologies Used

- Python
- OpenCV
- winsound (built-in Windows module)

## Requirements

- Python 3.x
- OpenCV
- A working webcam
- Windows operating system
- A `sound.wav` alarm audio file

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/YOUR-USERNAME/diy-security-camera.git
   ```

2. Navigate to the project directory:

   ```bash
   cd diy-security-camera
   ```

3. Install OpenCV:

   ```bash
   pip install opencv-python
   ```

4. Place your `sound.wav` file in the same directory as the Python script.

## Usage

Run the application:

```bash
python diy_security_camera.py
```

The webcam feed will open in a window titled `Security Camera`. When significant movement is detected, the application plays the alarm sound.

Press `ESC` to exit.

## How It Works

1. Captures consecutive frames from the webcam.
2. Calculates the absolute difference between the frames using `cv2.absdiff()`.
3. Converts the difference image to grayscale.
4. Applies binary thresholding to highlight significant pixel changes.
5. Detects contours in the resulting image.
6. Filters out contours with an area smaller than 5,000 pixels.
7. Plays an alarm sound when a contour meets the area threshold.

## Project Structure

```text
diy-security-camera/
├── diy_security_camera.py
├── sound.wav
└── README.md
```

## Limitations

- The application detects visual changes, not specifically people.
- Lighting changes and camera movement may trigger false alarms.
- The alarm may be triggered repeatedly while significant movement continues.
- The `winsound` module makes the alarm system Windows-specific.

## Future Improvements

- Add a cooldown period between alarms.
- Save images or video clips when motion is detected.
- Improve detection accuracy under changing lighting conditions.
- Add person detection using a computer vision model.

## License

This project is available for educational and personal use. Add a license file if you want to specify formal reuse and distribution terms.
