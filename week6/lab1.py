import os

directories = ["date.md", "generators.md", "json.md", "Readme.md"]

for directory in directories:
    print(f"Contents of {directory}:")
    for root, dirs, files in os.walk(directory):
        for file in files:
            print(os.path.join(root, file))
        for dir in dirs:
            print(os.path.join(root, dir))