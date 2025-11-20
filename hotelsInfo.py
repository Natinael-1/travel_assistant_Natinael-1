#Importing requests and os libraries to make request and access env variable respectively
import requests
import os
url_list = "https://apidojo-booking-v1.p.rapidapi.com/properties/v2/list"
RAPID_BOOKING_API_KEY = os.getenv("RAPID_BOOKING_API_KEY")

def hotel_finder(search_type):
    querystring = {"offset":"0",
                   "guest_qty":"1", 
                   "dest_ids":"-3712125",
                   "room_qty":"1",
                   "search_type":"city",
                   "arrival_date": "2025-11-27", 
                   "departure_date": "2025-11-29"
                   }
    
    
    arrival_date = input("\t\tArrival date(yyyy-mm-dd): ")
    departure_date = input("\t\tDeparture date(yyyy-mm-dd):")

    offset = input("\t\tOffset(beginning page number): ")
    guest_qty = input("\t\tGuest quantity: ")
    dest_ids = input("\t\tDestination Id: ")
    room_qty = input("\t\tRoom quantity: ")

    querystring.update({"offset": offset, 
                        "guest_qty": guest_qty, 
                        "dest_ids": dest_ids, 
                        "room_qty": room_qty, 
                        "arrival_date": arrival_date, 
                        "departure_date": departure_date})
    querystring["search_type"] = search_type.lower()


    headers = {
        "x-rapidapi-key": RAPID_BOOKING_API_KEY,
        "x-rapidapi-host": "apidojo-booking-v1.p.rapidapi.com"
    }
    response = requests.get(url_list, headers=headers, params=querystring)
    response_dic = response.json()
    hotels = response_dic.get("result", [])

    print(f"\n\t\t====Details of hotels in the \"{search_type}\"===")
    if hotels:
        for ciho in hotels:
            if ciho.get("type") == "banner":
                continue
            else:
                print(f"\t\tHotel Name: {ciho['hotel_name']}")
                print(f"\t\tHotel Id: {ciho['hotel_id']}")
                print(f"\t\tAddress: {ciho.get('address','N/A')}")
                print(f"\t\tRating: {ciho.get('review_score', 'N/A')}")
                print(f"\t\tReview Count: {ciho.get('review_nr', 'N/A')}")
                print(f"\t\tDistance to City center: {ciho.get('distance_to_city_center', 'N/A')}")
                print(f"\t\tDistrict: {ciho.get('district', 'N/A')}")
                price = ciho.get("composite_price_breakdown", {}).get("all_inclusive_amount", {})
                print(f"\t\tPrice per night: {price.get('value', 'N/A')}")
                print(f"\t\tCurrency: {price.get('currency', 'N/A')}")
                print("=====================================================")
    else:
        print("\t\t❌ No Hotels Found")

    


        



    