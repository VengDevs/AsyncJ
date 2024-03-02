"""
:authors: VengDevs
:licence: Apache License, Version 2.0
:copyright: (c) 2024 VengDevs
"""

from ujson import loads, dumps


class SyncJson:
    """A class to read and write JSON files synchronously."""

    def __init__(self, filepath: str) -> None:
        """
        Initialize the class with the file path.

        :param filepath: Path to JSON file.
        """
        self.filepath: str = filepath

    def read(self) -> dict:
        """Read the JSON file and return a dictionary."""
        with open(self.filepath, encoding="utf-8") as file:
            return loads(obj=file.read())

    def write(self, data: dict) -> None:
        """
        Write a dictionary to the JSON file.

        :param data: Dictionary.
        """
        with open(self.filepath, "w", encoding="utf-8") as file:
            file.write(dumps(obj=data, indent=4))