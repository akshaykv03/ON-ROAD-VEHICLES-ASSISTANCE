


from geopy.distance import geodesic

def calculate_distance(lat1, lon1, lat2, lon2):
    # Coordinates of the two locations
    location1 = (lat1, lon1)
    location2 = (lat2, lon2)
    
    # Calculate the distance between them
    distance = geodesic(location1, location2).kilometers
    return distance


def estimate_travel_time(distance, speed=30):  # Speed in km/h
    # Time = distance / speed
    # Convert time to minutes: time * 60
    time_minutes = (distance / speed) * 60
    return time_minutes


def travel_info(clat,clon,alat,alon):
    lat1 = float(clat)
    lon1 = float(clon)
    lat2 = float(alat)
    lon2 = float(alon)
    
    distance = calculate_distance(lat1, lon1, lat2, lon2)
    time_taken = estimate_travel_time(distance)
    distance = f"{distance:.2f} km"
    time = f"{time_taken:.2f} minutes"
    return distance, time
