# Practice 9: Type hints and useful standard libraries
# This file uses type hints and the standard libraries mentioned in the plan.

import os
import sys
import re
import json
import logging
from pathlib import Path
from datetime import datetime
from typing import Optional, Union, Any, List, Dict

# Configure logging to show messages in the console.
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

# Example function with type hints for input and output.
def format_name(name: str, nickname: Optional[str] = None) -> str:
    if nickname:
        return f"{name} ({nickname})"
    return name

# Example function using Union and Any.
def parse_value(value: Union[str, int, float, None]) -> Any:
    if value is None:
        return None
    if isinstance(value, str):
        value = value.strip()
        if value.isdigit():
            return int(value)
        try:
            return float(value)
        except ValueError:
            return value
    return value

example_name = format_name("Manu", nickname="M")
print(example_name)
print(parse_value(" 42 "))
print(parse_value("3.14"))
print(parse_value("hello"))

# Use pathlib and datetime to build a timestamped filename.
folder = Path("JustForFun/Test/practice_0")
output_file = folder / f"practice9_output_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

result: Dict[str, Any] = {
    "name": example_name,
    "number": parse_value(" 99 "),
    "created_at": datetime.now().isoformat(),
}

# Write a JSON file using the standard library.
output_file.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
print("Wrote output JSON to", output_file)

# Use os and sys to inspect the running environment.
print("Python executable:", sys.executable)
print("Current working directory:", Path.cwd())
print("List directory with os.listdir:", os.listdir(folder))

# Use regex to extract words from a test string.
text = "Aprender Python es útil: 100% cierto."
matches = re.findall(r"\w+", text, flags=re.UNICODE)
print("Words found by regex:", matches)

logging.info("Practice 9 finished successfully.")
