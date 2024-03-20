import json
import plotly.express as px

# load : file
# loads : str > dict, dict > str

#160
#mag, (lat, lon)
mag = []
lat = []
lon = []
with open("eq.geojson", "r", encoding="utf-8") as f:
    data = json.load(f)
    print(type(data), type(data["features"]), data["features"][0]) # type(data) - <class 'dict'>
    for feature in data["features"] :
        # print(feature["properties"]["mag"])
        mag.append(feature["properties"]["mag"]) #<class 'dict'> feature 안의 <class 'dict'> geometry 안의 coordinates 표현 : 키로 찾아들어가?
        lon.append(feature["geometry"]["coordinates"][0]) #무언가 안의 무언가를 찾아들어가는 표현 같다
        lat.append(feature["geometry"]["coordinates"][1])
    # print(data["features"][0]["properties"]["mag"])
    # print(data["features"][0]["geometry"]["coordinates"])
        
fig = px.scatter_geo(lat=lat, lon=lon, size=mag)
fig.show()