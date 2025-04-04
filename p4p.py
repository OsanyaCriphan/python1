# File Read & Write Challenge 🖋️ and Error Handling Lab 🧪

def read_and_write_file():
    try:
        # Ask the user for the input filename
        input_filename = input("Enter the name of the file to read from: ")

        # Attempt to open the input file
        with open(input_filename, 'r') as input_file:
            # Read the file content
            content = input_file.read()

        # Modify the content (eg : convert to uppercase)
        modified_content = content.upper()

        #  output filename
        output_filename = input("Enter the name of the new file to write to: ")

        # change modified content to the new file
        with open(output_filename, 'w') as output_file:
            output_file.write(modified_content)

        print(f"File has been successfully modified and saved to '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        print(f"Error: Could not read or write to the file.")

# Run the program
read_and_write_file()
