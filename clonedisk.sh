#!/bin/bash
# Diyar Parwana
# It is important to clone the disk multiple times.. and be sure to follow the instructions...
# Prompt the user for the source drive path
read -p "Enter the source drive path (e.g., /dev/sdX): " source_drive
if [ ! -b "$source_drive" ]; then
    echo "Source drive not found or invalid. Exiting."
    exit 1
fi

# Prompt the user for the destination drive path
read -p "Enter the destination drive path (e.g., /dev/sdY): " destination_drive
if [ ! -b "$destination_drive" ]; then
    echo "Destination drive not found or invalid. Exiting."
    exit 1
fi

# Display information about the operation
echo "This will clone the contents of $source_drive to $destination_drive."
echo "Please make sure you have the correct source and destination drives."
read -p "Do you want to continue? (Y/N): " confirmation

# Check user's confirmation
if [ "$confirmation" != "Y" ] && [ "$confirmation" != "y" ]; then
    echo "Operation canceled."
    exit 0
fi

# Clone the source drive to the destination drive using dd
sudo dd if="$source_drive" of="$destination_drive" bs=4M status=progress

# Verify if the operation was successful
if [ "$?" -eq 0 ]; then
    echo "Drive cloning completed successfully."
else
    echo "Drive cloning encountered an error."
fi
