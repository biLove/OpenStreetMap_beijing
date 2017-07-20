#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.cElementTree as ET
import re



lower = re.compile(r'^([a-z]|_)*$')   #全部小写
lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')   #有冒号"："
problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')    #有特殊字符属于问题标钱类型


def key_type(element, keys):
    if element.tag == "tag":
        k_attrib = element.attrib["k"]
        if lower.match(k_attrib) is not None:
            keys["lower"] += 1
        elif lower_colon.match(k_attrib) is not None:
            keys["lower_colon"] += 1
        elif problemchars.search(k_attrib) is not None:
            keys["problemchars"] += 1
            print k_attrib
            temp_attrib = k_attrib.split(" ")
            k_attrib_new = "_".join(temp_attrib)
            print k_attrib_new
        else:
            keys["other"] += 1

    return keys


def process_map(filename):
    keys = {"lower": 0, "lower_colon": 0, "problemchars": 0, "other": 0}
    for _, element in ET.iterparse(filename):
        keys = key_type(element, keys)

    return keys


if __name__ == "__main__":
    key = process_map("sample.osm")
    print key