#!/bin/sh


# Check if at least one argument was provided
if [ "$#" -eq 0 ]; then
    echo "Usage: $0 <folder_name>"
    exit 1
fi



echo "Type your folder name project:"
read folder_name_project

FOLDER_NAME_PROJECT="$folder_name_project"

# Check if the folder already exists
if [ ! -d "$FOLDER_NAME_PROJECT" ]; then
    # If the folder doesn't exist, create it
    mkdir "$FOLDER_NAME_PROJECT"
    echo "Folder '$FOLDER_NAME_PROJECT' created successfully."
else
    # If the folder already exists, display a message
    echo "Folder '$FOLDER_NAME_PROJECT' already exists."
fi





# function is_value_passed() {
#     echo "Creating a new project with the name: ${1}!"

#     if [ ! -d "$1" ]; then
#         # If the folder doesn't exist, create it
#         mkdir "$1"
#         echo "Folder '$1' created successfully."
#     else
#         # If the folder already exists, display a message
#         echo "Folder '$1' already exists."
#     fi


# }

# my_function

