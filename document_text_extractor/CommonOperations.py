import base64
import logging


def convert_input_to_format(file_input: dict, temp_path: str):
    try:
        base64_str = file_input['Object']
        file_name = file_input['ObjectName']
        file_format = file_input['ObjectFormat']

        decoded_bytes = base64.b64decode(base64_str)
        file_path = temp_path + "/" + file_name + "." + file_format
        with open(file_path, "wb") as output_file:
            output_file.write(decoded_bytes)
        return file_path

    except Exception as e:
        logging.error(str(e), exc_info=True)


def convert_to_json(file_name: str = None, file_format: str = None, base64_str: str = None):
    try:

        return {
            "ObjectName": file_name,
            "ObjectFormat": file_format,
            "Object": base64_str
        }
    except Exception as e:
        print(e)
