# FastAPI Music  Psychology Project

This project is a FastAPI-based web application for generating customized music based on user preferences such as mood, heartbeat, harmony, beat, and instrument. It utilizes the `music21` library and a pre-trained neural network to generate melodies.

## Features

- **Customize Music**: Users can input their mood, heartbeat, and select options for harmony, beat, and instrument to generate personalized music compositions.
- **Generate Music**: The application generates music based on user inputs using a pre-trained neural network and saves the generated music as MIDI files.
- **Responsive Interface**: The web interface is designed to be user-friendly and responsive across various devices.

## Setup Instructions

1. **Clone the Repository**:
    ```
    git clone https://github.com/your_username/MusicPsychology.git
    ```

2. **Install Dependencies**:
    ```
    cd MusicPsychology
    pip install -r requirements.txt
    ```

3. **Run the Server**:
    ```
    uvicorn app:app --reload
    ```

4. **Access the Web Interface**:
   Open a web browser and navigate to `http://localhost:8000` to access the web application.

## Usage

1. **Customize Music**:
    - Visit the `/customize_music/` endpoint to access the customization form.
    - Input your mood, heartbeat, and select options for harmony, beat, and instrument.
    - Click the "Generate Music" button to generate personalized music.

2. **Generate Music from Seed Note**:
    - You can also generate music based on a specific seed note by visiting the `/generate_music/{seed_note}` endpoint.
    - Replace `{seed_note}` with the desired MIDI note value (e.g., `/generate_music/60` for middle C).

## Additional Notes

- **Neural Network Model**: Replace the dummy function `generate_melody` in main project folder with your actual music generation logic using a pre-trained neural network model.
- **Customization Options**: Extend the customization options and music generation capabilities based on your requirements and the capabilities of your neural network model.

## 