import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 read_set_file.py <filename>")
        return
    
    filename = sys.argv[1]

    with open(filename, "rb") as f:
        data = f.read()

    text = data.decode("utf-8")
    lines = text.splitlines()

    for line in lines:
        parts = line.split(";")

        if parts[0] == "SET":
            set_id = parts[1]
            name = parts[2]
            year = parts[3]
            category = parts[4]

            print(f"Set ID: {set_id}")
            print(f"Name: {name}")
            print(f"Year: {year}")
            print(f"Category: {category}")
            print()
            print("Inventory:")

        elif parts[0] == "BRICK":
            brick_type_id = parts[1]
            color_id = parts[2]
            count = parts[3]

            print(f"  Brick type: {brick_type_id}, Color: {color_id}, Count: {count}")

if __name__ == "__main__":
    main()