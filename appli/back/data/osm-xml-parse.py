import os
from lxml import etree

tree = etree.parse("map.osm")

brut = tree.findall('way')

for way in brut:
	tag = way.findall('tag').text
	print(tag)

#je sais pas faire de commentaire en python donc tu l'enlèveras comme un grand, je t'aime fort et je suis sûre que tu vas t'en sortir avec ton script tout pourri parce que tu es le meilleur. Plein de love sur ton bon boule <3<3<3