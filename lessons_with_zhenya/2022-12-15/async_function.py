import asyncio
from maps_coordinates import get_coordinates


async def main():
    result = await asyncio.gather(
        get_coordinates("Berlin"),
        get_coordinates("Stockholm"),
        get_coordinates("Brussels"),
        get_coordinates("Prague"),
        get_coordinates("Kiruna"),
    )
    print(result)


asyncio.run(main())
