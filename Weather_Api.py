# Python program to find current
# weather details of any city
# using openweathermap api

# import required modules
import requests
import json
import math
# import the pyttsx library
import pyttsx3

# initialisation
engine = pyttsx3.init()

# Enter your API key here
api_key = ".........."
# base_url variable to store url
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# Give city name
city_name = input("Enter city name : ")

# complete_url variable to store
# complete url address
complete_url = base_url + "appid=" + api_key + "&q=" + city_name

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

# get method of requests module
# return response object
response = requests.get(complete_url)

# json method of response object
# convert json format data into
# python format data
x = response.json()
jprint(x)

# Now x contains list of nested dictionaries
# Check the value of "cod" key is equal to
# "404", means city is found otherwise,
# city is not found
if x["cod"] != "404":
	# store the value of "main"
	# key in variable y
	y = x["main"]

	# store the value corresponding
	# to the "temp" key of y
	current_temperature = y["temp"]
   
    
	# store the value corresponding
	# to the "pressure" key of y
	current_pressure = y["pressure"]

	# store the value corresponding
	# to the "humidity" key of y
	current_humidity = y["humidity"]

	# store the value of "weather"
	# key in variable z
	z = x["weather"]

	# store the value corresponding
	# to the "description" key at
	# the 0th index of z
	weather_description = z[0]["description"]

else:
	print(" City Not Found ")

# convert to Fahrenheit
fahrenheit_temp =(current_temperature-273.15)*1.8+32
current_temp=round(fahrenheit_temp)

#conver hectopascal (hPa) to barometric pressure
barometric_pressure = current_pressure*0.030
format_pressure = "{:.2f}".format(barometric_pressure)

# print following values
print(" Temperature (in Fahrenheit) = " +
str(current_temp) +
"\n atmospheric pressure (in Barometer) = " +
str(format_pressure) +
"\n humidity (in percentage) = " +
str(current_humidity) +
"\n description = " +
str(weather_description))

engine.say("Current Weather Condition for" +city_name)
engine.say("The temperature (in Fahrenheit) is" + str(current_temp) +"degrees")
engine.say("The atmospheric pressure is" + str(format_pressure)+"inches Barometer" )
engine.say("Current humidity is"+ str(current_humidity)+"percent")
engine.say("Weather Description "+str(weather_description))
engine.say("Have a good day!")
engine.runAndWait()


