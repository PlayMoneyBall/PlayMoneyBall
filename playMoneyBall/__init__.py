def reader():
    with open("./data/211028.csv", 'r') as file:
        line = file.read()
        print(line ,"---> ")
        print(line.split(",")," <---")


if __name__ == "__main__":
    reader()
