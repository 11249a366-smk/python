def main():
    filename = input("Enter the filename: ")
    file = open(filename, 'r')
    N = int(input("Enter number of lines to display: "))

    print(f"\nFirst {N} lines of the file:")
    for i in range(N):
        line = file.readline()
        if line == '':
            print("End of file reached.")
            break
        print(line.strip())
    file.close()

    word = input("\nEnter the word to find its frequency: ").lower()
    file = open(filename, 'r')
    content = file.read().lower()
    frequency = content.count(word)
    file.close()

    print(f"\nThe word '{word}' occurred {frequency} times in the file.")

main()
