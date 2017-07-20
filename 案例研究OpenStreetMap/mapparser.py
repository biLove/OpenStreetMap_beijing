import xml.etree.cElementTree as ET
import pprint

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
    return tag_num


def test():
    tags = count_tags('example.osm')
    pprint.pprint(tags)
    assert tags == {'bounds': 1,
                    'member': 3,
                    'nd': 4,
                    'node': 20,
                    'osm': 1,
                    'relation': 1,
                    'tag': 7,
                    'way': 1}


if __name__ == "__main__":
    test()


