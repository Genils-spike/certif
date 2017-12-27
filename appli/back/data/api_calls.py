import pymongo, json, requests, sys, time

client = pymongo.MongoClient("mongodb://127.0.0.1:27017")
db= client[sys.argv[1]]
collection =  db[sys.argv[2]]

if sys.argv[1] == "road_works":
	if sys.argv[2] == "rennes_metropole":
		api_url = "http://travaux.data.rennesmetropole.fr/api/roadworks"
		api = requests.get(api_url).json()

		#drop the old collection
		collection.drop()

		class road_works :
			works_id = 0

		for events in api["features"]:
			tmp = road_works()
			properties = events["properties"]

			#creation of the road_works database enteries		
			
			tmp.works_id = properties["id"]
			tmp.insert_date_hour = time.localtime()
			tmp.city = properties["commune"]
			tmp.location = properties["quartier"]
			tmp.adress = properties["localisation"]
			tmp.begin_date = properties["date_deb"]
			tmp.ending_date = properties['date_fin']
			tmp.works_type = properties["type"]
			tmp.works_name = properties["libelle"]
			tmp.works_level = properties["niv_perturbation"]
			tmp.works_location = events["geometry"]

			#insertion of road works in the database

			collection.insert(tmp.__dict__)
			print(tmp.__dict__)

if sys.argv[1] == "bus_lines":
	if sys.argv[2] == "rennes_metropole":
		api_url = "https://data.explore.star.fr/api/records/1.0/search/?dataset=tco-bus-topologie-lignes-td&rows=350&facet=nomfamillecommerciale"
		api = requests.get(api_url).json()

		collection.drop()

		class bus_lines :
			bus_id = 0

		for lines in api["records"]:
			properties = lines["fields"]
			tmp = bus_lines()

			tmp.bus_id = lines["recordid"]
			tmp.bus_text = properties["couleurtexteligne"]
			tmp.bus_name = properties["nomlong"]
			tmp.bus_short_name = properties["nomcourt"]


			collection.insert(tmp.__dict__)
			