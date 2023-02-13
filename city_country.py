def city_country(city, country):
	cit_countr = f"{city}, {country}"
	return(cit_countr.title())

east = city_country('moskow', 'russia')
north = city_country('ottava', 'canada')
sounth = city_country('ierusalime', 'izraile')

print(east)
print(north)
print(sounth)