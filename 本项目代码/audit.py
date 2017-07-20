#!/usr/bin/python
# -*- coding: UTF-8 -*-

import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint

OSMFILE = "sample.osm"
street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)


expected = ["Street", "Avenue", "Boulevard", "Drive", "Court", "Place", "Square", "Lane", "Road",
            "Trail", "Parkway", "Commons"]

# UPDATE THIS VARIABLE
mapping = { "St": "Street",
            "St.": "Street",
            "Ave": "Avenue",
            "Rd.": "Road",
            }


def audit_street_type(street_types, street_name):
    m = street_type_re.search(street_name)
    if m:
        street_type = m.group()
        if street_type not in expected:
            street_types[street_type].add(street_name)


def is_street_name(elem):
    return (elem.attrib['k'] == "addr:street")


def audit(osmfile):
    osm_file = open(osmfile, "r")
    street_types = defaultdict(set)
    for event, elem in ET.iterparse(osm_file, events=("start",)):

        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_street_name(tag):
                    #print tag.attrib['v']
                    audit_street_type(street_types, tag.attrib['v'])
    osm_file.close()
    #print street_types
    return street_types


def update_name(name, mapping):

    # YOUR CODE HERE
    name_tmp = name.split(" ")
    name_old = name_tmp[len(name_tmp) - 1]
    if name_old in mapping:
        name_new = mapping[name_old]
        name_tmp[len(name_tmp) - 1] = name_new
    name = ' '.join(name_tmp)

    return name


def test():
    st_types = audit(OSMFILE)
    #assert len(st_types) == 3
    pprint.pprint(dict(st_types))

    for st_type, ways in st_types.iteritems():
        for name in ways:
            better_name = update_name(name, mapping)
            print name, "=>", better_name
            if name == "West Lexington St.":
                assert better_name == "West Lexington Street"
            if name == "Baldwin Rd.":
                assert better_name == "Baldwin Road"


if __name__ == '__main__':
    test()