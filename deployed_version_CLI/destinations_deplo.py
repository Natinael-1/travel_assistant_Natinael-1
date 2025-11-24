import requests
import os
import time

url_endpt = "https://apidojo-booking-v1.p.rapidapi.com/locations/auto-complete"
RAPID_BOOKING_API_KEY = os.getenv("RAPID_BOOKING_API_KEY")

# accepting city as argument
def getCityInfo(destination_city):
    if not destination_city:
        print("Error: No city provided.")
        return

    print(f"Finding destination details for {destination_city}--------")

    query_dic = {
        "text": destination_city,
        "languagecode": "en-us"
    }

    headers = {
        "x-rapidapi-key": RAPID_BOOKING_API_KEY,
        "x-rapidapi-host": "apidojo-booking-v1.p.rapidapi.com"
    }

    response = requests.get(url_endpt, headers=headers, params=query_dic)

    if response.status_code == 200:
        response_list = response.json()
        city_item = [item for item in response_list if item["dest_type"] == "city"]
        
        if city_item:
            for city in city_item:
                print(f"\n\t\t================== Details about \"{destination_city}\" ====================")
                print(f"\t\tCity Found: {city['label']}")
                print(f"\t\tCountry: {city['country']}")
                print(f"\t\tRegion: {city['region']}")
                print(f"\t\tHotels Available: {city['nr_hotels']}")
                print(f"\t\tDestination ID: {city['dest_id']}")
                print("=============================================================\n")
        else:
            print("\t\t❌ No city found.")
    else:
        print("\t\t❌ Oops! Request is not successful.")