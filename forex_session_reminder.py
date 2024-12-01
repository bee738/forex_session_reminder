# Forex Session Reminder Script
# Author: BeeKid2.0
# Date: December 2024
# Description: This script plays reminder sounds for Forex trading sessions based on South Africa Standard Time (SAST).
# It uses the pygame library for sound and schedule library for managing session start and end times.
# Copyright (c) 2024 BeeKid2.0. All rights reserved.

import time
import schedule
import pygame
from datetime import datetime
import threading

# Initialize pygame for sound
pygame.mixer.init()

# Function to play a sound (you can replace the file path with your own sound file)
def play_start_sound():
    pygame.mixer.music.load("start_sound.mp3")  # Replace with your start session sound file
    pygame.mixer.music.play()

def play_end_sound():
    pygame.mixer.music.load("end_sound.mp3")  # Replace with your end session sound file
    pygame.mixer.music.play()

# Forex session start and end times in SAST (UTC +2)
forex_sessions = {
    'Sydney': {'start': '00:00', 'end': '08:00'},   # Sydney session start and end
    'Tokyo': {'start': '02:00', 'end': '10:00'},    # Tokyo session start and end
    'London': {'start': '10:00', 'end': '18:00'},   # London session start and end
    'New York': {'start': '15:00', 'end': '23:00'}, # New York session start and end
}

# Function to play a start sound and print a message for each session
def start_session(session_name):
    play_start_sound()
    print(f"Starting {session_name} session!")

# Function to play an end sound and print a message for each session
def end_session(session_name):
    play_end_sound()
    print(f"{session_name} session has ended!")

# Function to schedule sound reminders for each session
def set_reminders():
    for session, times in forex_sessions.items():
        schedule.every().day.at(times['start']).do(start_session, session_name=session)
        schedule.every().day.at(times['end']).do(end_session, session_name=session)

# Main loop to run the reminders
def run_reminders():
    set_reminders()
    while True:
        schedule.run_pending()
        time.sleep(1)  # Check for scheduled tasks every second

# Run the reminder system in a separate thread to allow non-blocking execution
if __name__ == "__main__":
    reminder_thread = threading.Thread(target=run_reminders)
    reminder_thread.daemon = True  # Allow the thread to exit when the main program ends
    reminder_thread.start()
    
    # Keep the main program running to prevent immediate exit
    while True:
        time.sleep(1000)  # You can adjust this to any duration, this keeps the script running
