import requests
import os
import time

url_endpt = "https://apidojo-booking-v1.p.rapidapi.com/locations/auto-complete"
RAPID_BOOKING_API_KEY = os.getenv("RAPID_BOOKING_API_KEY")

def displayCityInfo():
    destination_city = input("\t\t🏢 City you want to travel to or check(London): ")
    print("Finding destination details--------")
    time.sleep(3)

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
        # Find the first CITY result
        city_item = []
        district_item = []
        airport_item = []
        for item in response_list:
            if item["dest_type"] == "city":
                city_item.append(item)
            elif item["dest_type"] == "district":
                district_item.append(item)
            elif item["dest_type"] == "airport":
                airport_item.append(item)
        #Print city if exists
        if city_item:
            for city in city_item:
                print(f"\n\t\t================== Details about \"{destination_city}\" ====================")
                print(f"\t\tCity Found: {city['label']}")
                print(f"\t\tCountry: {city['country']}")
                print(f"\t\tRegion: {city['region']}")
                print(f"\t\tTimezone: {city['timezone']}")
                print(f"\t\tHotels Available: {city['nr_hotels']}")
                print(f"\t\tDestination ID: {city['dest_id']}")
                print("=============================================================\n")
        else:
            print("\t\t❌ No city found.")
        if district_item:
            for district in district_item:
                print(f"\n\t\t===========Details about district of {destination_city}============")
                print(f"\t\tDistrict Found: {district['label']}")
                print(f"\t\tCountry: {district['country']}")
                print(f"\t\tRegion: {district['region']}")
                print(f"\t\tTimezone: {district['timezone']}")
                print(f"\t\tHotels Available: {district['nr_hotels']}")
                print(f"\t\tDestination ID: {district['dest_id']}")
                print("=============================================================\n")
        else:
            print("\t\t❌ No district found.")

        if airport_item:
            for airport in airport_item:
                print(f"\n\t\t===========Details about airport in {destination_city} ============")
                print(f"\t\tAirport Found: {airport['label']}")
                print(f"\t\tCountry: {airport['country']}")
                print(f"\t\tRegion: {airport['region']}")
                print(f"\t\tTimezone: {airport['timezone']}")
                print(f"\t\tHotels Available: {airport['nr_hotels']}")
                print(f"\t\tDestination ID: {airport['dest_id']}")
                print("=============================================================\n")
        else:
            print("\t\t❌ No airport found.")
    else:
        print("\t\t❌ Oops! Request is not successful.")
  



