from teapot_body import Teapot_body
from spout import Spout
from GA.ga_flow import GeneticAlgorithmFlow
from GA.ga_volume import GeneticAlgorithmVolume
import random
from save import Save


class Teapot:
    def __init__(self, GA_spout_radius, GA_vol_radius):
        self.GA_spout_radius = GA_spout_radius
        self.GA_vol_radius = GA_vol_radius

        self.make_teapot(self.GA_spout_radius, self.GA_vol_radius)

    def make_teapot(self, radius_teapot, radius_spout):
        teapot_body = Teapot_body(radius_teapot, radius_spout)
        teapot_spout = Spout(0, -radius_teapot*0.8, -radius_teapot*0.3, radius_teapot, radius_spout)
    
    
class Journal:
    def __init__(self, GA_spout_radius, GA_vol_radius):
        self.GA_spout_radius = GA_spout_radius
        self.GA_vol_radius = GA_vol_radius

        self.teapot_journal(GA_spout_radius, GA_vol_radius)

    def teapot_journal(GA_spout_radius, GA_vol_radius):
        rand = str(random.randint(1, 10000))
        folder_location = "C:\\Users\\sfoss\\OneDrive - NTNU\\Skole\\Knowledge-based Engineering\\Assignments\\Assignment 3\\tmm4270_assignment3\\Generated Customer Models\\"
        file_name_model = "teapot_" + rand

        try:
            teapot_make = Teapot(GA_vol_radius, GA_spout_radius)
            save = Save(folder_location, file_name_model)
            save.initForNX()
        except ValueError:
            print('ERROR: Error making the teapot.')
            