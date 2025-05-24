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
    drivers = laps['Driver'].unique()

    plt.figure(figsize=(10, 6))
    for drv in drivers:
        drv_laps = laps.pick_driver(drv)
        plt.plot(drv_laps['LapNumber'], drv_laps['LapTime'].dt.total_seconds(), label=drv)

    plt.xlabel('Lap Number')
    plt.ylabel('Lap Time (s)')
    plt.title(f'{year} {gp} {session_type} - Lap Times by Driver')
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_lap_times()  # You can change the year, gp, and session_type as needed
