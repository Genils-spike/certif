import os
import json
from lxml import etree

class rue:
	nom = "no name"
	fonction = "no fonction"
	bicycle = "no bicycle"
	maxspeed = "no max speed"
	oneway = "none"
	points =[]

i = 0
tree = etree.parse("map.osm")

for element in tree.xpath("way"):
	way = element

	for tag in way.xpath("tag"):
		road = tag.attrib

		if road["k"] == "highway":
			test = rue()
			i = i+1

			for tag in way.xpath("tag"):
				name = tag.attrib

				if name["k"] == "name":
					test.nom = name["v"]

				if name["k"] == "highway":
					test.fonction = road["v"]

				if name["k"] == "bicycle":
					test.bicycle = road["v"]

				if name["k"] == "maxspeed":
					test.maxspeed = road["v"]

				if name["k"] == "oneway":
					test.oneway = road["v"]

			test.points = []
			for nd in way.xpath("nd"):
				nd_ref = nd.attrib["ref"]
				for node in tree.xpath("node"):
					if node.attrib["id"] == nd_ref:
						test.points.append([node.attrib["lon"],node.attrib["lat"]])

	print(test.nom)
	print(test.fonction)
	print(test.bicycle)
	print(test.maxspeed)
	print(test.oneway)
	print(test.points)
	print(json.dump(test, indent=4, io))
print(i)
