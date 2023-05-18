import json
# '''   used means it is a string not json right now 
c3p0 = '''{
	"name": "C-3PO",
	"height": "167",
	"mass": "75",
	"hair_color": "n/a",
	"skin_color": "gold",
	"eye_color": "yellow",
	"birth_year": "112BBY",
	"gender": "n/a",
	"homeworld": "http://swapi.dev/api/planets/1/",
	"films": [
		"http://swapi.dev/api/films/1/",
		"http://swapi.dev/api/films/2/",
		"http://swapi.dev/api/films/3/",
		"http://swapi.dev/api/films/4/",
		"http://swapi.dev/api/films/5/",
		"http://swapi.dev/api/films/6/"
	],
	"species": [
		"http://swapi.dev/api/species/2/"
	],
	"vehicles": [],
	"starships": [],
	"created": "2014-12-10T15:10:51.357000Z",
	"edited": "2014-12-20T21:17:50.309000Z",
	"url": "http://swapi.dev/api/people/2/"
}'''
c3p0 = json.loads(c3p0)     
# we took string an dsaid convert it to proper dictionary sing loads and then we change the name 

c3p0['name'] = "Kane Ezki"      
#^ this will do only in dictionary as after json.loads ,if you check its type it shows the dictionary and we need to convert it back and hence using  json.dumps()
c3p0_str = json.dumps(c3p0)
# now we dump that data back in string 
print(c3p0_str)

# {"name": "Kane Ezki", "height": "167", "mass": "75", "hair_color": "n/a", "skin_color": "gold", "eye_color": "yellow", "birth_year": "112BBY", "gender": "n/a", "homeworld": "http://swapi.dev/api/planets/1/", "films": ["http://swapi.dev/api/films/1/", "http://swapi.dev/api/films/2/", "http://swapi.dev/api/films/3/", "http://swapi.dev/api/films/4/", "http://swapi.dev/api/films/5/", "http://swapi.dev/api/films/6/"], "species": ["http://swapi.dev/api/species/2/"], "vehicles": [], "starships": [], "created": "2014-12-10T15:10:51.357000Z", "edited": "2014-12-20T21:17:50.309000Z", "url": "http://swapi.dev/api/people/2/"}