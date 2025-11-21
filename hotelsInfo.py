#Importing requests and os libraries to make request and access env variable respectively
import requests
import os
url_list = "https://apidojo-booking-v1.p.rapidapi.com/properties/v2/list"
url_getroom = "https://apidojo-booking-v1.p.rapidapi.com/properties/v2/get-rooms"
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
                print(f"\t\tSearch Id: {ciho.get('search_ids', 'N/A')}")
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
def get_rooms():
    room_querystring = {}
    headers = {
	"x-rapidapi-key": RAPID_BOOKING_API_KEY,
	"x-rapidapi-host": "apidojo-booking-v1.p.rapidapi.com"
    }

    hotel_id = input("\t\tHotel Id: ")
    departure_date = input("\t\tDeparture date: ")
    arrival_date = input("\t\tArrival date: ")
    rec_guest_qty = input("\t\tGuest quantity: ")
    rec_room_qty = input("\t\tRoom quantity: ")
    room_querystring.update({"hotel_id": hotel_id, "departure_date": departure_date, "arrival_date": arrival_date, "rec_guest_qty":rec_guest_qty, "rec_room_qty":rec_room_qty})

    room_response = requests.get(url_getroom, headers=headers, params=room_querystring)
    if room_response.status_code == 200:
        room_response = room_response.json()
        for room_deta in room_response:
            room = room_deta.get("rooms")
            if isinstance(room, dict):     
                for room_type, room_details in room.items():
                    print("=========================================================")
                    print(f"\t\tRoom type Id: {room_type}")
                    room_details_value = room_details.get("facilities",[])
                    for facility in room_details_value:
                        print(f"\t\tRoom ID: {facility.get('id', 'N/A')}")
                        print(f"\t\tName: {facility.get('name', 'N/A')}")
                        print(f"\t\tFacility description: {facility.get('alt_facilitytype_name', 'N/A')}")
                        print(f"-------------------------------")                   
                    print(f"\t\tDescription: {room_details.get('description', 'N/A')}")
                    bed_desc = room_details.get("bed_configurations", [])
                    for bed in bed_desc:
                        bed_info = bed.get('bed_types', [])
                        for bed_detail in bed_info:
                            print(f"\t\tBed description: {bed_detail.get('description', 'N/A')}")
                            print(f"\t\tNumber of beds: {bed_detail.get('name_with_count', 'N/A')}")
                    image = room_details.get("photos", [])
                    for image_detail in image:
                        print(f"Photo_URL: {image_detail.get('url_original', 'N/A')}")

                    print("------------------------------------------")

    elif room_response.status_code == 204:
        print("\t\tMissing or invalid parameters.")
    elif room_response.status_code == 302:
        print("\t\tReached page but response is empty or redirected.")
    elif room_response.status_code == 400:
        print("\t\tBad input parameter.")
    elif room_response.status_code == 403:
        print("\t\tAccess denied due to bot protection on server.")

    




        



    