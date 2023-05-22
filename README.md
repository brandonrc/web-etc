# Web-etc

This application allows users to view and edit `.env` and `.json` configuration files in a specified directory. The directory to scan is specified by the `MY_APP_DIR` environment variable.

## Installation

1. Clone this repository: `git clone https://github.com/username/web-etc.git`
2. Navigate to the app directory: `cd web-etc`
3. Install the application: `poetry install`
4. Set the `MY_APP_DIR` environment variable to the directory you want to scan: `export MY_APP_DIR=/your/directory/path`
5. Run the application: `uvicorn web_etc.main:app`

## Running as a Systemd Service

If you want to run this application as a systemd service, you can use the provided service file (`web-etc.service`). Here are the steps to do that:

1. Replace `/path/to/your/web-etc/directory` in `web-etc.service` with the path to your `web-etc` directory, and `yourusername` and `yourgroup` with your username and group respectively.
2. Copy the service file to your systemd directory, usually `/etc/systemd/system/`: `sudo cp web-etc.service /etc/systemd/system/`
3. Start the service: `sudo systemctl start web-etc`
4. Enable the service to run on startup: `sudo systemctl enable web-etc`

## Usage

Navigate to `http://localhost:8000` in your web browser. You will see a list of all variables in the `.env` and `.json` files in the specified directory. You can edit the value of a variable and click the "Save" button to save the changes.
