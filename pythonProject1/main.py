import os

def check_lines_present(lines, search_lines):
    if len(lines) < 2:
        return False

    return lines[0].strip() == search_lines[0] or lines[1].strip() == search_lines[1]

search_lines = ["Hello, how are you?", "What are you doing?"]
directory = "C:/Users/periy/Desktop"  # Update with the directory path where your SQL files are located

for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        filepath = os.path.join(directory, filename)
        with open(filepath, "r") as file:
            lines = file.readlines()

        if not check_lines_present(lines[:2], search_lines):
            if lines[0].strip() == search_lines[0] or lines[0].strip() == search_lines[1]:
                if lines[0].strip() == search_lines[0]:
                    with open(filepath, "w") as file:
                        file.seek(1)
                        file.write("\n" + search_lines[1] + "\n" + "".join(lines))
                        print(f"{filename}: one line added.")
                elif lines[0].strip() == search_lines[1]:
                    with open(filepath, "w") as file:
                        file.seek(0)
                        file.write(search_lines[0] + "\n")
                        file.seek(2)
                        file.write("".join(lines))
                        print(f"{filename}: one line added.")
                with open(filepath, "w") as file:
                    file.write(search_lines[0] + "\n" + search_lines[1] + "\n")
                    print(f"{filename}: one line added.")
            elif len(lines) == 1 and (lines[0].strip() == search_lines[0] or lines[0].strip() == search_lines[1]):
                if lines[0].strip() == search_lines[0]:
                    with open(filepath, "w") as file:
                        file.seek(1)
                        file.write("\n" + search_lines[1] + "\n" + "".join(lines))
                        print(f"{filename}: one line added.")
                elif lines[0].strip() == search_lines[1]:
                    with open(filepath, "w") as file:
                        file.seek(0)
                        file.write(search_lines[0] + "\n")
                        file.seek(2)
                        file.write("".join(lines))
                        print(f"{filename}: one line added.")




                with open(filepath, "w") as file:
                    file.write(search_lines[0] + "\n" + search_lines[1] + "\n" + "".join(lines))
                    print(f"{filename}: Search lines added.")

        else:
            if lines[0].strip() == search_lines[0] and lines[1].strip() == search_lines[1]:
                print(f"{filename}: Found search lines, no changes made.")
            elif lines[0].strip() == search_lines[0]:
                with open(filepath, "w") as file:
                    file.seek(1)
                    file.write("\n" + search_lines[1] + "\n" + "".join(lines))
                    print(f"{filename}: one line added.")
            elif lines[0].strip() == search_lines[1]:
                with open(filepath, "w") as file:
                    file.seek(0)
                    file.write(search_lines[0] + "\n")
                    file.seek(2)
                    file.write("".join(lines))
                    print(f"{filename}: one line added.")

            print(f"{filename}: Found search lines, no changes made.")
