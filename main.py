import xml.dom.minidom
import shutil
import os
import sys

var = sys.argv[1]

doc = xml.dom.minidom.parse(var)
path = doc.getElementsByTagName("file")

for count in range(len(path)):
    shutil.copy(os.path.join(path[count].getAttribute("source_path"), path[count].getAttribute("file_name")),
                path[count].getAttribute("destination_path"))

