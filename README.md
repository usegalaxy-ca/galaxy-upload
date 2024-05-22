# galaxy-upload
Simple program to assist in uploading files UseGalaxy.ca

# install
- virtualenv venv
- pip install bioblend

# Usage
```
galaxy-upload key=<your Galaxy API key> histid=<History ID> filepath=<Full path name of the file to upload>
```

- If you omit your Galaxy API key you will be promped to provide it. 

- If you omit the <History ID> the program will give you the list of your histories you can choose from

- If you omit the filepath you will be able to navigate trough your directories and select the file
