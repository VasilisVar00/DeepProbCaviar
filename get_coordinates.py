# we need information for the coordinates and the orientation of entities
# at first we take this terms with absolute confidence i.e with prob = 1
# i assume that (in the future) this coordinates will be given by a pretrained 
# computer vision neural network

import xml.etree.ElementTree as ET
# 'wk1gt.xml'

# function that finds coordinates and orientation inside the .xml file
# it returns a list of dictionaries, one for each frame

def transform_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    acc = []

    for child in root:
        d = dict()
        d['frame'] = child.attrib["number"]
        l = []
        for child2 in child[0]:
            d2 = dict()
            d2['id'] = child2.attrib["id"]
            for child3 in child2:
                if(child3.tag == "orientation" or child3.tag == "box"):
                    if(child3.tag == "orientation"):
                            d2["orientation"] = child3.text
                    elif(child3.tag == "box"):
                            d2["box"] = child3.attrib
            l.append(d2)
        d['list'] = l
        acc.append(d)
    return acc

# print(transform_xml('wk1gt.xml'))
video = '01-Walk1'

# take the list of dictionaries returned from the above function
# to format the holdsAt predicates

def get_coordinates(filename):
    dicts = transform_xml(filename)
    for d1 in dicts:
        timeframe = int(d1["frame"]) * 40
        for d2 in d1['list']:
            print("holdsAt('{0}', coord(id{1}) = ({2},{3}), {4})".format(video,d2["id"],d2["box"]["xc"],d2["box"]["yc"],timeframe))
            print("holdsAt('{0}', orientation(id{1}) = {2}, {3})".format(video,d2["id"],d2["orientation"],timeframe))


    


