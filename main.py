def main():
    result = []
    while True:
        start = input('Enter the starting letter: ')
        end = input('Enter the starting letter: ')
        if start.isalpha() and end.isalpha():
            startNum = ord(start)
            endNum = ord(end)
        else:
            print("Input must be a letter of the alphabet.")
            break

    print(*result)

    ########################################
    # Do not delete the return statement
    ########################################
    return result


if __name__ == '__main__':
    main()
