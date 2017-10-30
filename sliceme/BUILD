
py_library(
  name = "slicestl",
  srcs = ["slicestl/loader.py", "slicestl/viewer.py", "slicestl/util.py", "slicestl/slicer.py", "slicestl/__init__.py"],
)


py_binary(
  name = "runme",
  srcs = ["runme.py"],
  deps = [":slicestl"]
)

# vim:set ts=8 sts=2 sw=2 et:
