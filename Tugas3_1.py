def main():
    with open("indata.txt", "r") as file:
        numbers = [int(line.strip()) for line in file]

    total = sum(numbers)

    print("{:,.2f}".format(total))

if __name__ == "__main__":
    main()