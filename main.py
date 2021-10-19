import xml.dom.minidom
import shutil
import os
import sys

def copy(var):
    doc = xml.dom.minidom.parse(var)
    file = doc.getElementsByTagName("file")

    for count in range(len(file)):
        shutil.copy(os.path.join(file[count].getAttribute("source_path"), file[count].getAttribute("file_name")),
                    file[count].getAttribute("destination_path"))

if __name == '__main__':
    copy(sys.argv[1])
