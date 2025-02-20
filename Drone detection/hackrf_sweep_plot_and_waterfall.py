import numpy as np
import subprocess
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout, QMainWindow, QLineEdit, QLabel
import atexit
from pyqtgraph import ColorMap

# Define blue-red colormap
colors = [
    (0, (0, 0, 255)),        # Blue for 0% to 70%
    (0.95, (255, 255, 0)),    # Yellow starts at 70% and goes up to 90%
    (0.97, (255, 0, 0)),      # Red starts at 90% and goes up to 100%
    (1, (255, 0, 0))         # Red continues to 100%
]

lna_gain = 32   # Initial lna gain
gain = 40       # Initial gain

# Configuration
TOTAL_LINES = 1200  
FREQ_BINS_PER_LINE = 5  
TOTAL_FREQ_BINS = TOTAL_LINES * FREQ_BINS_PER_LINE  
WATERFALL_DEPTH = 100  

# Global Data Storage
power_values = []
max_hold = None
waterfall_data = np.full((WATERFALL_DEPTH, TOTAL_FREQ_BINS), -100)
frequencies = np.linspace(0, 6e9, TOTAL_FREQ_BINS)

# PyQtGraph Setup
app = QApplication.instance()
if not app:
    app = QApplication([])

# Create Main Window
main_window = QMainWindow()
main_widget = QWidget(main_window)
main_layout = QVBoxLayout(main_widget)

# Create the GraphicsLayoutWidget for the plots
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

# Curves
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
        self.plot.setYRange(0, self.history_size)  
        self.waterfall_img = pg.ImageItem()
        self.plot.addItem(self.waterfall_img)
        self.plot.invertY(True)

    def update_plot(self, data):
        self.counter += 1
        # Update the image position to move downwards
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

        waterfall_data[1:, :] = waterfall_data[:-1, :]
        waterfall_data[0, :] = np.array(power_values)

        min_power, max_power = np.min(waterfall_data), np.max(waterfall_data)
        if max_power - min_power > 1e-3:  
            scaled_waterfall = (waterfall_data - min_power) / (max_power - min_power)
        else:
            scaled_waterfall = np.zeros_like(waterfall_data)  

        waterfall_widget.waterfall_img.setImage(
            scaled_waterfall.T,  
            autoLevels=False,
            lut=lut,
            levels=(0, 1)  
        )

        power_values.clear()

def reset_max_hold():
    global max_hold
    max_hold = None
    max_hold_curve.setData(frequencies, np.full_like(frequencies, -200))

def start_hackrf():
    """ Start the HackRF process """
    global gain, lna_gain, process
    process = subprocess.Popen(
        ["hackrf_sweep", "-l", str(lna_gain), "-g", str(gain)],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    )

def stop_hackrf():
    """ Stop the HackRF process """
    global process
    if process:
        process.terminate()

def restart_hackrf():
    """ Restart HackRF with the new gain and resume data reading """
    stop_hackrf()
    start_hackrf()


def apply_gain():
    """ Apply new gain value and restart the HackRF process """
    global gain
    try:
        gain = int(gain_input.text())
        restart_hackrf()
        reset_max_hold()
    except ValueError:
        print("Invalid gain input.")

def apply_lna_gain():
    """Apply new lna gain value and restart the HackRF process"""
    global lna_gain
    try:
        lna_gain = int(lna_gain_input.text())
        restart_hackrf()
        reset_max_hold()
    except ValueError:
        print("Invalid LNA gain input.")
# Start HackRF process
process = None


# Create buttons
reset_button = QPushButton('Reset Max Hold')
reset_button.clicked.connect(reset_max_hold)

apply_gain_button = QPushButton('Apply Gain')
apply_gain_button.clicked.connect(apply_gain)

gain_input = QLineEdit()
gain_input.setText(str(gain))

apply_lna_gain_button = QPushButton('Apply LNA Gain')
apply_lna_gain_button.clicked.connect(apply_lna_gain)
lna_gain_input = QLineEdit()
lna_gain_input.setText(str(lna_gain))
# UI Setup
ui_widget = QWidget()
ui_layout = QVBoxLayout()
ui_layout.addWidget(QLabel("Enter VGA Gain:"))
ui_layout.addWidget(gain_input)
ui_layout.addWidget(apply_gain_button)
ui_layout.addWidget(QLabel("Enter LNA Gain:"))
ui_layout.addWidget(lna_gain_input)
ui_layout.addWidget(apply_lna_gain_button)
ui_layout.addWidget(reset_button)
ui_widget.setLayout(ui_layout)
ui_widget.setGeometry(900, 70, 100, 100)  
main_window.setMenuWidget(ui_widget)

main_layout.addWidget(win)
main_window.setCentralWidget(main_widget)
main_window.show()



try:
    # Initial process launch
    process = subprocess.Popen(
        ["hackrf_sweep", "-l", str(lna_gain), "-g", str(gain)],
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

    read_timer = QtCore.QTimer()
    read_timer.timeout.connect(read_data)
    read_timer.start(10)
    update_plot()
    app.exec_()

except Exception as e:
    print(f"Error: {e}")