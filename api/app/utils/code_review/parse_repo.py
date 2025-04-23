import os
import tempfile
import subprocess

def clone_github_repo(github_endpoint: str):
    temp_dir = tempfile.mkdtemp()
    try:
        subprocess.run(["git", "clone", github_endpoint, temp_dir], check=True)
        return temp_dir
    except subprocess.CalledProcessError as e:
        raise Exception(f"Failed to clone git repo: {str(e)}")
    
def read_code_from_temp_dir(temp_dir_path, extensions=(".py", ".java", ".cpp", ".go", "js", ".ts")):
    code = ""
    skip_dirs = {"node_modules", "__pycache__", ".git", "build", "dist", "venv", "env", "tests", ".idea", ".vscode"}
    for root, dirs, files in os.walk(temp_dir_path, topdown=True):
        dirs[:] = [d for d in dirs if d not in skip_dirs]
        for file in files:
            if file.endswith(extensions):
                full_path = os.path.join(root, file)
                try:
                    with open(full_path, "r", encoding="utf-8", errors="ignore") as f:
                        code += f"\n\n# File: {file}\n" + f.read()
                except Exception as e:
                    print(f"Error reading file at path: {os.path.join(root, file)}")
    return code
    