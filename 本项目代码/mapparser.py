import xml.etree.cElementTree as ET
import pprint

filename = 'sample.osm'

def count_tags(filename):
    tag_num = {}

    tree = ET.ElementTree(file= filename)
    root = tree.getroot()
    #print root.tag,root.attrib

    for elem in tree.iter():
        get_tag =  elem.tag
        if get_tag in tag_num:
            tag_num[get_tag] += 1
        else:
            tag_num[get_tag] = 1

    print tag_num

count_tags(filename)






