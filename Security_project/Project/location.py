import asyncio
import winrt.windows.devices.geolocation as geolocation

async def get_location():
    try:
        access_status = await geolocation.Geolocator.request_access_async()
        if access_status == geolocation.GeolocationAccessStatus.allowed:
            geolocator = geolocation.Geolocator()
            geoposition = await geolocator.get_geoposition_async()
            coordinate = geoposition.coordinate
            return coordinate.latitude, coordinate.longitude
        else:
            print("Location access denied.")
            return None, None
    except Exception as e:
        print("Error:", e)
        return None, None

async def main():
    latitude, longitude = await get_location()
    if latitude is not None and longitude is not None:
        print("Latitude:", latitude)
        print("Longitude:", longitude)

if __name__ == "__main__":
    asyncio.run(main())
