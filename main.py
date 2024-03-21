import requests
import json
import win32com.client as wincom
city = input("Enter The Name Of The City:")
url = f"https://api.weatherapi.com/v1/current.json?key=7e7e8992395343adb6e94814231608&q={city}"
r = requests.get(url)
# print(r.text)
wdict = json.loads(r.text)
w = wdict["current"]["temp_c"]
speak = wincom.Dispatch("SAPI.spVoice")
speak.Speak(f"The Current Weather in {city} is {w} Degree")
