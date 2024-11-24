import os

def find_missing_files(source_folder, destination_folder):
    """Find and return the list of missing files with their paths from the source folder compared to the destination folder."""
    missing_files = []

    # Walk through the source folder and check against the destination
    for root, _, files in os.walk(source_folder):
        for file in files:
            # Construct the source file path and its corresponding destination file path
            source_file_path = os.path.join(root, file)
            # Create the relative path for the destination comparison
            relative_path = os.path.relpath(source_file_path, source_folder)
            destination_file_path = os.path.join(destination_folder, relative_path)

            # Check if the file exists in the destination folder
            if not os.path.exists(destination_file_path):
                missing_files.append(source_file_path)  # Store the source file path of the missing file

    return missing_files

def write_missing_files_to_file(missing_files, output_folder, output_filename):
    """Write the list of missing files with their locations to the specified output text file."""
    # Ensure the output directory exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    output_file_path = os.path.join(output_folder, output_filename)
    
    with open(output_file_path, 'w') as file:
        if missing_files:
            file.write("Missing files in the destination folder:\n")
            for missing_file in missing_files:
                file.write(f"{missing_file}\n")
        else:
            file.write("All files from the source folder are present in the destination folder.\n")

def main():
    # Get user input for the source and destination folders
    source_folder = input("Enter the path of the source folder: ").strip()
    destination_folder = input("Enter the path of the destination folder: ").strip()
    
    # Get user input for the output folder and output text file name
    output_folder = input("Enter the path of the output folder: ").strip()
    output_filename = input("Enter the name of the output text file (e.g., missing_files.txt): ").strip()

    # Find missing files
    missing_files = find_missing_files(source_folder, destination_folder)

    # Write missing files to the output text file
    write_missing_files_to_file(missing_files, output_folder, output_filename)

    print(f"Missing files have been written to '{os.path.join(output_folder, output_filename)}'.")

if __name__ == "__main__":
    main()