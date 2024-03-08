# galaxy-upload
Simple program to assist in uploading files UseGalaxy.ca

# install
virtualenv venv
pip install bioblend

# Usage

galaxy-upload key=<your personal Galaxy API key\> histid=<History ID\> filepath=<Full path name of the file to upload\>

- If you omit your secret ket you will be promped to provide the information. 

- If the histid is not provided the program will give you the list of your histories you can choose from

- If the filepath is not provided you will be able to navigate trough your directories and select the file
