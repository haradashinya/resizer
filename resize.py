#!/usr/bin/python
import PIL.Image
import os
import sys
from os.path import expanduser

# set input dir
target_dir = "/Desktop/"
home_dir = expanduser("~") + target_dir

# input the retina file path and output editted file.

def format_dir(path,ext):
    return home_dir + path +  ext


def resize(path):
    input_path = format_dir(path,".png")
    output_normal_path = format_dir(path,".png")
    output_retina_path = format_dir(path,"@2x.png")
    try:
        f = PIL.Image.open(input_path)
        f_normal = f.resize((int(f.size[0] * 0.5) , int(f.size[1] * 0.5)))
        f_normal.save(output_normal_path)
        f_retina = f.resize((int(f.size[0]),int(f.size[1])))
        f_retina.save(output_retina_path)
    except IOError:
        print "IO error. file %s doesn't exist." % input_path

if  len(sys.argv) == 2:
    resize(sys.argv[1])
else:
    raise "you can't file path as argument."



