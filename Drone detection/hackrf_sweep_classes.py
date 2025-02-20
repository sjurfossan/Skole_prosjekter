import numpy as np
import subprocess
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout, QMainWindow, QLineEdit, QLabel
import atexit
from pyqtgraph import ColorMap


# Constants
FREQ_BINS_PER_LINE = 5
WATERFALL_DEPTH = 100

# Define blue-red colormap
colors = [
    (0, (0, 0, 225)),
    (0.95, (255, 255, 0)),
    (0.97, (255, 0, 0)),
    (1, (255, 0, 0))
]
color_map = pg.ColorMap(*zip(*colors))
lut = color_map.getLookupTable(start=0.0, stop=1.0, nPts=256)


class FrequencyManager:
    """Manages the available frequency ranges."""
    def __init__(self):
        self.freq_dict = {
            1: [300, 600],
            2: [900, 1500],
            3: [2000, 3000],
            4: [4500, 5500],
            5: [0, 6000]
        }
        self.index = 0
        self.counter = 0

    def next_range(self):
        self.counter += 1
        temp_freq_dict_val_low = self.freq_dict[self.counter][0]
        temp_freq_dict_val_high = self.freq_dict[self.counter][1]

        if not self.counter < len(self.freq_dict):
            self.counter = 0

        return temp_freq_dict_val_low, temp_freq_dict_val_high

        


class HackRFController:
    """Handles HackRF interaction."""
    def __init__(self):
        self.lna_gain = 32
        self.gain = 40
        self.process = None

        self.freq_low = 0
        self.freq_high = 6000

        self.total_lines = int((self.freq_high - self.freq_low) / FREQ_BINS_PER_LINE)
        self.total_freq_bins = int(self.total_lines * FREQ_BINS_PER_LINE)

    def start(self):
        self.stop()
        self.process = subprocess.Popen(
            ["hackrf_sweep", "-f", f"{self.freq_low}:{self.freq_high}", "-l", str(self.lna_gain), "-g", str(self.gain)],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )
    
    def stop(self):
        if self.process:
            self.process.terminate()
            self.process.wait()
            self.process = None
    
    def restart(self):
        self.start()

class SpectrumPlot:
    """Handles the real-time spectrum plot."""
    def __init__(self, layout, freq_low, freq_high):
        self.plot = layout.addPlot(title='Real-Time Spectrum with Max Hold')
        self.plot.setLabel('bottom', 'Frequency (Hz)')
        self.plot.setLabel('left', 'Power (dB)')
        self.plot.setXRange(freq_low * 1e6, freq_high * 1e6)
        self.plot.setYRange(-100, 0)
        
        self.real_time_curve = self.plot.plot(pen='y')
        self.max_hold_curve = self.plot.plot(pen='r')
        
    def update(self, frequencies, power_values, max_hold):
        self.real_time_curve.setData(frequencies, power_values)
        self.max_hold_curve.setData(frequencies, max_hold)

class WaterfallPlotWidget:
    """Handles the waterfall plot."""
    
    def __init__(self, layout, freq_low, freq_high):
        self.layout = layout
        self.history_size = WATERFALL_DEPTH
        self.counter = 0
        self.freq_low = freq_low
        self.freq_high = freq_high
        self.create_plot()

    def create_plot(self):
        self.plot = self.layout.addPlot()
        self.plot.setLabel('bottom', 'Frequency', units='Hz')
        self.plot.setLabel('left', 'Time')
        self.plot.setYRange(0, self.history_size)
        self.plot.setXRange(self.freq_low * 1e6, self.freq_high * 1e6)

        self.waterfall_img = pg.ImageItem()
        self.plot.addItem(self.waterfall_img)
        self.plot.invertY(True)

        # Scale the image in x-direction by a factor of 1/1000
        self.waterfall_img.setTransform(QtGui.QTransform().scale(1e6, 1))
    
    def update(self, data):
        self.counter += 1
        # Update the image position to move downwards
        self.waterfall_img.setImage(data.T, autoLevels=False, lut=lut, levels=(0, 1))
        self.waterfall_img.setPos(self.freq_low * 1e6, 0)

class MainWindow(QMainWindow):
    """Main application window."""
    def __init__(self):
        super().__init__()
        self.setWindowTitle('HackRF Spectrum Sweep')
        self.resize(1000, 800)

        self.freq_manager = FrequencyManager()
        self.hackrf = HackRFController()
        self.freq_low, self.freq_high = self.freq_manager.next_range()
        
        self.frequencies = np.linspace(self.freq_low * 1e6, self.freq_high * 1e6, 100)
        self.waterfall_data = np.full((WATERFALL_DEPTH, 100), -100)
        self.max_hold = np.full(100, -100)
        self.power_values = []

        self.layout = pg.GraphicsLayoutWidget()
        self.setCentralWidget(self.layout)

        self.spectrum_plot = SpectrumPlot(self.layout, self.freq_low, self.freq_high)
        self.layout.nextRow()
        self.waterfall_plot = WaterfallPlotWidget(self.layout, self.freq_low, self.freq_high)
        
        self.init_ui()
        self.hackrf.start()
        self.read_timer = QtCore.QTimer()
        self.read_timer.timeout.connect(self.read_data)
        self.read_timer.start(10)
        
    def init_ui(self):
        self.ui_widget = QWidget()
        self.ui_layout = QVBoxLayout()

        self.freq_button = QPushButton('Set Frequency Range')
        self.freq_button.clicked.connect(self.set_frequency_range)
        self.ui_layout.addWidget(self.freq_button)

        self.reset_button = QPushButton('Reset Max Hold')
        self.reset_button.clicked.connect(self.reset_max_hold)
        self.ui_layout.addWidget(self.reset_button)
        
        self.ui_widget.setLayout(self.ui_layout)
        self.setMenuWidget(self.ui_widget)

    def set_frequency_range(self):
        self.freq_low, self.freq_high = self.freq_manager.next_range()
        self.hackrf.restart(self.freq_low, self.freq_high)
        self.spectrum_plot.plot.setXRange(self.freq_low * 1e6, self.freq_high * 1e6)
        self.waterfall_plot.plot.setXRange(self.freq_low * 1e6, self.freq_high * 1e6)
        print(f"Setting frequency range: {self.freq_low} MHz to {self.freq_high} MHz")

    def reset_max_hold(self):
        self.max_hold.fill(-100)

    def read_data(self):
        if self.hackrf.process:
            line = self.hackrf.process.stdout.readline()
            if line.strip():
                self.power_values = np.random.uniform(-100, 0, 100)  # Simulating data
                self.max_hold = np.maximum(self.max_hold, self.power_values)
                self.waterfall_data[1:, :] = self.waterfall_data[:-1, :]
                self.waterfall_data[0, :] = self.power_values
                self.spectrum_plot.update(self.frequencies, self.power_values, self.max_hold)
                self.waterfall_plot.update(self.waterfall_data)

if __name__ == "__main__":
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    atexit.register(main_window.hackrf.stop)
    app.exec_()
