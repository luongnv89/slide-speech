import os
import time
import pyautogui
import pygame
from PyPDF2 import PdfReader
from pptx import Presentation  # Optional for PPTX
import subprocess  # To open the presentation file
import sys  # To detect the operating system
import logging
from rich.console import Console
from rich.logging import RichHandler

# Initialize rich console
console = Console()

# Configure logging with rich
logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
    handlers=[RichHandler(console=console, rich_tracebacks=True)]
)
logger = logging.getLogger("rich")

# Initialize pygame for audio
pygame.mixer.init()

def list_presentations(presentations_dir):
    """List all available presentations in the presentations directory."""
    presentations = []
    try:
        for entry in os.listdir(presentations_dir):
            presentation_path = os.path.join(presentations_dir, entry)
            if os.path.isdir(presentation_path):
                presentations.append(entry)
        logger.info(f"Found {len(presentations)} presentations in '{presentations_dir}'.")
    except Exception as e:
        logger.error(f"Error listing presentations: {e}")
    return presentations

def select_presentation(presentations):
    """Allow the user to select a presentation from the list."""
    console.print("Available presentations:", style="bold green")
    for i, presentation in enumerate(presentations):
        console.print(f"{i + 1}. {presentation}", style="bold blue")
    while True:
        try:
            choice = int(console.input("Select a presentation (number): "))
            if 1 <= choice <= len(presentations):
                return presentations[choice - 1]
            else:
                console.print("Invalid choice. Please try again.", style="bold red")
        except ValueError:
            console.print("Invalid input. Please enter a number.", style="bold red")

def open_presentation(presentation_path):
    """Open the presentation file using the default application and reset to Slide 1."""
    try:
        if os.path.exists(presentation_path):
            if sys.platform == "win32":  # Windows
                os.startfile(presentation_path)
            elif sys.platform == "darwin":  # macOS
                # Close Preview if it's already open
                subprocess.run(['osascript', '-e', 'tell application "Preview" to quit'])
                time.sleep(1)  # Wait for Preview to close
                # Open the file in Preview
                subprocess.run(['open', presentation_path])
                time.sleep(2)  # Wait for Preview to open
                # Force navigation to the first slide using arrow keys
                pyautogui.press('left', presses=100)  # Press left arrow many times to ensure we're at the first slide
                time.sleep(1)  # Wait for navigation to complete
            else:  # Linux
                subprocess.run(['xdg-open', presentation_path])
            time.sleep(5)  # Wait for the application to open
            logger.info(f"Successfully opened presentation: {presentation_path}")
            return True
        else:
            logger.error(f"Presentation file {presentation_path} not found.")
            return False
    except Exception as e:
        logger.error(f"Error opening presentation: {e}")
        return False

def enter_full_screen(app_type="powerpoint"):
    """
    Enter full-screen presentation mode based on the operating system and application type.

    Parameters:
    app_type (str): The application type to target. Options are "powerpoint" or "pdf".
    """
    try:
        time.sleep(2)  # Wait for the application to load
        if sys.platform == "win32":  # Windows
            pyautogui.press('f5')  # F5 is the shortcut for starting a slideshow in most apps
        elif sys.platform == "darwin":  # macOS
            if app_type == "powerpoint":
                pyautogui.press('f5')  # Shortcut for PowerPoint on macOS
                logger.info("Trying to enter PowerPoint presentation mode...")
            elif app_type == "pdf":
                # AppleScript to enter full-screen mode in Preview for PDFs
                script = '''
                tell application "Preview"
                    activate
                    delay 1
                    tell application "System Events" to keystroke "f" using {command down, control down}
                end tell
                '''
                logger.info("Trying to enter full-screen mode in Preview...")
                try:
                    subprocess.run(['osascript', '-e', script], check=True)
                    logger.info(f"Successfully entered {app_type} full-screen mode.")
                except subprocess.CalledProcessError as e:
                    logger.error(f"Failed to enter full-screen mode for {app_type}: {e}")
            else:
                raise ValueError("Invalid app_type. Use 'powerpoint' or 'pdf'.")
        else:  # Linux
            pyautogui.press('f5')  # Default to F5 for Linux (may vary by PDF viewer)
        time.sleep(2)  # Wait for the presentation to enter full-screen mode
    except Exception as e:
        logger.error(f"Error entering full-screen mode: {e}")

def get_audio_duration(audio_file):
    """Get the duration of the audio file in seconds."""
    try:
        if os.path.exists(audio_file):
            sound = pygame.mixer.Sound(audio_file)
            return sound.get_length()
        else:
            logger.error(f"Audio file {audio_file} not found.")
            return 0
    except Exception as e:
        logger.error(f"Error getting audio duration: {e}")
        return 0

def play_audio(audio_file):
    """Play the specified audio file."""
    try:
        if os.path.exists(audio_file):
            pygame.mixer.music.load(audio_file)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():  # Wait for the audio to finish playing
                time.sleep(0.1)
        else:
            logger.error(f"Audio file {audio_file} not found.")
    except Exception as e:
        logger.error(f"Error playing audio: {e}")

def auto_present_pdf(pdf_path, audio_folder):
    """Automatically present a PDF and play audio for each slide."""
    try:
        reader = PdfReader(pdf_path)
        num_slides = len(reader.pages)
        logger.info(f"Starting presentation with {num_slides} slides...")
        for slide_num in range(num_slides):
            logger.info(f"Presenting slide {slide_num + 1}")
            audio_file = os.path.join(audio_folder, f"slide_{slide_num + 1}.wav")
            play_audio(audio_file)  # Play audio and wait for it to finish
            pyautogui.press('right')  # Immediately go to the next slide
    except Exception as e:
        logger.error(f"Error during PDF presentation: {e}")

def auto_present_pptx(pptx_path, audio_folder):
    """Automatically present a PPTX and play audio for each slide."""
    try:
        presentation = Presentation(pptx_path)
        num_slides = len(presentation.slides)
        logger.info(f"Starting presentation with {num_slides} slides...")
        for slide_num in range(num_slides):
            logger.info(f"Presenting slide {slide_num + 1}")
            audio_file = os.path.join(audio_folder, f"slide_{slide_num + 1}.wav")
            play_audio(audio_file)  # Play audio and wait for it to finish
            pyautogui.press('right')  # Immediately go to the next slide
    except Exception as e:
        logger.error(f"Error during PPTX presentation: {e}")

if __name__ == "__main__":
    # Path to the presentations directory
    presentations_dir = "./presentations"

    # List available presentations
    presentations = list_presentations(presentations_dir)
    if not presentations:
        logger.error("No presentations found. Please add presentations to the 'presentations' folder.")
        exit()

    # Let the user select a presentation
    selected_presentation = select_presentation(presentations)
    presentation_folder = os.path.join(presentations_dir, selected_presentation)

    # Find the presentation file (PDF or PPTX)
    presentation_path = None
    file_type = 'powerpoint'
    try:
        for file in os.listdir(presentation_folder):
            if file.endswith('.pptx'):
                if file.startswith('~$'):
                    continue  # Skip temporary PowerPoint files
                presentation_path = os.path.join(presentation_folder, file)
                break
            elif file.endswith('.pdf'):
                presentation_path = os.path.join(presentation_folder, file)
                file_type = 'pdf'
                break

        if not presentation_path:
            logger.error(f"No PDF or PPTX file found in the '{selected_presentation}' folder.")
            exit()

        # Path to the audio files
        audio_folder = os.path.join(presentation_folder, "audio")

        # Open the presentation and enter full-screen mode
        if open_presentation(presentation_path):
            enter_full_screen(file_type)

            # Determine the file type and call the appropriate function
            if presentation_path.endswith('.pdf'):
                auto_present_pdf(presentation_path, audio_folder)
            elif presentation_path.endswith('.pptx'):
                auto_present_pptx(presentation_path, audio_folder)
            else:
                logger.error("Unsupported file format. Please use a PDF or PPTX file.")
    except Exception as e:
        logger.error(f"An error occurred: {e}")