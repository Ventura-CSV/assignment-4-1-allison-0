def main():
    result = []
    while True:
        start = input('Enter the starting letter: ')
        end = input('Enter the starting letter: ')
        if start.isalpha() and end.isalpha(): # Check if inputs are letters in the alphabet
            startNum = ord(start)
            endNum = (ord(end) + 1)
            if startNum < endNum: # Check if num representing start input is less than num representing end
                for i in range(startNum,endNum):
                    result.append(chr(i))
                else:
                    break
            else:
                print("Start must be less than end.")
                break
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
