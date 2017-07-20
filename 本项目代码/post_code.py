import xml.etree.cElementTree as ET

filename = 'sample.osm'

def is_post_code(elem):
    return (elem.attrib['k'] == 'addr:postcode')

for event, elem in ET.iterparse(filename, events=("start",)):

    if elem.tag == "node" or elem.tag == "way":
        for tag in elem.iter("tag"):
            if is_post_code(tag):
                post_code = tag.attrib['v']
                if len(str(post_code)) != 6:
                    print post_code