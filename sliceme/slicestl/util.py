#!/usr/bin/env python3

from . import Loader
from . import Slicer
import numpy as np

# @TODO Add offset correction
class Util(Loader):

    # Placeholder so that YCML autocompletes them \*/
    x_min = None
    y_min = None
    z_min = None
    x_max = None
    y_max = None
    z_max = None
    slicer = None

    def __init__(self, filename):
        """Init"""
        super(Util, self).__init__()
        self.load_file(filename)

        # Update basic parameters
        if self.loaded:
            self.calc_dimensions()
            self.slicer = Slicer(self.get_vertices(), self.loaded_vertices, \
                                 self.get_normals(), self.get_dimensions())

        # Debug
        # print(self.get_dimensions())


    def calc_dimensions(self):
        """Calculates dimeonsions of the mesh """

        self.x_min = np.float32("inf")
        self.y_min = np.float32("inf")
        self.z_min = np.float32("inf")
        self.x_max = 0
        self.y_max = 0
        self.z_max = 0

        for v in self.get_vertices():
            for i in v:
                if i[0] < self.x_min:
                    self.x_min = i[0]

                if i[1] < self.y_min:
                    self.y_min = i[1]

                if i[2] < self.z_min:
                    self.z_min = i[2]

                if i[0] > self.x_max:
                    self.x_max = i[0]

                if i[1] > self.y_max:
                    self.y_max = i[1]

                if i[2] > self.z_max:
                    self.z_max = i[2]

        print("Dimensions: x ${} y ${} z ${}]".format( self.x_max-self.x_min, \
                                                                self.y_max-self.y_min, \
                                                                self.z_max-self.z_min))

    def get_dimensions(self):
        """Returns dimensions of the mesh in form ([xyz]_min, [xyz]_max)"""
        return (self.x_min, self.y_min, self.z_min, \
                self.x_max, self.y_max, self.z_max)

    def get_intersection(self, zoffset):
        return self.slicer.compute_intersection(zoffset)

