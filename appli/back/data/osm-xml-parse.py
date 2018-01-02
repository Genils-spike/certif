import os, json, pymongo, sys
from lxml import etree

client = pymongo.MongoClient("mongodb://127.0.0.1:27017")
db = client['map_data']
collection = db['roads']

class rue:
	nom = "no name"
	fonction = "no fonction"
	bicycle = "no bicycle"
	maxspeed = "no max speed"
	oneway = "none"
	points = []

class node_object :
	lon = "lon"
	lat = "lat"

j = 0

way_array = []
tree = etree.parse(sys.argv[1])

#Creation of a list with all the node from map.osm
node_array = {}

for node in tree.xpath("node"):
	node_tmp = node_object()
	node_tmp.lon = node.attrib["lon"]
	node_tmp.lat = node.attrib["lat"]

	node_array[node.attrib["id"]] = node_tmp

#drop the old collection waiting for a better sorting of the new datas
collection.drop()

#creation of the road database enteries
for element in tree.xpath("way"):
	way = element

	for tag in way.xpath("tag"):
			road = tag.attrib

			if road["k"] == "highway":

				tmp = rue()
				tmp.nom = "none"
				tmp.fonction = "none"
				tmp.bicycle = "none"
				tmp.maxspeed = "none"
				tmp.oneway = "none"
				tmp.points = []
				j +=1
				way_tmp = []

				for tag in way.xpath("tag"):
					name = tag.attrib

					if name["k"] == "name":
						tmp.nom = name["v"]

					if name["k"] == "highway":
						tmp.fonction = road["v"]

					if name["k"] == "bicycle":
						tmp.bicycle = road["v"]

					if name["k"] == "maxspeed":
						tmp.maxspeed = road["v"]

					if name["k"] == "oneway":
						tmp.oneway = road["v"]
						break

				for nd in way.xpath("nd"):
					ref = nd.attrib["ref"]
					tmp.points.append([node_array[ref].lon, node_array[ref].lat])
			#insertion of road in the database
				collection.insert(tmp.__dict__)
				print(tmp.__dict__)
			tmp = rue()