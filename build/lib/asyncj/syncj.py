"""
:authors: VengDevs
:licence: Apache License, Version 2.0
:copyright: (c) 2024 VengDevs
"""

from os.path import exists

from ujson import loads, dumps


class SyncJson:
    """A class to read and write JSON files synchronously."""

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
