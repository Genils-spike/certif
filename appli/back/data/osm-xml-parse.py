import os
from lxml import etree

tree = etree.parse("map.osm")

for element in tree.xpath("way"):
	way = element

	for tag in way.xpath("tag"):
		attrib = tag.attrib
		print(attrib)
