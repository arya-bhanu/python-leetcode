class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        dicts = {}
        i = 0
        stripped = key.replace(" ", "")
        for k in stripped:
            if k in dicts:
                continue
            dicts[k] = i
            i += 1
        words = []
        for m in message:
            if m in dicts:
                words.append(chr(97 + (dicts[m])))
                continue
            words.append(m)
        joinned = "".join(words)
        return joinned
