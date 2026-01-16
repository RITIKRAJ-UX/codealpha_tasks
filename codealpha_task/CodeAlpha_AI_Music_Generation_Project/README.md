# AI Music Generation Project 🎵

## Overview
This project demonstrates **music generation using Artificial Intelligence**.
Using Python and **LSTM (Long Short-Term Memory) neural networks**, the model learns musical patterns from MIDI files and generates new music automatically.

## Features
- Reads and processes MIDI music files
- Extracts notes and chords using `music21`
- Converts musical sequences into numerical data
- Trains LSTM neural network to learn note sequences
- Generates new music and exports as a MIDI file
- Fully automatic music generation

## Technologies Used
- **Python 3.8+**
- **TensorFlow / Keras** for LSTM model
- **NumPy** for data processing
- **music21** for MIDI file processing
- Optional: **Google Colab** for faster training

## Project Structure
```
AI_Music_Project/
 ├── music_dataset/      # Folder containing MIDI files
 │     ├── song1.mid
 │     ├── song2.mid
 ├── music_ai.py         # Main Python code
 ├── README.md           # Project documentation
 └── generated_music.mid # Example output (optional)
```

## Installation

1. **Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/AI_Music_Project.git
cd AI_Music_Project
```

2. **Install required libraries**
```bash
pip install music21 tensorflow numpy
```

3. **Add MIDI files**
- Place your `.mid` files inside `music_dataset/`

## Usage

1. Open `music_ai.py` in your Python IDE or Google Colab
2. Run the script:
```bash
python music_ai.py
```
3. The AI will generate music and save it as `generated_music.mid`
4. Open the MIDI file using VLC, Windows Media Player, or any MIDI player

## Example Output
- The generated music will be saved as:
```
generated_music.mid
```
- Play it using any media player

## Deployment
- Can be run **locally on a laptop**
- Can also be run on **Google Colab** for faster processing
- Fully automatic generation of original music

## Contributing
- Feel free to fork this repository and improve the model
- You can add more MIDI datasets for better music quality

## Author
**Ritik Raj**  
BCA Student  

## License
This project is open-source and free to use.