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
    
    # Parse latitude and logitude from the destination as defined in the order_management microservice
    if "lat" in destination and "long" in destination:
        split_destination = destination.split(",")
        destination = (
            split_destination[0].replace("lat: ", ""),
            split_destination[1].replace("long: ", ""),
        )

    try:
        # Access Google Maps API
        gmaps = googlemaps.Client(key=os.environ.get("GOOGLE_MAPS_API_KEY"))
        matrix = gmaps.distance_matrix(origin, destination)
        # Return the distance and duration
        return {
            "body": {
                "distance": matrix["rows"][0]["elements"][0]["distance"]["text"],
                "duration": matrix["rows"][0]["elements"][0]["duration"]["text"],
            },
            "statusCode": 200,
        }
    except Exception as e:
        return {"body": f"Error: {str(e)}", "statusCode": 500}
