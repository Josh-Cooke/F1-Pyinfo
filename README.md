# F1 Pyinfo

A Python project that uses the [FastF1](https://theoehrly.github.io/Fast-F1/) package to fetch Formula 1 data and visualize it with graphs. This project is designed as a personal portfolio project to demonstrate data analysis and visualization skills.

## Features
- Fetches F1 session data (e.g., qualifying, race) for any season and Grand Prix
- Plots lap times for all drivers in a session using matplotlib
- Easily customizable for other types of F1 data and visualizations

## Requirements
- Python 3.8+
- fastf1
- matplotlib
- pandas

Install dependencies with:
```sh
pip install -r requirements.txt
```

## Usage
1. Run the script:
   ```sh
   python main.py
   ```
2. A matplotlib window will open showing lap times for all drivers in the selected session.
3. You can edit `main.py` to change the year, Grand Prix, or session type.

## Example Output
![Lap Times Example](https://raw.githubusercontent.com/theOehrly/Fast-F1/main/docs/_static/example_lap_times.png)

## Customization
- Change the session (year, Grand Prix, session type) in `main.py`.
- Modify the plotting code to visualize other data (e.g., speed traces, sector times).

## References
- [FastF1 Documentation](https://theoehrly.github.io/Fast-F1/)
- [matplotlib Documentation](https://matplotlib.org/)

---
*Created as a personal project to boost my CV and showcase Python data analysis skills.*
