import os
import subprocess

def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    try:
        working_directory_abs = os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(working_directory_abs, file_path))
        valid_target_dir = os.path.commonpath([working_directory_abs, target_path]) == working_directory_abs

        if valid_target_dir == False:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if os.path.isfile(target_path) == False:
            return f'Error: "{file_path}" does not exist or is not a regular file'

        if target_path.endswith(".py") == False:
            return f'Error: "{file_path}" is not a Python file'

        else:
            command = ["python", target_path]
            if args:
                command.extend(args)

            process = subprocess.run(
                command,
                cwd = working_directory_abs,
                capture_output = True,
                text = True,
                timeout = 30,
            )

            output = []

            if process.returncode != 0:
                output.append(f"Process exited with code {process.returncode}")

            if process.stdout:
                output.append(f"STDOUT:{process.stdout}")

            if process.stderr:
                output.append(f"STDERR:{process.stderr}")

            if not process.stdout and not process.stderr:
                output.append("No output produced")

        return "\n".join(output)

    except Exception as e:
        return f'Error: executing Python file: {e}'


schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Runs a python file and returns the output as a string",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "File path to execute file from, relative to the working directory (default is the working directory itself)",
                },
                "args": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "Optional command-line arguments to pass to the Python file.",
                },
            },
            "required": ["file_path"],
        },
    },
}
