from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from dotenv import dotenv_values, load_dotenv
import json
import os

# Load environment variables from .env file
load_dotenv()

# Get the directory to scan from the MY_APP_DIR environment variable,
# defaulting to /usr/local/etc if the variable is not set
dir = os.getenv("MY_APP_DIR", "/usr/local/etc")

app = FastAPI()
# Specify the directory where the Jinja2 templates are located
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_env(request: Request, search: str = ""):
    """Return a list of environment variables in .env and .json files in the specified directory."""

    # Dictionary to store file paths and their environment variables
    files_dict = {}

    # Recursively scan the directory
    for root, dirs, files in os.walk(dir):
        for file in files:
            if file.endswith('.env'):
                env_path = os.path.join(root, file)
                # Get a dictionary of the environment variables in the .env file
                env_dict = dotenv_values(env_path)
                files_dict[env_path] = env_dict
            elif file.endswith('.json'):
                json_path = os.path.join(root, file)
                with open(json_path, 'r') as json_file:
                    # Load the JSON file into a dictionary
                    json_dict = json.load(json_file)
                files_dict[json_path] = json_dict

    # If a search term is provided, filter the environment variables
    if search:
        files_dict = {
            file_path: {key: value for key, value in env_dict.items() if search.lower() in key.lower() or search.lower() in value.lower()}
            for file_path, env_dict in files_dict.items()
        }

    # Return a TemplateResponse with the request and environment variables
    return templates.TemplateResponse("index.html", {"request": request, "files_dict": files_dict})

@app.post("/update", response_class=HTMLResponse)
async def update_env(request: Request, file_path: str = Form(...), key: str = Form(...), value: str = Form(...)):
    """Update an environment variable in a .env or .json file."""

    # If the file is a .env file
    if file_path.endswith('.env'):
        # Open the file and read all the lines
        with open(file_path, 'r') as file:
            lines = file.readlines()
        # Open the file again to write the updated lines
        with open(file_path, 'w') as file:
            for line in lines:
                # If the line starts with the environment variable key, replace the line with the updated value
                if line.startswith(key + '='):
                    file.write(key + '=' + value + '\n')
                else:
                    file.write(line)
    # If the file is a .json file
    elif file_path.endswith('.json'):
        # Open the file and load the JSON into a dictionary
        with open(file_path, 'r') as json_file:
            json_dict = json.load(json_file)
        # Update the value of the environment variable in the dictionary
        json_dict[key] = value
        # Open the file again to write the updated JSON
        with open(file_path, 'w') as json_file:
            json.dump(json_dict, json_file)

    # Return the updated list of environment variables
    return await read_env(request)
