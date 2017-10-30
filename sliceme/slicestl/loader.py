#!/usr/bin/env python

import os
import numpy as np
import stl

class Loader(object):
    """Utility class for loading STL Files in ASCII and binary format"""

    loaded = False


    def __init__(self):
        """Init"""
        super(Loader, self).__init__()


    def load_file(self, filename):
        """Loads STL File in ASCII or binary format"""
        self.mesh = stl.mesh.Mesh.from_file(filename)
        self.loaded_vertices = len(self.mesh.v0)
        print("[+] STLLoader -> Loaded {0!s} vertices".format(self.loaded_vertices))

        if self.mesh:
            self.loaded = True


    def get_vertices(self):
        """Returns a tuple containing all vertices in form (v0,v1,v2)"""

        ret_buf = []

        if self.loaded:
            for i in range(self.loaded_vertices):
                ret_buf.append(self.get_vertex(i))

        return np.array(ret_buf)


    def get_vertex(self, index):
        """Returns a list containing the vertex at a given index"""
        if self.loaded and index < self.loaded_vertices:
            return [self.mesh.v0[index], self.mesh.v1[index], self.mesh.v2[index]]


    def get_normals(self):
        """Returns all normals as array"""
        if self.loaded:
            return self.mesh.normals


    def get_normal(self, index):
        """Returns normal vector for a given index"""
        if self.loaded and index < self.loaded_vertices:
            return self.mesh.normals[index]


    def get_mesh(self):
        """Returns mesh"""
        return self.mesh
