def fall_distance(time):

    "Calculates the distance an object falls due to gravity in a given time. Time = the seconds the object has been falling. return = the distance in meters the object has fallen"

    g = 9.8 

    "Assuming we're using Earth's gravity."

    d = (1/2) * g * (time**2)
    return d 