#!/usr/bin/env python3

import slicestl
import numpy as np

zoffset = 12

if __name__=="__main__":

    # stl = slicestl.Util("testfiles/25mm_cube.stl")
    # stl = slicestl.Util("testfiles/turning_knob.stl")
    stl = slicestl.Util("testfiles/3DBenchy.stl")
    # stl = slicestl.Util("testfiles/test02.stl")

    # slicestl.Viewer().plot_mesh(stl.get_mesh())


    inarray = stl.get_intersection(zoffset)

    obj_lines = []

    for i in inarray:
        obj_lines.append(i["line"])

    slicestl.Viewer().plot_2dlines(obj_lines)
