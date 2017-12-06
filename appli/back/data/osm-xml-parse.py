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

j = 0
node_array = []
way_array = []
tree = etree.parse("map.osm")

#Creation of an warray with all of the map.osm way
for element in tree.xpath("way"):
	wayfu = element
	for tag in wayfu.xpath("tag"):
			road = tag.attrib

			if road["k"] == "highway":
				j +=1
				way = []

				for tag in wayfu.xpath("tag"):
					name = tag.attrib

					if name["k"] == "name":
						way.append(name["v"])

					else:
						way.append("none")

					if name["k"] == "highway":
						way.append(road["v"])

					else:
						way.append("none")

					if name["k"] == "bicycle":
						way.append(road["v"])

					else:
						way.append("none")
						
					if name["k"] == "maxspeed":
						way.append(road["v"])

					else:
						way.append("none")
						
					if name["k"] == "oneway":
						way.append(road["v"])
						break

					else:
						way.append("none")
						break


				points = []

				for nd in wayfu.xpath("nd"):
					nd_ref = nd.attrib["ref"]

					points.append(nd_ref)

				way.append(points)
				way_array.append(way)

print(j)

#Creation of a list with all the node from map.osm
for node in tree.xpath("node"):
	node_array.append([node.attrib["id"], node.attrib["lon"], node.attrib["lat"]])

i = 0
map = open("map.json", "w")

map.write("{\"point\":[")
map.close()

#Parse of the way elment an integration in a rue class
for element in way_array:
	test = rue()
	test.nom = element[0]
	test.fonction = element[1]
	test.bicycle = element[2]
	test.maxspeed = element[3]
	test.oneway = element[4]
	test.points = []

	for nd in element[5]:
		coord_list = [t for t in node_array if nd in t[0]]

		test.points.append([coord_list[0][1], coord_list[0][2]])
	i+=1

	with open('map.json', 'a') as f:
		json.dump(test.__dict__, f)
		f.write(",")
	print(i,"/",j)
	test = rue()


map = open("map.json", "a")
map.write("{\"end\":\"true\"}]}")
map.close()