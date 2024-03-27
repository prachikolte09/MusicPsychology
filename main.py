from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from music21 import stream, note
import json
import random

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
music_concepts = {
    "harmony": ["Simple", "Complex"],
    "beat": ["Slow", "Medium", "Fast"],
    "instrument": ["Piano", "Guitar", "Violin"]
}

# Load songs from JSON file

songs = {
    "calming": [
        "https://youtu.be/gxvpOq8JlPI?t=864",
        "https://youtu.be/qbzXvzIos4U?t=1725",
        "https://youtu.be/Llour2YvsiI?t=513"
    ],
    "energizing": [
        "https://www.youtube.com/watch?v=h3DwcJiEuYI&ab_channel=Aimi",
        "https://youtu.be/tU5gBSrp0C8?t=824",
        "https://www.youtube.com/watch?v=RZV4oXuTZlA&ab_channel=HeyBearSensory"
    ]
}


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/shuffle_music")
async def shuffle_music(heartbeat: int):
    if heartbeat > 80:
        # Select a random song for high heartbeat

        song = random.choice(songs["calming"])
    else:
        # Select a random song for low heartbeat
        # sleeping heartrate is between 40-50
        song = random.choice(songs["energizing"])
    return JSONResponse({"song": song})


def calculate_bpm(heartbeat: int) -> int:
    # Ensure BPM stays within a reasonable range (60-180 BPM) could be customized a little
    return max(60, min(180, heartbeat))
def generate_melody(seed_note):
    # Generate a short melody based on the given seed note
    generated_notes = [seed_note, seed_note + 2, seed_note + 4]
    generated_durations = [1.0, 0.5, 0.5]  # Example durations

    # Create a music21 stream object
    generated_score = stream.Stream()
    for note_value, duration in zip(generated_notes, generated_durations):
        new_note = note.Note(midi=note_value)
        new_note.duration.quarterLength = duration
        generated_score.append(new_note)

    # Save the generated melody to a MIDI file
    generated_score.write("midi", "generated_melody.mid")
    return "generated_melody.mid"

@app.get("/customize_music/", response_class=HTMLResponse)
async def customize_music(request: Request):
    return templates.TemplateResponse("customize_music.html", {"request": request, "music_concepts": music_concepts})

@app.post("/generate_music/")
async def generate_music(mood: str, heartbeat: int, harmony: str, beat: str, instrument: str):
    # Adjust BPM based on heartbeat data
    bpm = calculate_bpm(heartbeat)

    # Generate customized music based on mood, adjusted BPM, and selected music concepts
    generated_music = f"Customized music generated for mood: {mood}, Heartbeat: {heartbeat}, Harmony: {harmony}, Beat: {beat}, Instrument: {instrument}, BPM: {bpm}"
    return JSONResponse({"music": generated_music})

@app.get("/generate_music/{seed_note}")
async def generate_music_from_seed(seed_note: int):
    # Generate melody based on the provided seed note
    melody_file = generate_melody(seed_note)

    # Return the generated melody file as a response
    return FileResponse(melody_file, media_type="audio/midi")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
