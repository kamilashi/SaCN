import sys
import math

import numpy as np
from PIL import Image
import data.locales as locales
import fDiscord
import plotly.graph_objects as go

enum_locations = [{"lat": 53.552778, "long": 10.006389, "riddlePiece": "Сквозь время, через километры"}, # Hbh
                   {"lat": 53.553611, "long": 9.9925, "riddlePiece": "В тяжелый день на пять минут"},  # Jungfernstieg
                    {"lat": 53.549167, "long": 9.986389, "riddlePiece": "Поймаешь и пробросишь бегло"},  # Stadthausbrücke
                    {"lat": 53.546111, "long": 9.966667, "riddlePiece": "Как хочешь время повернуть"},  # Landungsbrücken
                    {"lat": 53.549444, "long": 9.955833, "riddlePiece": "Вперед, где больше ждать не надо"},  # Reeperbahn
                    {"lat": 53.548333, "long": 9.945556, "riddlePiece": "Где все еще минут на пять"},  # Königstraße
                    {"lat": 53.551944, "long": 9.935, "riddlePiece": "Поймав его, мы будем рады\nО наших буднях рассказать."},  # Altona
                   ];
point_data = [{"lat":"lat", "long":"long", "radius":"radius"}];
points = [];
# enum_riddle_pieces = ["Сквозь время, через километры",
#                      "В тяжелый день на пять минут",
#                      "Поймаешь и пробросишь бегло",
#                     "Как хочешь время повернуть",
#                      "Вперед, где больше ждать не надо",
#                     "Где все еще минут на пять",
#                     "Поймав его, мы будем рады ",
#                     "О наших буднях рассказать."];

ratio = 1/0.220; #220 meters in 1 cm on map
R_EARTH = 6371.000
img_width = 1024;
img_height = 1024;

top_bound = 53.75; #
bottom_bound = 53.36666; #
right_bound = 10.35
left_bound = 9.7;

center_coords = [53.551086,9.993682]

allowableError = 0.5;


def toRadians(deg):
    return deg * math.pi/ 180;

def drawDot(lat1_deg, long1_deg, savepath):


    y = (abs(lat1_deg - bottom_bound) /abs(top_bound - bottom_bound) )*img_height
    x = (abs(long1_deg - left_bound)/ abs(right_bound - left_bound))*img_width

    print(" x = " + str(x) + "\n" + " y = " + str(y))


    try:  # try opening existing file
        with Image.open(savepath) as img:
            data = img.load()
        data[int(x), int(y)] = (255, 255, 255)  # Mark the point
    except Exception:  # create new if not exists
        print("created new image ")
    # Create a 1024x1024x3 array of 8 bit unsigned integers
        data = np.zeros((img_width, img_height, 3), dtype=np.uint8)
        data[int(x), int(y)] = [255, 255, 255]  # Mark the point
        img = Image.fromarray(data);
    img.save(savepath)
    img.close()

def plotAllPoints():
    mapbox_access_token = "pk.eyJ1Ijoia2FtaWxhc2hpIiwiYSI6ImNsaDY3ZDY3ejAzY3YzYm10dGgwazJmaWoifQ.DWDmOzff2A7wlkxankGMxQ"
    allLats = []
    allLongs = []
    for i in range(0, len(enum_locations)):
        allLats.append(enum_locations[i]["lat"]);
        allLongs.append(enum_locations[i]["long"]);
    fig = go.Figure(go.Scattermapbox(
        lat=allLats,
        lon=allLongs,
        mode='markers',
        marker=go.scattermapbox.Marker(
            size=10
        ),
        text=[''],
    ))

    fig.update_layout(
        autosize=True,
        uirevision=True,
        hovermode='closest',
        mapbox=dict(
            accesstoken=mapbox_access_token,
            bearing=0,
            center=dict(
                lat=center_coords[0],
                lon=center_coords[1]
            ),
            pitch=0,
            zoom=12  # 10 meters per pixel
        ),
    )

def plotPoint(lat1_deg, long1_deg, rad):

    mapbox_access_token  = "pk.eyJ1Ijoia2FtaWxhc2hpIiwiYSI6ImNsaDY3ZDY3ejAzY3YzYm10dGgwazJmaWoifQ.DWDmOzff2A7wlkxankGMxQ"
    fig = go.Figure(go.Scattermapbox(
        lat=[str(lat1_deg)],
        lon=[str(long1_deg)],
        mode='markers',
        marker=go.scattermapbox.Marker(
            size= rad * 22 * 2,
            opacity = 0.3
        ),
        text=[''],
    ))

    fig.update_layout(
        autosize=True,
        uirevision = True,
        hovermode='closest',
        mapbox=dict(
            accesstoken=mapbox_access_token,
            bearing=0,
            center=dict(
                lat=center_coords[0],
                lon=center_coords[1]
            ),
            pitch=0,
            zoom=12 # 10 meters per pixel
        ),
    )

    fig.show()

def plotPointDebug(lat1_deg, long1_deg, rad):
    allLats = [str(lat1_deg)]
    allLongs = [str(long1_deg)]
    sizes = [rad * 22 * 2]
    mapbox_access_token  = "pk.eyJ1Ijoia2FtaWxhc2hpIiwiYSI6ImNsaDY3ZDY3ejAzY3YzYm10dGgwazJmaWoifQ.DWDmOzff2A7wlkxankGMxQ"
    for i in range(0, len(enum_locations)):
        allLats.append(str(enum_locations[i]["lat"]));
        allLongs.append(str(enum_locations[i]["long"]));
        sizes.append(10)

    fig = go.Figure(go.Scattermapbox(
        lat=allLats,
        lon=allLongs,
        mode='markers',
        marker=go.scattermapbox.Marker(
            size= sizes
        ),
        text=[''],
    ))

    fig.update_layout(
        autosize=True,
        uirevision = True,
        hovermode='closest',
        mapbox=dict(
            accesstoken=mapbox_access_token,
            bearing=0,
            center=dict(
                lat=center_coords[0],
                lon=center_coords[1]
            ),
            pitch=0,
            zoom=12 # 10 meters per pixel
        ),
    )

    fig.show()

def drawAllPoints(img_path):
    for i in range(0, len(enum_locations)):
        lat_deg = enum_locations[i]["lat"];
        long_deg = enum_locations[i]["long"];
        drawDot(lat_deg,long_deg, img_path)

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
def main(lat1_deg, long1_deg, radius_cm):
    count = 0; # number of locations close to input coordinates within the given radius
    hit = False;
    return_message = "";
    riddle_piece = "";

    #plotPoint(lat1_deg, long1_deg, radius_cm)

    for i in range(0, len(enum_locations)):
        lat2_deg = enum_locations[i]["lat"];
        long2_deg = enum_locations[i]["long"];
        distance_cm = getDistance(lat1_deg, long1_deg, lat2_deg, long2_deg) * ratio;
        if(distance_cm <= allowableError): #if the spot was quessed
            hit = True;
            riddle_piece +=  fDiscord.italic(enum_locations[i]["riddlePiece"]);
            return_message += "[1], ";
            count -= 1;
        if(distance_cm <= radius_cm+allowableError):
            count+=1;
    return_message += str(count); # number of points within the tested radius, excluding the found one if such exists
    return_message += "\n\n" + riddle_piece;

    print(return_message);
    return [return_message, hit];




if __name__ == "__main__":
    main(sys.argv[1]);