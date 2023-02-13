def discibe_city(city, country= 'russia'):
	"""Выводит информацию о городе и стране"""
	print(f"{city.title()} is in {country.title()}.")

discibe_city('moskow')
discibe_city('new-york', 'usa')
discibe_city(city= 'paris',country= 'france')