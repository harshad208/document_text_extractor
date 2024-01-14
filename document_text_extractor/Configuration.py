import configparser
import os

try:
    config = configparser.RawConfigParser()

    # Get the path to the config.ini file within the package
    current_dir = os.path.dirname(os.path.abspath(__file__))
    config_file_path = os.path.join(current_dir, 'data', 'config.ini')

    try:
        config.read(config_file_path)
        temp_path = config.get("ENVIRONMENT", "TEMP_FOLDER_PATH")

        # Ensure the temp folder exists, create it if not
        if not os.path.exists(temp_path):
            os.makedirs(temp_path)

    except Exception as e:
        print(f"Error reading configuration: {e}")

except Exception as e:
    print(e)
