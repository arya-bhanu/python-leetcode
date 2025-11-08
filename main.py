from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        sets = set()
        morse_code = [
            ".-",
            "-...",
            "-.-.",
            "-..",
            ".",
            "..-.",
            "--.",
            "....",
            "..",
            ".---",
            "-.-",
            ".-..",
            "--",
            "-.",
            "---",
            ".--.",
            "--.-",
            ".-.",
            "...",
            "-",
            "..-",
            "...-",
            ".--",
            "-..-",
            "-.--",
            "--..",
        ]
        morse_code_map = {}
        for i in range(len(morse_code)):
            morse_code_map[chr(i + 97)] = morse_code[i]
        for word in words:
            morse = ""
            for w in word:
                morse += morse_code_map[w]
            sets.add(morse)
        return len(sets)
