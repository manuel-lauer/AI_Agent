import os
from config import MAX_CHARS

def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        working_directory_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_directory_abs, file_path))
        valid_target_dir = os.path.commonpath([working_directory_abs, target_dir]) == working_directory_abs

        if os.path.isfile(target_dir) == False:
            return f'Error: File not found or is not a regular file: "{file_path}"'

        if valid_target_dir == False:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        else:
            with open(target_dir, "r") as f:
                file_content_string = f.read(MAX_CHARS)
                if f.read(1):
                    file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
            return file_content_string

    except Exception as e:
        return f'Error: {e}'

schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": "Opens files in a specified directory relative to the working directory, reading the first 10,000 characters",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "File path to read file from, relative to the working directory (default is the working directory itself)",
                },
            },
            "required": ["file_path"],
        },
    },
}
