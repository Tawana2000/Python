#write a funtion to filter a list of dictionaries based on star rating

def filter_by_star_rating(hotels, min_star):

    filtered_hotels = [hotel for hotel in hotels if hotel.get('stars', 0) >= min_star]
    return filtered_hotels


hotels = [
    {'name': 'Hotel1', 'stars': 3},
    {'name': 'Hotel2', 'stars': 4},
    {'name': 'Hotel3', 'stars': 5}
]

min_star = 4
print(filter_by_star_rating(hotels, min_star))