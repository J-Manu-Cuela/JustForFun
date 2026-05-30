# Practice 4: File input and output in Python
# This file covers reading and writing text, JSON, and CSV files.

from pathlib import Path
import json
import csv

folder = Path("JustForFun/Test/practice_0")
text_file = folder / "practice4_sample.txt"
json_file = folder / "practice4_sample.json"
csv_file = folder / "practice4_sample.csv"

# 1) Write and read a plain text file.
lines = ["Linea 1", "Linea 2", "Linea 3"]
text_file.write_text("\n".join(lines), encoding="utf-8")
print("Wrote text file to", text_file)

content = text_file.read_text(encoding="utf-8")
print("Text file content:")
print(content)

# 2) Write and read a JSON file.
person = {
    "name": "Manu",
    "age": 30,
    "skills": ["Python", "programming", "automation"],
}
with json_file.open("w", encoding="utf-8") as handle:
    json.dump(person, handle, indent=2, ensure_ascii=False)
print("Wrote JSON file to", json_file)

with json_file.open("r", encoding="utf-8") as handle:
    loaded_person = json.load(handle)
print("Loaded JSON data:", loaded_person)

# 3) Write and read a CSV file.
rows = [
    ["name", "score"],
    ["Manu", 95],
    ["Ana", 88],
]
with csv_file.open("w", newline="", encoding="utf-8") as handle:
    writer = csv.writer(handle)
    writer.writerows(rows)
print("Wrote CSV file to", csv_file)

with csv_file.open("r", newline="", encoding="utf-8") as handle:
    reader = csv.reader(handle)
    for row in reader:
        print("CSV row:", row)
