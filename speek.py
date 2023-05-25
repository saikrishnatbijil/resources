import pyaudio
import wave
import audioop
import time
import pygame

# Constants for audio settings
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000

# Set the initial volume level
initial_volume = 1.0

# Load your music file
music_file = "music.mp3"

# Initialize Pygame mixer and load music
pygame.mixer.init()
pygame.mixer.music.load(music_file)

# Function to play music
def play_music():
    pygame.mixer.music.play()

# Function to pause music
def pause_music():
    pygame.mixer.music.pause()

# Function to resume music
def resume_music():
    pygame.mixer.music.unpause()

# Function to adjust volume
def adjust_volume(volume):
    pygame.mixer.music.set_volume(volume)

# Function to detect speech
def detect_speech():
    audio = pyaudio.PyAudio()

    # Open the audio stream
    stream = audio.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)

    # Variables to track speech detection
    silent_frames = 0
    speech_started = False

    print("Listening for speech...")

    # Continuously monitor audio stream
    while True:
        # Read audio data from the stream
        data = stream.read(CHUNK)

        # Calculate the RMS energy of the audio data
        rms = audioop.rms(data, 2)

        # If RMS energy is below a threshold, consider it as silent
        if rms < 150:
            silent_frames += 1

            # If silent frames exceed a threshold, speech has likely stopped
            if silent_frames > 50 and speech_started:
                print("Speech stopped")
                return False
        else:
            silent_frames = 0

            # If speech has not started, consider it as speech start
            if not speech_started:
                print("Speech started")
                return True

        # Adjust the volume based on speech detection
        if speech_started:
            adjust_volume(0.5)
            pause_music()
        else:
            adjust_volume(initial_volume)
            resume_music()

    # Cleanup
    stream.stop_stream()
    stream.close()
    audio.terminate()

# Play the music initially
play_music()

# Variables to track the time of last speech detection
last_speech_time = time.time()

# Main program loop
while True:
    # Check for speech
    if detect_speech():
        # Reduce volume when speaking
        adjust_volume(0.5)
        pause_music()
        last_speech_time = time.time()
    else:
        # Increase volume when not speaking
        adjust_volume(initial_volume)
        resume_music()

    # Check the time difference since the last speech detection
    speech_time = time.time() - last_speech_time
    if speech_time >= 1:
        resume_music()
