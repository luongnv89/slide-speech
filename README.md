# SlideSpeech: Auto Presentation Script

Introducing SlideSpeech, a tool designed to automate your PDF or PPTX presentations by synchronizing them with audio files. It dynamically adjusts slide durations based on the corresponding audio length and supports seamless transitions across slides.

### Key Features:

- **Format Compatibility**: Works effortlessly with both PDF and PPTX files.
- **Seamless Navigation**: Automatically progresses to the next slide as each audio file ends, ensuring a smooth presentation flow.
- **Sequential Audio Playback**: Synchronizes your content by playing audio files in order for every slide.
- **Flexible Presentation Management**: Choose from multiple presentations at startup, providing versatility for different scenarios.
- **Cross-Platform Support**: Compatible with Windows, macOS, and Linux, allowing broad accessibility.

SlideSpeech is the perfect solution for educators, trainers, corporate presenters, or anyone looking to enhance their presentation delivery. Explore and contribute on GitHub [Insert Link Here]. #OpenSource #PresentationTool #SlideSpeech

---

Enhance your presentations effortlessly with SlideSpeech!

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

### 1. Clone the Repository
First, clone the `slide-speech` repository to your local machine:

```bash
git clone https://github.com/luongnv89/slide-speech.git
cd slide-speech
```

### 2. Install Python
If you don't have Python installed, download and install it from [python.org](https://www.python.org/downloads/).

### 3. Install Required Libraries
Open a terminal or command prompt and run the following commands to install the required libraries:

```bash
pip install pyautogui pygame PyPDF2 python-pptx
```

### 4. Prepare Your Files
- **Presentations**: Place each presentation in its own folder under the `presentations` directory.
  - Each folder should contain:
    - A PDF or PPTX file (e.g., `slides.pdf` or `slides.pptx`).
    - An `audio` folder with audio files named `slide_1.wav`, `slide_2.wav`, etc.

#### File Structure
```
slide-speech/
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
├── slide-speech.py                 # Main script
└── README.md                       # Project documentation
```

---

## Usage

### 1. Run the Script
Open a terminal or command prompt, navigate to the folder containing the script, and run:

```bash
python slide-speech.py
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