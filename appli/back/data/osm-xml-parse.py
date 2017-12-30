import os, json, pymongo, sys
from lxml import etree

client = pymongo.MongoClient("mongodb://127.0.0.1:27017")
db = client['map_data']
collection = dn['roads']

class rue:
	nom = "no name"
	fonction = "no fonction"
	bicycle = "no bicycle"
	maxspeed = "no max speed"
	oneway = "none"
	points =[]

class node_object :
	lon = "lon"
	lat = "lat"
j = 0

way_array = []
tree = etree.parse(sys.argv[1])

#Creation of an warray with all of the map.osm way
for element in tree.xpath("way"):
	way = element
	for tag in way.xpath("tag"):
			road = tag.attrib

			if road["k"] == "highway":
				j +=1
				way_tmp = []

				for tag in way.xpath("tag"):
					name = tag.attrib

					if name["k"] == "name":
						way_tmp.append(name["v"])

					else:
						way_tmp.append("none")

					if name["k"] == "highway":
						way_tmp.append(road["v"])

					else:
						way_tmp.append("none")

					if name["k"] == "bicycle":
						way_tmp.append(road["v"])

					else:
						way_tmp.append("none")

					if name["k"] == "maxspeed":
						way_tmp.append(road["v"])

					else:
						way_tmp.append("none")

					if name["k"] == "oneway":
						way_tmp.append(road["v"])
						break

					else:
						way_tmp.append("none")
						break


				points = []

				for nd in way.xpath("nd"):
					nd_ref = nd.attrib["ref"]

					points.append(nd_ref)

				way_tmp.append(points)
				way_array.append(way_tmp)

print(j)

#Creation of a list with all the node from map.osm
node_array = {}

for node in tree.xpath("node"):
	node_tmp = node_object()
	node_tmp.lon = node.attrib["lon"]
	node_tmp.lat = node.attrib["lat"]

	#print(node_tmp.__dict__)
	node_array[node.attrib["id"]] = node_tmp

#print(node_array["34958227"])

i = 0

#Parse of the way elment an integration in a rue class
for element in way_array:
	tmp = rue()
	tmp.nom = element[0]
	tmp.fonction = element[1]
	tmp.bicycle = element[2]
	tmp.maxspeed = element[3]
	tmp.oneway = element[4]
	tmp.points = []

	for nd in element[5]:
		tmp.points.append([node_array[nd].lon, node_array[nd].lat])
	i += 1

	collection.insert(tmp.__dict__)

	test = rue()


map = open("map.json", "a")
map.write("{\"end\":\"true\"}]}")
map.close()
