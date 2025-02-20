#!/usr/bin/env python3
import os
# Force Qt to use the X11 (xcb) platform instead of Wayland.
os.environ["QT_QPA_PLATFORM"] = "xcb"

import numpy as np
import subprocess
import pyqtgraph as pg
import atexit
from pyqtgraph import ColorMap

# Import all Qt classes from pyqtgraph’s Qt wrapper so they use the same binding.
from pyqtgraph.Qt import QtCore, QtWidgets

# Define blue-red colormap
colors = [
    (0, (0, 0, 255)),        # Blue for 0% to 70%
    (0.95, (255, 255, 0)),    # Yellow starts at 70% and goes up to 90%
    (0.97, (255, 0, 0)),      # Red starts at 90% and goes up to 100%
    (1, (255, 0, 0))          # Red continues to 100%
]

gain = 40  # Initial gain

# Configuration
TOTAL_LINES = 1200           # Lines per sweep
FREQ_BINS_PER_LINE = 5       # Frequency bins per line
TOTAL_FREQ_BINS = TOTAL_LINES * FREQ_BINS_PER_LINE  # Total frequency bins
WATERFALL_DEPTH = 100        # Number of sweeps stored

# Global Data Storage
power_values = []
max_hold = None
waterfall_data = np.full((WATERFALL_DEPTH, TOTAL_FREQ_BINS), -100)
frequencies = np.linspace(0, 6e9, TOTAL_FREQ_BINS)

# Set up QApplication using QtWidgets from pyqtgraph’s Qt wrapper
app = QtWidgets.QApplication.instance()
if not app:
    app = QtWidgets.QApplication([])

# Create a QMainWindow to contain both the UI (button) and the plot
main_window = QtWidgets.QMainWindow()
main_widget = QtWidgets.QWidget(main_window)
main_layout = QtWidgets.QVBoxLayout(main_widget)

# Create the GraphicsLayoutWidget for the plots (provided by pyqtgraph)
win = pg.GraphicsLayoutWidget(show=True, title="HackRF Spectrum Sweep with Waterfall")
win.resize(1000, 800)
win.setWindowTitle("HackRF Spectrum Sweep with Waterfall")
layout = win.addLayout()

# Top Plot: Spectrum
plot = layout.addPlot(title="Real-Time Spectrum with Max Hold")
plot.setLabel("bottom", "Frequency (Hz)")
plot.setLabel("left", "Power (dB)")
plot.setXRange(0, 6e9)
plot.setYRange(-100, 0)

layout.nextRow()

# Curves for real-time and max-hold plots
real_time_curve = plot.plot(pen="y")
max_hold_curve = plot.plot(pen="r")
color_map = ColorMap(*zip(*colors))
lut = color_map.getLookupTable(start=0.0, stop=1.0, nPts=256)

# Waterfall Plot Class
class WaterfallPlotWidget:
    def __init__(self, layout):
        self.layout = layout
        self.history_size = WATERFALL_DEPTH
        self.counter = 0
        self.create_plot()

    def create_plot(self):
        self.plot = self.layout.addPlot()
        self.plot.setLabel("bottom", "Frequency", units="Hz")
        self.plot.setLabel("left", "Time")
        self.plot.setYRange(0, self.history_size)  # Y-axis covers the history size
        self.waterfall_img = pg.ImageItem()
        self.plot.addItem(self.waterfall_img)
        self.plot.invertY(True)  # Invert Y so new sweeps appear at the top

    def update_plot(self, data):
        self.counter += 1
        # Update the image position to move downward over time.
        self.waterfall_img.setImage(data.T, autoLevels=False, lut=lut, levels=(0, 1))
        self.waterfall_img.setPos(0, self.counter if self.counter < self.history_size else self.history_size)

waterfall_widget = WaterfallPlotWidget(layout)

# Process HackRF Sweep Output
def process_line(line):
    parts = line.strip().split(", ")
    try:
        values = list(map(float, parts[-FREQ_BINS_PER_LINE:]))
        return values if len(values) == FREQ_BINS_PER_LINE else []
    except ValueError:
        return []

def update_plot():
    global power_values, max_hold, waterfall_data

    if len(power_values) == TOTAL_FREQ_BINS:
        if max_hold is None:
            max_hold = np.array(power_values)
        else:
            max_hold = np.maximum(max_hold, power_values)
        
        real_time_curve.setData(frequencies, power_values)
        max_hold_curve.setData(frequencies, max_hold)
        
        # Shift waterfall history and insert new data at the top
        waterfall_data[1:, :] = waterfall_data[:-1, :]
        waterfall_data[0, :] = np.array(power_values)

        # Normalize the waterfall data for display
        min_power, max_power = np.min(waterfall_data), np.max(waterfall_data)
        if max_power - min_power > 1e-3:
            scaled_waterfall = (waterfall_data - min_power) / (max_power - min_power)
        else:
            scaled_waterfall = np.zeros_like(waterfall_data)

        # Update the waterfall image
        waterfall_widget.waterfall_img.setImage(
            scaled_waterfall.T,  # Transpose for correct orientation
            autoLevels=False,
            lut=lut,
            levels=(0, 1)
        )

        power_values.clear()

# Create a button and connect its click signal to update the gain
def button_clicked():
    global gain, process
    try:
        new_gain = float(gain_input.text())
        print(f'Updated Gain: {new_gain}')
        gain = new_gain
        
        # Terminate the current HackRF sweep process if it exists
        if process:
            process.terminate()
        
        # Restart the HackRF sweep process with the new gain
        process = subprocess.Popen(
            ["hackrf_sweep", "-l", "30", "-g", str(gain)],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )
        
    except ValueError:
        print("Invalid input for gain. Please enter a valid number.")

# Initialize process as None
process = None

button = QtWidgets.QPushButton('Apply Gain')
button.clicked.connect(button_clicked)

# Create a widget to hold UI elements (gain label, input, and button)
ui_widget = QtWidgets.QWidget()
ui_layout = QtWidgets.QVBoxLayout()
ui_layout.addWidget(QtWidgets.QLabel("Enter Gain:"))
gain_input = QtWidgets.QLineEdit()
gain_input.setText(str(gain))
ui_layout.addWidget(gain_input)
ui_layout.addWidget(button)
ui_widget.setLayout(ui_layout)

# Position the UI widget in the top-right corner (adjust as needed)
button_width = 100
button_height = 40
ui_widget.setGeometry(900, 20, button_width, button_height)

# Instead of adding 'win' directly (which may cause a type mismatch), wrap it in a container widget.
win_container = QtWidgets.QWidget()
win_container_layout = QtWidgets.QVBoxLayout(win_container)
win_container_layout.addWidget(win)
main_layout.addWidget(win_container)

# Set up and display the main window
main_window.setCentralWidget(main_widget)
main_window.show()

# Add the UI widget as an overlay (menu widget) on the main window
main_window.setMenuWidget(ui_widget)

try:
    # Launch the initial HackRF sweep process.
    process = subprocess.Popen(
        ["hackrf_sweep", "-l", "30", "-g", str(gain)],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    )
    
    def cleanup():
        if process:
            process.terminate()
    atexit.register(cleanup)

    lines_processed = 0
    def read_data():
        global power_values, lines_processed
        for line in process.stdout:
            if line.strip():
                power_values.extend(process_line(line))
                lines_processed += 1
                if lines_processed >= TOTAL_LINES:
                    update_plot()
                    lines_processed = 0
                    break
    
    timer = QtCore.QTimer()
    timer.timeout.connect(read_data)
    timer.start(10)
    update_plot()
    
    # Start the Qt event loop in a way that works for both PyQt5 and PyQt6
    if hasattr(app, "exec_"):
        exit_code = app.exec_()
    else:
        exit_code = app.exec()
    import sys
    sys.exit(exit_code)

except Exception as e:
    print(f"Error: {e}")
