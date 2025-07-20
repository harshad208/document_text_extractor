import configparser
import os

try:
    config = configparser.RawConfigParser()

    current_dir = os.path.dirname(os.path.abspath(__file__))
    config_file_path = os.path.join(current_dir, 'data', 'config.ini')

    try:
        config.read(config_file_path)
        temp_path = config.get("ENVIRONMENT", "TEMP_FOLDER_PATH")

        if not os.path.exists(temp_path):
            os.makedirs(temp_path)
        host = config.get("ENVIRONMENT", "HOST")
        port = int(config.get("ENVIRONMENT", "PORT"))
    except Exception as e:
        print(f"Error reading configuration: {e}")

except Exception as e:
    print(e)
