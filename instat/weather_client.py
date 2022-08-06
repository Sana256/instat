import asyncio
import json

import aiohttp


class WeatherClient:
    def __init__(self, api_token: str, cities: list[str]) -> None:
        self.api_token = api_token
        self.cities: list[tuple] = cities

    async def run(self) -> dict:
        tasks = []
        for city in self.cities:
            tasks.append(asyncio.ensure_future(self.get_weather_by_city(city)))
        results = await asyncio.gather(*tasks)
        await self.save_to_file(results)


    async def get_weather_by_city(self, city_name: str) -> dict:
        async with aiohttp.ClientSession(timeout = aiohttp.ClientTimeout(10), raise_for_status=True) as session:
            try:
                coord = ()
                async with session.get(
                    f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={self.api_token}"
                ) as resp:
                    resp_json = await resp.json()
                    if len(resp_json) < 1:
                        raise Exception("No city found")
                    
                    coord = resp_json["coord"]["lat"], resp_json["coord"]["lon"]

                async with session.get(
                    f"https://api.openweathermap.org/data/2.5/weather?lat={coord[0]}&lon={coord[1]}&appid={self.api_token}"
                ) as resp:
                    resp_json = await resp.json()
                    await self.save_to_file(resp_json)
                    return resp_json

            except Exception as e:
                print(e)
                return None

    async def save_to_file(self, weather: dict) -> None:
        with open("weather.json", "w") as f:
            json.dump(weather, f)
    