import httpx
from mcp.server.fastmcp import FastMCP

mcp= FastMCP("Weather")


@mcp.tool()
async def get_weather(location: str) -> str:
    """
    Get weather of a particular location using Open-Meteo API.

    Args:
        location (str): location name, e.g., 'New Delhi'

    Returns:
        str: weather description
    """
    # Get coordinates using Nominatim
    async with httpx.AsyncClient() as client:
        geocode_resp = await client.get(
            "https://nominatim.openstreetmap.org/search",
            params={"q": location, "format": "json"}
        )
        geocode_data = geocode_resp.json()
        if not geocode_data:
            return f"Could not find coordinates for '{location}'"

        lat = geocode_data[0]["lat"]
        lon = geocode_data[0]["lon"]

        # Fetch weather from Open-Meteo
        weather_resp = await client.get(
            "https://api.open-meteo.com/v1/forecast",
            params={
                "latitude": lat,
                "longitude": lon,
                "current_weather": True
            }
        )
        weather_data = weather_resp.json()
        weather = weather_data.get("current_weather", {})
        if not weather:
            return f"No weather data available for '{location}'"

        temp = weather["temperature"]
        wind = weather["windspeed"]
        return f"Current temperature in {location} is {temp}°C with windspeed {wind} km/h."

    
    


if __name__=='__main__':
    mcp.run(transport="streamable-http")