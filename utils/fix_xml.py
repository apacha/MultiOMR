#!/home/alex/anaconda/bin/python

from music21 import *
import lxml.etree as ET
import os, sys
from subprocess import call
from tempfile import (mkstemp, NamedTemporaryFile)

fn = sys.argv[1]

fh = open(fn, "r")
tree = ET.parse(fh)

for element in tree.iter(tag=ET.Element):
    if element.tag == "bar-style" and element.text == None:
        element.text = "regular"
    if element.tag == "beats" and element.text == "null":
        element.text = "4"
    if element.tag == "beat-type" and element.text == "null":
        element.text = "4"

print ET.tostring(tree)
