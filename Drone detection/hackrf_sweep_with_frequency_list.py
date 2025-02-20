import numpy as np
import subprocess
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout, QMainWindow, QLineEdit, QLabel
import atexit
from pyqtgraph import ColorMap



# Define blue-red colormap
colors = [
    (0, (0, 0, 225)),
    (0.95, (255, 255, 0)),
    (0.97, (255, 0, 0)),
    (1, (255, 0, 0))
]

lna_gain = 32   # Intial lna gain
gain = 40       # Initial vga gain


# Initial configuration
freq_low = 0
freq_high = 6000

FREQ_BINS_PER_LINE = 5
total_lines = int(freq_high / FREQ_BINS_PER_LINE)
total_freq_bins = int(total_lines * FREQ_BINS_PER_LINE)
WATERFALL_DEPTH = 100


# Frequency dictionary
freq_dict = {
    1 : [300, 600],
    2 : [900, 1500],
    3 : [2000, 3000],
    4 : [4500, 5500],
    5 : [0, 6000]
}

# Global frequency button count
freq_button_count = 0


# Initial configuration
power_values = []
max_hold = None
waterfall_data = np.full((WATERFALL_DEPTH, total_freq_bins), -100)
frequencies = np.linspace(0, freq_high*1000000, total_freq_bins)


# PyQtGraph Setup
app = QApplication.instance()
if not app:
    app = QApplication([])

# Create Main window
main_window = QMainWindow()
main_widget = QWidget(main_window)
main_layout = QVBoxLayout(main_widget)


# Create the GraohicsLayoutWidget for the plots
win = pg.GraphicsLayoutWidget(show=True, title='HackRF Sweep with Waterfall plot')
win.resize(1000, 800)
win.setWindowTitle('HackRF Spectrum Sweep with Waterfall plot')
layout = win.addLayout()


# Top Plot: Spectrum
plot = layout.addPlot(title='Real-Time Spectrum with Max Hold')
plot.setLabel('bottom', 'Frequency (Hz)')
plot.setLabel('left', 'Power (dB)')
plot.setXRange(0, total_freq_bins*1000000)
plot.setYRange(-100, 0)

layout.nextRow()


# Curves
real_time_curve = plot.plot(pen='y')
max_hold_curve = plot.plot(pen='r')
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
        self.plot.setLabel('bottom', 'Frequency', units='Hz')
        self.plot.setLabel('left', 'Time')
        self.plot.setYRange(0, self.history_size)
        self.plot.setXRange(freq_low * 1e6, freq_high * 1e6)

        self.waterfall_img = pg.ImageItem()
        self.plot.addItem(self.waterfall_img)
        self.plot.invertY(True)

        # Scale the image in x-direction by a factor of 1/1000
        self.waterfall_img.setTransform(QtGui.QTransform().scale(1e6, 1))

    def update_plot(self, data):
        self.counter += 1
        # Update the image position to move downwards
        self.waterfall_img.setImage(data.T, autoLevels=False, lut=lut, levels=(0, 1))
        self.waterfall_img.setPos(freq_low * 1e6, 0)



waterfall_widget = WaterfallPlotWidget(layout)



# Process HackRF Sweep Output
def process_line(line):
    parts = line.strip().split(", ")
    try:
        values = list(map(float, parts[-FREQ_BINS_PER_LINE:]))
        return values if len(values) == FREQ_BINS_PER_LINE else []
    except ValueError:
        return []
    


def reset_max_hold():
    global max_hold
    max_hold = None
    max_hold_curve.setData(frequencies, np.full_like(frequencies, -200))


def start_hackrf():
    """Start the HackRF process"""
    global gain, lna_gain, process, freq_low, freq_high
    process = subprocess.Popen(
    ["hackrf_sweep", "-f", f"{freq_low}:{freq_high}", "-l", str(lna_gain), "-g", str(gain)],
    stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    )
    

def stop_hackrf():
    """ Stop the HackRF process """
    global process
    if process:
        process.terminate()

def restart_hackrf():
    """ Restart HackRF with new frequency settings and resume data reading """
    global process
    stop_hackrf()
    
    # Ensure process is fully terminated before restarting
    if process:
        process.wait()  # Wait for full termination

    start_hackrf()



def apply_gain():
    """ Apply new gain value and restart the HackRF process """
    global gain
    try:
        gain = int(gain_input.text())
        restart_hackrf()
        reset_max_hold()
    except ValueError:
        print('Invalid gain input')

def apply_lna_gain():
    """ Apply new lna gain value and restart the HackRF process """
    global lna_gain
    try:
        lna_gain = int(lna_gain_input.text())
        restart_hackrf()
        reset_max_hold()
    except ValueError:
        print('Invalid LNA gain input')


def set_frequency_range():
    """ Set new frequency range and restart HackRF """
    global freq_low, freq_high, total_freq_bins, frequencies, waterfall_data, power_values, total_lines, max_hold, process, freq_button_count

    if freq_button_count < len(freq_dict):
        freq_button_count += 1
        freq_low = freq_dict[freq_button_count][0]
        freq_high = freq_dict[freq_button_count][1]

        # Calculate total number of frequency bins based on new range
        total_lines = int((freq_high - freq_low) / FREQ_BINS_PER_LINE)
        total_freq_bins = int(total_lines * FREQ_BINS_PER_LINE)
        
        # Update frequency axis for plotting
        frequencies = np.linspace(freq_low * 1e6, freq_high * 1e6, total_freq_bins)

        # Reset waterfall data and power values to avoid display issues
        waterfall_data = np.full((WATERFALL_DEPTH, total_freq_bins), -100)
        power_values = []

        # Reset max_hold to reflect the new frequency range
        max_hold = np.full(total_freq_bins, -100)

        # Update the X-range of both the spectrum and waterfall plot
        plot.setXRange(freq_low * 1e6, freq_high * 1e6)
        waterfall_widget.plot.setXRange(freq_low * 1e6, freq_high * 1e6)

        # Update the Y-range of the waterfall plot to match the depth of the waterfall (time dimension)
        waterfall_widget.plot.setYRange(0, WATERFALL_DEPTH)

        plot.setTitle(f'Real-Time Spectrum: {freq_low} - {freq_high} MHz')

        print(f"Setting frequency range: {freq_low} MHz to {freq_high} MHz")

        restart_hackrf()  # Restart HackRF to begin capturing data in the new range
        reset_max_hold()  # Reset the max hold data

        # Force a redraw to ensure that the plot reflects the changes immediately
        app.processEvents()

    else:
        freq_button_count = 0


def update_plot():
    global power_values, max_hold, waterfall_data, frequencies

    if len(power_values) == total_freq_bins:
        if max_hold is None or len(max_hold) != total_freq_bins:
            # Reset max_hold if it doesn't match the expected size
            max_hold = np.full(total_freq_bins, -100)

        max_hold = np.maximum(max_hold, power_values)

        # Update the plot with frequencies in GHz
        real_time_curve.setData(frequencies, power_values)
        max_hold_curve.setData(frequencies, max_hold)

        # Update waterfall plot
        waterfall_data[1:, :] = waterfall_data[:-1, :]
        waterfall_data[0, :] = np.array(power_values)

        # Normalize the waterfall data for better visibility
        min_power, max_power = np.min(waterfall_data), np.max(waterfall_data)
        if max_power - min_power > 1e-3:  
            scaled_waterfall = (waterfall_data - min_power) / (max_power - min_power)
        else:
            scaled_waterfall = np.zeros_like(waterfall_data)  

        waterfall_widget.update_plot(scaled_waterfall)


        power_values.clear()





# Start HackRF process
process = None


# Create buttons
freq_range_button = QPushButton('Set Frequency Range')
freq_range_button.clicked.connect(set_frequency_range)


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

ui_layout.addWidget(freq_range_button)
ui_widget.setLayout(ui_layout)
ui_widget.setGeometry(900, 70, 100, 100)  
main_window.setMenuWidget(ui_widget)

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
                if lines_processed >= total_lines:
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