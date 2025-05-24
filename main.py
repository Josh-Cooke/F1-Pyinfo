"""
A simple FastF1 example: Get lap times for a session and plot them.
"""
import fastf1
import matplotlib.pyplot as plt
import pandas as pd

# Enable FastF1 cache (optional, but recommended)
fastf1.Cache.enable_cache('fastf1_cache')

def plot_lap_times(year=2023, gp='Bahrain', session_type='Q'):
    # Load a session (e.g., Qualifying in Bahrain 2023)
    session = fastf1.get_session(year, gp, session_type)
    session.load()

    # Get all laps
    laps = session.laps
    print(laps.pick_driver('VER').pick_fastest())


if __name__ == "__main__":
    plot_lap_times()  # You can change the year, gp, and session_type as needed
