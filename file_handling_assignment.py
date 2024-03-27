try:
    # File Creation
    with open("my_file.txt", "w") as file:
        file.write("This is line 1\n")
        file.write("2nd line with numbers: 12345\n")
        file.write("Line 3: Python file handling\n")
    
    # File Reading and Display
    print("Contents of 'my_file.txt':")
    with open("my_file.txt", "r") as file:
        content = file.read()
        print(content)
    
    # File Appending
    with open("my_file.txt", "a") as file:
        file.write("Appending line 1\n")
        file.write("Appending line 2\n")
        file.write("Appending line 3\n")

except FileNotFoundError:
    print("Error: File not found.")
except PermissionError:
    print("Error: Permission denied.")
except Exception as e:
    print("An error occurred:", e)
finally:
    print("File handling completed.")
