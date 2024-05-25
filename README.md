# Solarwinds Incident Alert Generator

## Overview
The Solarwinds Incident Alert Generator is a tool designed to help you stay on top of new incidents in your SolarWinds ServiceDesk. It generates a custom JavaScript bookmarklet that checks for the keyword "NEW INCIDENT" on the page and alerts you with an audio notification and a visual strobing effect.

## Features
- **Audio Notification**: Plays a selected MP3 file when a new incident is detected.
- **Visual Strobing**: Triggers a color strobing effect on the webpage.
- **Customizable**: Set the strobe rate and search frequency.
- **Audio Loop Option**: Choose whether the audio should play once or loop continuously.
- **Dark Mode**: User-friendly dark mode interface.

## How to Use

### 1. Generate the JavaScript Code:
   - Open the application.
   - Browse and select an MP3 file.
   - Enter the strobe rate in milliseconds (e.g., 500 for 500ms).
   - Enter the search frequency in milliseconds (e.g., 5000 for 5 seconds).
   - Check the "Loop Audio" checkbox if you want the audio to loop.
   - Click "Generate JavaScript Code" to produce the minified JavaScript bookmarklet code.
   - Click "Copy to Clipboard" to copy the generated code to the clipboard.

### 2. Add the Bookmarklet:
   - Open your web browser.
   - Create a new bookmark.
   - In the URL field of the bookmark, paste the JavaScript code copied to the clipboard.
   - Name the bookmark something meaningful (e.g., "Solarwinds Incident Alert").

### 3. Use the Bookmarklet:
   - Navigate to the SolarWinds ServiceDesk page in your browser.
   - Click the bookmark you created.
   - The script will start running and check for the keyword "NEW INCIDENT" every X milliseconds.
   - If the keyword is found, it will play the selected audio file and trigger a color strobing effect.
   - Move your mouse to stop the audio and strobing effect.

## Future Improvements
I'm planning to make improvements and add more tools.

## Installation

### Prerequisites
- Python 3.x
- Tkinter
- PyInstaller (for compiling to an executable)

### Running the Tool
1. **Clone the repository**:
   ```sh
   git clone https://github.com/yourusername/solarwinds-incident-alert-generator.git
2. **Navigate to the project directory**:
   ```sh
   cd solarwinds-incident-alert-generator
3. **Run the script**:
   ```sh
   python incident_alert_generator.py
   
### Compiling to an Executable
   To compile the script into a single executable file using PyInstaller:
1. **Install pyinstaller**:
   ```sh
   pip install pyinstaller
2. **Compile the script**:
   ```sh
   pyinstaller --onefile --windowed incident_alert_generator.py
