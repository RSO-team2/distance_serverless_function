import os

import googlemaps


def main(args):
    origin = args.get("origin")
    destination = args.get("destination")

    if not origin or not destination:
        return {
            "body": "Error: 'origin' and 'destination' parameters are required.",
            "statusCode": 400,
        }
    
    if "lat" in destination and "long" in destination:
        split_destination = destination.split(",")
        destination = {
            "lat": split_destination[0].replace("lat: ", ""),
            "long": split_destination[1].replace("long: ", ""),
        }

    # Google Maps API key
    try:
        gmaps = googlemaps.Client(key=os.environ.get("GOOGLE_MAPS_API_KEY"))
        matrix = gmaps.distance_matrix(origin, destination)

        return {
            "body": {
                "distance": matrix["rows"][0]["elements"][0]["distance"]["text"],
                "duration": matrix["rows"][0]["elements"][0]["duration"]["text"],
            },
            "statusCode": 200,
        }
    except Exception as e:
        return {"body": f"Error: {str(e)}", "statusCode": 500}
