import requests

req = requests.get("https://swapi.dev/api/people/2/")
person = req.json()
print(person)
print(f"Name is \t\t\t{person['name']}")
print(f"Birth year is \t\t\t{person['birth_year']}")

print("Films involved in :")
for film in person['films']:
    req =requests.get(film)
    film = req.json()
    print("Film is : " ,film['title'])

# answers
# {'name': 'C-3PO', 'height': '167', 'mass': '75', 'hair_color': 'n/a', 'skin_color': 'gold', 'eye_color': 'yellow', 'birth_year': 
# '112BBY', 'gender': 'n/a', 'homeworld': 'https://swapi.dev/api/planets/1/', 'films': ['https://swapi.dev/api/films/1/', 'https://swapi.dev/api/films/2/', 'https://swapi.dev/api/films/3/', 'https://swapi.dev/api/films/4/', 'https://swapi.dev/api/films/5/', 'https://swapi.dev/api/films/6/'], 'species': ['https://swapi.dev/api/species/2/'], 'vehicles': [], 'starships': [], 'created': '2014-12-10T15:10:51.357000Z', 'edited': '2014-12-20T21:17:50.309000Z', 'url': 'https://swapi.dev/api/people/2/'}
# Name is                         C-3PO
# Birth year is                   112BBY
# Films involved in :
# Film is :  A New Hope
# Film is :  The Empire Strikes Back
# Film is :  Return of the Jedi
# Film is :  The Phantom Menace
# Film is :  Attack of the Clones
# Film is :  Revenge of the Sith

