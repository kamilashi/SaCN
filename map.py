import sys
import math
import data.locales as locales
import fDiscord

enum_ref_coords = [{"lat": 53.55278, "long": 10.00639}, # Hbh
                   {"lat": 53.552729, "long": 9.99339},  # Jung
                   {"lat": 53.55194, "long": 9.93500},  # Altona
                   {"lat": 53.5496, "long": 9.9845}   # Stadthausbrücke
                   ];

ratio = 1/0.220; #220 meters in 1 on map
R_EARTH = 6371.000

def toRadians(deg):
    return deg * math.pi/ 180;

def getDistance(lat1_deg, long1_deg,lat2_deg ,long2_deg):
    delta_lat_rad = toRadians(abs(lat2_deg - lat1_deg));
    delta_long_rad = toRadians(abs(long2_deg - long1_deg));
    lat_rad = toRadians(lat1_deg);
    lat2_rad = toRadians(lat2_deg);
    a = math.acos(
        math.sin(lat_rad) * math.sin(lat2_rad) + math.cos(lat_rad) * math.cos(lat2_rad) * math.cos(delta_long_rad));
    dist_m = R_EARTH * a;  # in metres
    return dist_m;

# input given in following order: lat long radius in cm
#
def main(lat1_deg, long1_deg, radius_cm):
    count = 0; # number of locations close to input coordinates within the given radius

    for i in range(0, len(enum_ref_coords)):
        lat2_deg = enum_ref_coords[i]["lat"];
        long2_deg = enum_ref_coords[i]["long"];
        distance_cm = getDistance(lat1_deg, long1_deg, lat2_deg, long2_deg) * ratio;
        if(distance_cm <= radius_cm):
            count+=1;
    return_message = "count = " + str(count);
    print(return_message);
    return return_message;




if __name__ == "__main__":
    main(sys.argv[1]);