from setuptools import setup, find_packages
import json
import os


# Function to embed config.json data
def read_config():
    config_path = "config.json"
    if os.path.exists(config_path):
        with open(config_path, "r") as f:
            return json.load(f)
    else:
        return {}


# Read your config.json into a string (we'll inject this into main.py during build)
config_data = json.dumps(read_config())


# Custom command to modify main.py before build
class PreBuildCommand:
    def run(self):
        # Ensure `EMBEDDED_CONFIG` in `main.py` is replaced with the actual config data
        with open("main.py", "r") as file:
            content = file.read()

        # Replace placeholder with actual config data
        content = content.replace(
            "EMBEDDED_CONFIG = None", f"EMBEDDED_CONFIG = {config_data}"
        )

        with open("main.py", "w") as file:
            file.write(content)


# Pass PreBuildCommand to handle the config injection
setup(
    name="calculator",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "PyQt6",
        "PyQt6-Qt6",
    ],
    include_package_data=True,
    cmdclass={
        "build_py": PreBuildCommand,  # Custom pre-build command
    },
    entry_points={
        "console_scripts": [
            "calculator=main:main",  # Or your main entry point for the script
        ]
    },
)
