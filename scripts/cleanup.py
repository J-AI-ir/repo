# directory = "/Users/javid/Projects/lobe/repo/public/agents"  # Change this to your actual path
# new_author = "JAI"
# new_homepage = "https://j-ai.ir"

import os
import json

# Define the directory containing JSON files
directory = "/Users/javid/Projects/lobe/repo/public/agents"  # Update this to the correct directory path

# Define new values for "author" and "homepage"
new_author = "JAI"
new_homepage = "https://j-ai.ir"

# Check if the directory exists
if not os.path.exists(directory):
    print(f"Directory not found: {directory}")
else:
    print(f"Processing files in: {directory}")

# Iterate through all files in the directory
for filename in os.listdir(directory):
    if filename.endswith(".json"):
        filepath = os.path.join(directory, filename)
        print(f"Processing file: {filename}")

        try:
            # Load JSON file
            with open(filepath, "r") as file:
                data = json.load(file)

            # Update "author" and "homepage" values if they exist
            if "author" in data:
                data["author"] = new_author
            if "homepage" in data:
                data["homepage"] = new_homepage

            # Save the updated JSON file
            with open(filepath, "w") as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
            
            print(f"Updated: {filename}")

        except json.JSONDecodeError:
            print(f"Error: Invalid JSON in {filename}")
        except Exception as e:
            print(f"Error processing {filename}: {e}")

print("All files processed.")
