# Forex Session Reminder Script

## Overview

This Python script serves as a reminder for Forex trading sessions, designed to run on Windows and notify the user when each Forex session begins and ends, according to South Africa Standard Time (SAST). The script will:

- Play a sound when each Forex session starts.
- Print a message to the command prompt indicating which session has started.
- Play a different sound when the session ends.
- Print a message to the command prompt indicating which session has ended.

The Forex sessions included are:

- **Sydney**: 12:00 AM - 8:00 AM SAST
- **Tokyo**: 2:00 AM - 10:00 AM SAST
- **London**: 10:00 AM - 6:00 PM SAST
- **New York**: 3:00 PM - 11:00 PM SAST

## Prerequisites

Before running the script, ensure that you have the following installed on your system:

- **Python 3.x**: Download and install from [here](https://www.python.org/downloads/).
- **Required Python libraries**: You can install them via `pip`:

  ```bash
  pip install pygame schedule
