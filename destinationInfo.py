import requests
import os

url_endpt = "https://apidojo-booking-v1.p.rapidapi.com/locations/auto-complete"
RAPID_BOOKING_API_KEY = os.getenv("RAPID_BOOKING_API_KEY")

def displayCityInfo():
    destination_city = input("🏢 City you want to travel to: ")

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
                print(f"\n================== Details about \"{destination_city}\" ====================")
                print(f"Destination Found: {city['label']}")
                print(f"Country: {city['country']}")
                print(f"Region: {city['region']}")
                print(f"Timezone: {city['timezone']}")
                print(f"Hotels Available: {city['nr_hotels']}")
                print(f"Destination ID: {city['dest_id']}")
                print("=============================================================\n")
        else:
            print("❌ No city found.")
        if district_item:
            for district in district_item:
                print(f"\n===========Details about district of {destination_city}============")
                print(f"District Found: {district['label']}")
                print(f"Country: {district['country']}")
                print(f"Region: {district['region']}")
                print(f"Timezone: {district['timezone']}")
                print(f"Hotels Available: {district['nr_hotels']}")
                print(f"Destination ID: {district['dest_id']}")
                print("=============================================================\n")
        else:
            print("❌ No district found.")

        if airport_item:
            for airport in airport_item:
                print(f"\n===========Details about airport in {destination_city} ============")
                print(f"Airport Found: {airport['label']}")
                print(f"Country: {airport['country']}")
                print(f"Region: {airport['region']}")
                print(f"Timezone: {airport['timezone']}")
                print(f"Hotels Available: {airport['nr_hotels']}")
                print(f"Destination ID: {airport['dest_id']}")
                print("=============================================================\n")
        else:
            print("❌ No airport found.")

    elif response.status_code == 204:
        print("Missing or invalid parameters.")
    elif response.status_code == 302:
        print("Reached page but response is empty or redirected.")
    elif response.status_code == 400:
        print("Bad input parameter.")
    elif response.status_code == 403:
        print("Access denied due to bot protection on server.")


