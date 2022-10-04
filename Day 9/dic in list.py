import json
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
def add_new_country(country_visied, times_visited, cities_visited):
    new_country = {}
    new_country["country"] = country_visied
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited
    travel_log.append(new_country)          #since travel log is an "list"




add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(json.dumps(travel_log, indent=0))

