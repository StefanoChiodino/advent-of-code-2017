import os
from typing import List


class Day4:
    @staticmethod
    def is_passphrase_valid(passphrase: str) -> bool:
        words = passphrase.split(" ")
        words_set = set(words)
        is_valid = len(words) == len(words_set)
        return is_valid

    @staticmethod
    def get_valid_passphrases(passphrases: List[str]) -> List[str]:
        valid_passphrases = [pp for pp in passphrases if Day4.is_passphrase_valid(pp)]
        return valid_passphrases


if __name__ == "__main__":
    path = os.path.join("..", "inputs", "day4_inputs.txt")
    passphrases = [line.strip() for line in open(path, "r")]
    valid_passphrases = Day4.get_valid_passphrases(passphrases)
    print(len(valid_passphrases))