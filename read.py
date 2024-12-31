def read(location):
    with open(location,"r") as file:
        page=file.readlines()
        return [line.strip() for line in page]
location="example.txt"
print(read(location))