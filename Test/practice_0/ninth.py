# Practice 8: Virtual environments and project metadata
# This file explains how to work with environment files and package configuration.
# It also shows how to read a requirements.txt file using Python.

from pathlib import Path

project_folder = Path("JustForFun/Test/practice_0")
requirements_file = project_folder / "requirements.txt"
pyproject_file = project_folder / "pyproject.toml"

print("Practice 8: Environment and project files")
print("requirements.txt path:", requirements_file)
print("pyproject.toml path:", pyproject_file)

# Read requirements.txt if it exists.
if requirements_file.exists():
    print("requirements.txt content:")
    print(requirements_file.read_text(encoding="utf-8"))
else:
    print("requirements.txt does not exist yet.")

# Read pyproject.toml if it exists.
if pyproject_file.exists():
    print("pyproject.toml content:")
    print(pyproject_file.read_text(encoding="utf-8"))
else:
    print("pyproject.toml does not exist yet.")

print("\nNotes for a beginner:")
print("- Use venv to isolate Python packages for this project.")
print("- Create a virtual environment with: python -m venv .venv")
print("- Activate it before installing packages.")
print("- requirements.txt lists the packages your code needs.")
print("- pyproject.toml is a modern file to describe your Python project.")
