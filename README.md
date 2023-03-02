# DailyItemRemover-Grocy - Setting up a daily cronjob for automatic product removal in grocy
## Purpose

This Python script allows you to automatically remove one or more products from your grocy instance every day. You can set up a daily cronjob to run the script at a specific time.
Requirements

* A grocy instance with API access enabled
* Python 3.x installed on your system
* A text editor or IDE to edit the script
* Basic knowledge of the command line

## Setting up a virtual environment with requirements.txt

To ensure that you have all the necessary dependencies for the script, it's recommended to set up a virtual environment with the requirements.txt file included in the repository. Here are the steps to set up the virtual environment:

Open your terminal or command prompt and navigate to the directory containing the script and the requirements.txt file.

Run the following command to create a new virtual environment:

```bash

python3 -m venv env
```

This will create a new directory called env with the virtual environment files.

Activate the virtual environment by running the following command:

```bash

source env/bin/activate
```
Install the required dependencies by running the following command:

```
pip install -r requirements.txt
```

Now you can run the script from within the virtual environment by navigating to the directory containing the script and running the following command:

```
python3 script.py
```

Make sure to activate the virtual environment every time you want to run the script. To deactivate the virtual environment, run the following command:
```
deactivate
```

## Usage

Edit the settings.json file to add your grocy URL, API key, and the product IDs you want to remove. (Make a copy from settings.json.example)
  
Open your terminal or command prompt and navigate to the directory containing the script and the settings.json file.  
  
Use the following command to edit your crontab file:  
```
crontab -e
```
Add a new line to the crontab file with the following format:

```ruby

* * * * * /path/to/venv/python3 /path/to/script.py
```

Replace /path/to/script.py with the actual path to the Python script on your system and /path/to/venv/python3 with the actual path to the python binary in your venv.

This command will run the script every minute. To run the script at a specific time every day, you can modify the command as follows:

```ruby

    0 12 * * * /path/to/venv/bin/python3 /path/to/script.py
```

This command will run the script at 12:00 PM (noon) every day. You can modify the time to suit your needs.

Save and exit the crontab file.

The cronjob is now set up to run the script automatically every day at the specified time. The script will remove the specified products from your grocy instance if they are in stock.

## Troubleshooting

If the cronjob is not running as expected, you can check the system logs to see if there are any errors. You can also test the script manually by running it from the command line.
