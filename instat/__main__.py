import asyncio

import click

from instat.weather_client import WeatherClient

@click.command()
@click.option("--api-token", "-a", required=True, help="OpenWeatherMap API token")
@click.argument("cities", nargs=3, default=["Moscow", "London", "New York"])
def main(api_token: str, cities: list[str]) -> None:
    weather_client = WeatherClient(api_token, cities)
    asyncio.run(weather_client.run())


if __name__ == "__main__":
    main()