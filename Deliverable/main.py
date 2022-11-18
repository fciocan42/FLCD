from Deliverable.Scanner import Scanner


if __name__ == '__main__':
    file_name = input("filename: ")

    scanner = Scanner(file_name, "out/Output.txt", "out/PIF.txt", "out/ST.txt")
    scanner.scan()
