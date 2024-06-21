# galaxy-upload
Simple program to assist in uploading files to any Galaxy instances (default is https://usegalaxy.ca). You
will need to generate a secret key in your Galaxy account under "User/Preferences/Manage API Key".

# install
- virtualenv venv
- pip install bioblend

# Usage
```
python3 galaxy-upload.py galaxy_url=<Galaxy URL> key=<your Galaxy API key> histid=<History ID> filepath=<Full path name of the file to upload>
```

- If you omit the Galaxy URL the default will be https://usegalaxy.ca

- If you omit your Galaxy API secret key you will be promped to provide it. 

- If you omit the <History ID> the program will give you the list of your histories you can choose from

- If you omit the filepath you will be able to navigate trough your directories and select the file
