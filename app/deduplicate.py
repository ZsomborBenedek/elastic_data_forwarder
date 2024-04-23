import hashlib
import json


class Deduplicator:
    filename: str

    def __init__(self, filename: str):
        """Class for deduplicating a list of dicts based on their hash.

        Args:
            filename (str): File to use for deduplication.
        """
        self.filename = filename

    def get_md5(self, data: dict):
        """Calculate the MD5 hash of a dictionary.

        Args:
            data (dict): Dict to encode.

        Returns:
            str: Hash of dict.
        """
        hash_md5 = hashlib.md5(json.dumps(data, sort_keys=True).encode())
        return hash_md5.hexdigest()

    def uniques(self, input_list: list):
        """Get unique dicts from a list based on their MD5 hashes.

        Args:
            input_list (list): List of dicts.

        Returns:
            list: Unique list of dicts.
        """
        with open(self.filename, "a+") as file:
            file.seek(0)
            existing_hashes = [line.strip() for line in file]
            deduplicated_list = [
                item for item in input_list if self.get_md5(item) not in existing_hashes
            ]
            return deduplicated_list

    def store(self, new_list: list):
        """Write the new dicts to the end of the file.

        Args:
            new_list (list): New list of dicts.
        """
        with open(self.filename, "a+") as file:
            for item in new_list:
                file.write(f"{self.get_md5(item)}\n")
