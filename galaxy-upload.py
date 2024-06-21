#!/usr/bin/env python3

import sys,os,json

from bioblend.galaxy import GalaxyInstance

def parse_parameters(arguments):
  parameters = {}
  for arg in arguments:
    try:
      key, value = arg.split('=')
      parameters[key] = value
    except ValueError:  # Not in the format "key=value"
      print(f"Invalid argument format: {arg}. Skipping.")
  return parameters

def select_dest_history(gi,selected_destination_hist_id):

    histories=gi.histories.get_histories()

    if selected_destination_hist_id==None:
        for i, hist in enumerate(histories, start=1):
            print(f"{i} : {hist['id']} : \"{hist['name']}\"")
        hist_choice = input("\nEnter the number corresponding to the destination history: ")
        selected_history=histories[int(hist_choice)-1]
    else:
        for hist in histories:
            if hist['id']== selected_destination_hist_id:
                selected_history=hist

    return selected_history


def select_file(provided_file_to_upload):

    if provided_file_to_upload!=None:
        if os.path.isfile(provided_file_to_upload):
            return provided_file_to_upload
        else:
            print("ERROR: File provided is not a file !!!")
            exit()

    startpath = os.getcwd()  # Start at the current directory
    while True:
        print("\nCurrent directory:", os.path.abspath(startpath))
        print("Contents:")
        items = os.listdir(startpath)
        for i, item in enumerate(items, start=1):
            full_path = os.path.join(startpath, item)
            if os.path.isdir(full_path):
                print(f"  {i}. {item}/")
            else:
                print(f"  {i}. {item}")

        user_choice = input("\nEnter a number to select an item (or '../' to go up, or 'q' to quit): ")
        if user_choice.lower() == 'q':
            break
        elif user_choice == '..':
            startpath = os.path.dirname(startpath)  # Move up one level
        else:
            try:
                selected_index = int(user_choice) - 1
                selected_item = items[selected_index]
                new_path = os.path.join(startpath, selected_item)
                if os.path.isdir(new_path):
                    startpath = new_path
                else:
                    selected_file=new_path
                    break
            except (ValueError, IndexError):
                print("Invalid input. Please enter a valid number or '../'.")

    return selected_file

if __name__ == "__main__":

    params = parse_parameters(sys.argv[1:])

    if 'key' not in params:
        user_key = input("\nPlease provide your access secret key to access your UseGalaxy.ca account: ")
    else:
        user_key=params['key']

    if 'galaxyurl' not in params:
        galaxy_url='https://usegalaxy.ca'
    else:
        galaxy_url=params['galaxyurl']

    if 'histid' not in params:
        histid = None
    else:
        histid=params['histid']

    if 'filepath' not in params:
        filepath = None
    else:
        filepath=params['filepath']

    gi = GalaxyInstance(url=galaxy_url, key=user_key )

    selected_destination_hist = select_dest_history(gi,histid)

    selected_file_to_upload = select_file(filepath)

    print("\n====================================================================\n")

    print(f"Galaxy URL where to upload file : {galaxy_url}")
    print(f"File selected to upload         : {selected_file_to_upload}")
    print(f"Destination history selected    : {selected_destination_hist['name']}")

    user_choice = input("\nPlease confirm the operation ('y' or 'n'): ")
    if user_choice.lower() == 'y':
        gi.tools.upload_file(selected_file_to_upload,selected_destination_hist['id'])
    else:
        exit()
