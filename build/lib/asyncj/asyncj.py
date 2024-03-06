"""
:authors: VengDevs
:licence: Apache License, Version 2.0
:copyright: (c) 2024 VengDevs
"""

from os.path import exists

from aiofiles import open as aiopen
from ujson import loads, dumps


class AsyncJson:
    """A class to read and write JSON files asynchronously."""

    def __init__(self, filepath: str, create_if_not_exists: bool = True, default_type: dict | list = {}) -> None:
        """
        Initialize the class with the file path.

        :param filepath: Path to JSON file.
        :param create_if_not_exists: Creating a file if it doesn't exist.
        :param default_type: The default file fill type (when created) is dictionary or list.
        """
        self.filepath: str = filepath
        self.create_if_not_exists: bool = create_if_not_exists
        self.default_type: dict | list = default_type

        if self.create_if_not_exists:
            if not exists(self.filepath):
                with open(self.filepath, "w", encoding="utf-8") as file:
                    file.write(dumps(obj=self.default_type, indent=4))

        with open(self.filepath, "r+", encoding="utf-8") as file:
            if file.read() == "":
                file.write(dumps(obj=self.default_type, indent=4))


    async def read(self) -> dict | list:
        """Read the JSON file and return a dictionary or list."""
        async with aiopen(self.filepath, encoding="utf-8") as file:
            return loads(obj=await file.read())

    async def write(self, data: dict | list) -> None:
        """
        Write a dictionary or list to the JSON file.

        :param data: Dictionary.
        """
        async with aiopen(self.filepath, "w", encoding="utf-8") as file:
            await file.write(dumps(obj=data, indent=4))