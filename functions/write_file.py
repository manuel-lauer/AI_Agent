import os

def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        working_directory_abs = os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(working_directory_abs, file_path))
        valid_target_dir = os.path.commonpath([working_directory_abs, target_path]) == working_directory_abs

        if os.path.isdir(target_path) == True:
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        if valid_target_dir == False:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        else:
            parent_directory = os.path.dirname(target_path)
            os.makedirs(parent_directory, exist_ok=True)
            with open(target_path, "w") as f:
                f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f'Error: {e}'


schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Writes content to a file, creating or overwriting it",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "File path to open file from, relative to the working directory (default is the working directory itself)",
                },
                "content": {
                    "type": "string",
                    "description": "Content that is written to the opened file",
                },
            },
            "required": ["file_path", "content"],
        },
    },
}
