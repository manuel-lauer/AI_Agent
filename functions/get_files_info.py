import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        working_directory_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_directory_abs, directory))
        valid_target_dir = os.path.commonpath([working_directory_abs, target_dir]) == working_directory_abs

        if os.path.isdir(target_dir) == False:
            return f'Error: "{directory} is not a directory'

        if valid_target_dir == False:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        else:
            try:
                dir_info = ""
                for file in os.listdir(target_dir):
                    file_path = os.path.join(target_dir, file)
                    file_info = f'- {file}: file_size={os.path.getsize(file_path)} bytes, is_dir={os.path.isdir(file_path)}\n'
                    dir_info = dir_info + file_info
                return dir_info
            except Exception as e:
                return f'Error: {e}'
    except Exception as e:
        return f'Error: {e}'


schema_get_files_info = {
    "type": "function",
    "function": {
        "name": "get_files_info",
        "description": "Lists files in a specified directory relative to the working directory, providing file size and directory status",
        "parameters": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}
