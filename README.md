# SlideSpeech: Auto Presentation Script

SlideSpeech is a Python script that automates the presentation of PDF or PPTX files, playing an audio file for each slide. The time spent on each slide depends on the duration of the corresponding audio file. The script supports **multiple presentations**, allowing you to choose which one to start when running the script.

---

## Table of Contents
1. [Features](#features)
2. [Requirements](#requirements)
3. [Setup](#setup)
4. [Usage](#usage)
5. [File Structure](#file-structure)
6. [License](#license)
7. [Contributing](#contributing)
8. [Notes](#notes)

---

## Features
- Supports **PDF** and **PPTX** presentation formats.
- Automatically navigates to the next slide after the audio file finishes playing.
- Audio files are played sequentially for each slide.
- Dynamic slide duration based on the length of the audio file.
- Supports **multiple presentations**—choose which one to start when running the script.
- Cross-platform: Works on **Windows**, **macOS**, and **Linux**.

---

## Requirements
- Python 3.6 or higher.
- The following Python libraries:
  - `pyautogui`
  - `pygame`
  - `PyPDF2`
  - `python-pptx` (optional, for PPTX support)

---

## Setup

### 1. Install Python
If you don't have Python installed, download and install it from [python.org](https://www.python.org/downloads/).

### 2. Install Required Libraries
Open a terminal or command prompt and run the following commands to install the required libraries:

```bash
pip install pyautogui pygame PyPDF2 python-pptx
```

### 3. Prepare Your Files
- **Presentations**: Place each presentation in its own folder under the `presentations` directory.
  - Each folder should contain:
    - A PDF or PPTX file (e.g., `slides.pdf` or `slides.pptx`).
    - An `audio` folder with audio files named `slide_1.wav`, `slide_2.wav`, etc.

#### File Structure
```
SlideSpeech/
│
├── presentations/                  # Folder containing all presentations
│   ├── presentation_1/             # Folder for Presentation 1
│   │   ├── slides.pdf              # PDF or PPTX file
│   │   └── audio/                  # Folder for audio files
│   │       ├── slide_1.wav
│   │       ├── slide_2.wav
│   │       └── ...
│   │
│   ├── presentation_2/             # Folder for Presentation 2
│   │   ├── slides.pptx
│   │   └── audio/
│   │       ├── slide_1.wav
│   │       ├── slide_2.wav
│   │       └── ...
│   └── ...
│
├── SlideSpeech.py                  # Main script
└── README.md                       # Project documentation
```

---

## Usage

### 1. Run the Script
Open a terminal or command prompt, navigate to the folder containing the script, and run:

```bash
python SlideSpeech.py
```

### 2. Select a Presentation
The script will list all available presentations. Enter the number of the presentation you want to start.

Example:
```
Available presentations:
1. presentation_1
2. presentation_2
Select a presentation (number): 1
```

### 3. Let the Script Run
The script will:
1. Open the selected presentation.
2. Enter full-screen mode.
3. Play the audio for each slide and advance automatically.

---

## License
SlideSpeech is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## Contributing
We welcome contributions to SlideSpeech! If you'd like to contribute, please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Make your changes and commit them with clear messages.
4. Submit a pull request.

For more information, see our [Contribution Guidelines](CONTRIBUTING.md).

---

## Notes
- Ensure the audio files are named sequentially (`slide_1.wav`, `slide_2.wav`, etc.) and correspond to each slide.
- The script uses the `right` arrow key to navigate slides, which works in most presentation software.
- If you're using a PPTX file, ensure the `python-pptx` library is installed.
- Test the script with your presentation and audio files before using it in a live setting.

---

## Example Use Cases
- **Classroom Lectures**: Automate slide transitions while you focus on teaching.
- **Business Pitches**: Deliver polished, hands-free presentations.
- **Museums/Kiosks**: Create interactive, self-running exhibits.

---

## Support
If you encounter any issues or have questions, feel free to reach out or open an issue on the project repository.

---

Enjoy automating your presentations with **SlideSpeech**! 🚀