# directory = "/Users/javid/Projects/lobe/repo/docs/public/plugins"  # Update this to the correct directory path
# new_author = "J-AI-ir"
# new_homepage = "https://j-ai.ir"

import os
import json

directory = "/Users/javid/Projects/lobe/repo/docs/public/plugins"  # Update this to the correct directory path
new_author = "J-AI-ir"
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

            # Check for different formats and update "author" and "homepage"
            updated = False

            # 1. Format with "plugins" list
            if "plugins" in data:
                for plugin in data["plugins"]:
                    if "author" in plugin:
                        plugin["author"] = new_author
                    if "homepage" in plugin:
                        plugin["homepage"] = new_homepage
                updated = True

            # 2. Format with "agents" list
            if "agents" in data:
                for agent in data["agents"]:
                    if "author" in agent:
                        agent["author"] = new_author
                    if "homepage" in agent:
                        agent["homepage"] = new_homepage
                updated = True

            # 3. Top-level "author" and "homepage"
            if "author" in data:
                data["author"] = new_author
                updated = True
            if "homepage" in data:
                data["homepage"] = new_homepage
                updated = True

            # Save the updated JSON file if any field was updated
            if updated:
                with open(filepath, "w") as file:
                    json.dump(data, file, indent=4, ensure_ascii=False)
                print(f"Updated: {filename}")

        except json.JSONDecodeError:
            print(f"Error: Invalid JSON in {filename}")
        except Exception as e:
            print(f"Error processing {filename}: {e}")

print("All files processed.")
