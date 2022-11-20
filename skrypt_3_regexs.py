import re

text="Easssy python is easy to leeearn"
pattern=r"\bpyth22on\b"
match = re.search(pattern, text)
if match:
    print(f"Pattern {pattern} match to: {match.group()}")
    print(f"Staring index: {match.start()}")
    print(f"End index: {match.end()}")
    print(f"Length: {match.end() - match.start()}")
else:
    print("No patter found")

print(__name__)
