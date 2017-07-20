import xml.etree.cElementTree as ET

filename = 'sample.osm'

def is_street_name(elem):
    #return (elem.attrib['k'] == "addr:street")
    return (elem.attrib['k'] == "addr:city")


def is_post_code(elem):
    return (elem.attrib['k'] == 'addr:postcode')

for event, elem in ET.iterparse(filename, events=("start",)):

    if elem.tag == "node" or elem.tag == "way":
        for tag in elem.iter("tag"):
            if is_street_name(tag):
            #if is_post_code(tag):
                print tag.attrib['v']