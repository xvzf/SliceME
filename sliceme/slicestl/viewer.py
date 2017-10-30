#!/usr/bin/env python3

import os
import numpy as np
import stl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.lines as mlines

class Viewer(object):
    """Utility class for viewing STL Files using matplotlib or OpenGL"""

    def __init__(self):
        super(Viewer, self).__init__()


    def plot_mesh_intersection(self, mesh, points, hideaxis=True):
        """Simple view using matplotlib"""

        # Initialize Window
        figure = plt.figure("sliceme STL Viewer")
        axis = figure.add_subplot(1,2,1, projection='3d')
        # axis.set_autoscale_on(False)
        # axis.set_ylim(0,25)
        # axis.set_xlim(0,25)
        # axis.set_zlim(0,25)
        # if hideaxis:
        #     plt.axis('off')

        # Wireframe display
        for i in range(len(mesh.v0)):
            a = mesh.v0[i]
            b = mesh.v1[i]
            c = mesh.v2[i]
            axis.plot([a[0],b[0],c[0],a[0]],[a[1],b[1],c[1],a[1]],[a[2],b[2],c[2],a[2]])

        for p in points:
            axis.scatter(p[0], p[1], p[2], color="r")

        axis2 = figure.add_subplot(1,2,2)

        for p in points:
            axis2.scatter(p[0], p[1], color="r")

        # for i in len(points):
        #     axis2.add_line(mlines.Line2D([],[]))
        # xlist = []
        # ylist = []
        # for p in points:
        #     xlist.append(p[0])
        #     ylist.append(p[1])
        #
        # axis2.add_line(mlines.Line2D(xlist, ylist))

        if hideaxis:
            axis.axis('off')
            axis2.axis('off')

        plt.show()


    def plot_mesh(self, mesh):
        self.plot_mesh_intersection(mesh, [])



    def plot_2dlines(self, lines):
        for i in lines:
            plt.plot([i[0][0], i[1][0]], [i[0][1], i[1][1]], color="r")
            # print(i[0][0], i[0][1], i[1][0], i[1][1])

        plt.show()
