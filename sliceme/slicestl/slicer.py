#!/usr/bin/env python3

import numpy as np
import cv2
import sys


class Slicer(object):

    # Placeholder so that YCML autocompletes them!
    x_min           = None
    y_min           = None
    z_min           = None
    x_max           = None
    y_max           = None
    z_max           = None
    num_vertices    = None
    vertices        = None
    normals         = None


    def __init__(self, vertices, num_vertices, normals, dimensions):
        """Init"""

        # Update dimensions
        self.x_min, self.y_min, self.z_min, self.x_max, self.y_max, self.z_max = dimensions

        self.vertices = vertices
        self.normals = normals
        self.num_vertices = num_vertices


    def get_vertice_interacting(self, zplane_offset):
        """Returns all vertices which interact with a plane with normal vector [0,0,1] and offset zplane_offset)"""

        ret_buf = []

        def helper(v):
            z0 = v[0][2]
            z1 = v[1][2]
            z2 = v[2][2]

            if z0 > zplane_offset and z1 > zplane_offset and z2 > zplane_offset:
                return 0
            if z0 < zplane_offset and z1 < zplane_offset and z2 < zplane_offset:
                return 0
            return v


        for vertex in self.vertices:
            v = helper(vertex)

            # Just a dirty workaround
            if type(v) is not int:
                ret_buf.append(v)

        return ret_buf


    def distance(self, z, point):
        """Computes distance of point to a plane with offset z"""
        # Normal vector is [0,0,1]
        return np.dot(point, np.array([0,0,1])) - z

    # @TODO
    def compute_vertex_intersection(self, z, vertex):
        """Computes intersection of a vertex """

        linepairs = [0,1, 1,2, 2,0]

        intersections = []

        for i in range(3):
            a = vertex[ linepairs[i*2 + 0] ]
            b = vertex[ linepairs[i*2 + 1] ]

            dst_a = self.distance(z, a)
            dst_b = self.distance(z, b)

            if dst_a * dst_b < 0:
                # Calculate scaling factor
                scl = dst_a / (dst_a - dst_b)
                intersections.append( a + (b-a) * scl )

            # Triangle vertex on plane
            elif dst_a == 0:
                if len(intersections) < 2:
                    intersections.append(a)

            # Triangle vertex on plane
            elif dst_b == 0:
                if len(intersections) < 2:
                    intersections.append(b)

            elif len(intersections) == 2:
                break

        return {"line": intersections,
                "vertex": vertex}


    def compute_intersection(self, z):

        print("[+] STLSlicer -> Slicing at height {:.2f}mm complete".format(z))

        tmp_buf = []

        for i in self.get_vertice_interacting(z):
            tmp_buf.append(self.compute_vertex_intersection(z,i))

        return tmp_buf
