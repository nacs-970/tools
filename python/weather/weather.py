# Note : lear about api & json
# Scr : https://www.youtube.com/watch?v=9P5MY_2i7K8
import datetime as dt
import requests as req

# Geo API : 
city = input(str("Enter a city: "))
g_url = "https://geocoding-api.open-meteo.com/v1/search?"
g_url = g_url + "name=" + city
g_resp = req.get(g_url).json()
g_lat = g_resp['results'][0]['latitude'] # need to have [0]  = list of dict
g_long = g_resp['results'][0]['longitude']
#print (f"lat : {g_lat}, long : {g_long}")

# Weather API : https://open-meteo.com/ 
w_url = "https://api.open-meteo.com/v1/forecast?"
w_url = w_url + "latitude=" + str(g_lat) + "&longitude=" + str(g_long) + "&daily=sunrise,sunset&current_weather=true&timezone=Asia%2FBangkok"
w_resp  = req.get(w_url).json()
#print(w_resp)
#print("------------------------------------------------")

# List out put
time = w_resp['current_weather']['time']
time_z = w_resp['timezone_abbreviation']
temp = w_resp['current_weather']['temperature']
wind_s = w_resp['current_weather']['windspeed']
wind_d = w_resp['current_weather']['winddirection']
sun_r = w_resp['daily']['sunrise'][1]
sun_s = w_resp['daily']['sunset'][1]

print("----- Weather -----")
print(f"Time : {time} {time_z} GMT")
print(f"Latitude : {g_lat:.2f}") # :.2f to shorter a float
print(f"Longtitude : {g_long:.2f}")
print(f"Temp : {temp} °C")
print(f"Wind Speed : {wind_s} Km/h")
print(f"Wind Direction : {wind_d}")
print("------- Sun ------- ")
print(f"Sun Rise : {sun_r} {time_z} GMT")
print(f"Sun Set : {sun_s} {time_z} GMT")
