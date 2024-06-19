# the base path for my directory is C:\Users\MSHOME\Desktop\Newfolder\Python\PD_LAB
base_path = r"C:\Users\MSHOME\Desktop\Newfolder\Python\PD_LAB\\"

# @Author: Aditya Yedurkar
# @Date: 2023-11-18


def openfile():
    '''
    This function opens the file and returns the lines of the file.
    return: lines
    Exception: FileNotFoundError, PermissionError
    '''

    # to get input till the user enters a valid file name
    while True:

        # try catch to check for 1. file not found 2. permission error
        try:

            filename = input("Enter file name: ")
            path = base_path + filename

            # open the file in read mode
            with open(path, 'r') as f:
                lines = f.readlines()
            print("File opened successfully.")

            # return the lines of the file
            return lines

        # if file does not exist
        except (FileNotFoundError):
            print("Specified File not found at the given path. Please try again.")
        # if user does not have the required permission to access the file
        except (PermissionError):
            print(
                "You do not have the required permission to access this file. Please try again.")

        # catching other general exceptions
        except:
            print("An error occurred. Please try again.")


# function to check if the file is empty or not
def check_if_empty(content):
    '''
    This function checks if the file is empty or not.
    return: Output message
    '''
    # content is empty
    if len(content) == 0:
        return "File is empty."
    else:
        return "File is not empty."

# lenght of lines


def no_of_lines(lines):
    '''
    This function returns the number of lines in the file.
    return: number of lines
    '''
    # len of list of lines will be the number of lines in the file
    return len(lines)


def no_of_words(content):
    '''
    This function returns the number of words in the file.
    return: modified content
    '''
    # split the content by spaces and count the number of words
    # it will be list of words
    # output its length
    for i in content:
        # to ignore the new line characters
        # replace the new line character with space
        # so that the words split properly
        # we standardize the splitting criteria by replacing all the newlines with space
        if i == "\n":
            content = content.replace(i, " ")
    content = content.split(" ")
    return content


def no_of_characters(content):
    '''
    This function returns the number of characters in the file.
    return: number of characters
    '''
    # to ignore the whitespaces
    content = "".join(content.split(" "))

    # after removing whitespaces, length of the string will be the number of characters
    return len(content)


def no_of_unique_words(content):
    '''
    This function returns the number of unique words in the file.
    return: number of unique words
    '''
    # split the content by spaces and count the number of words
    total_words = no_of_words(content)

    # set will contain only unique words
    # set function in python is used to convert any of the iterable to sequence of iterable elements with distinct elements, commonly called Set.
    unique_words = set(total_words)

    # length of the set will be the number of unique words
    return unique_words


def five_most_frequent_words(content):
    '''
    This function returns the five most frequent words in the file.
    return: five most frequent words
    '''
    # a dictionary to store the frequency of each word
    # {key: value}
    # {word: frequency}
    word_freq = {}

    # generate list of words
    word_list = no_of_unique_words(content)

    # iterate over the list of words
    for word in word_list:

        # if the word is not present in the dictionary, add it with frequency 1
        if word not in word_freq:
            # initialize the frequency of the word to 1
            word_freq[word] = 1
        else:
            # if the word is already present in the dictionary, increment its frequency by 1
            word_freq[word] += 1

    # sort the dictionary by values in descending order and return the first 5 elements
    # slice operator is used to get the first 5 elements
    # sorted function is used to sort the dictionary by values
    # key is used to specify the key based on which the dictionary should be sorted
    # lambda is used to define an anonymous function
    # x is the parameter of the anonymous function
    # x[1] is the value of the dictionary
    # reverse is used to sort the dictionary in descending order
    return sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:5]


def five_least_frequent_words(content):
    '''
    This function returns the five least frequent words in the file.
    '''
    # a dictionary to store the frequency of each word
    # {key: value}
    # {word: frequency}
    word_freq = {}

    # generate list of words
    word_list = no_of_unique_words(content)

    # iterate over the list of words
    for word in word_list:

        # if the word is not present in the dictionary, add it with frequency 1
        if word not in word_freq:
            # initialize the frequency of the word to 1
            word_freq[word] = 1
        else:
            # if the word is already present in the dictionary, increment its frequency by 1
            word_freq[word] += 1

    # sort the dictionary by values in ascending order and return the first 5 elements
    # slice operator is used to get the first 5 elements
    # sorted function is used to sort the dictionary by values
    # key is used to specify the key based on which the dictionary should be sorted
    # lambda is used to define an anonymous function
    # x is the parameter of the anonymous function
    # x[1] is the value of the dictionary
    return sorted(word_freq.items(), key=lambda x: x[1])[:5]


def capitalize(lines):
    '''
    This function capitalizes the first and last letter of each line.
    '''
    capitalized_lines = []
    for line in lines:
        # reverse slicing is used to get the last character of the string

        # 1st-------<line>[start:stop:step]------------------last
        capitalized_line = line[0].upper() + line[1:-1] + line[-1].upper()
        capitalized_lines.append(capitalized_line)
    return capitalized_lines


def main():
    lines = openfile()  # Read the lines from the file

    # content is a string made by joining the line list together
    content = "".join(lines)

    print("lines: ", lines)
    print("content: ", content)

    while True:
        print("<------------------MENU------------------------------------------------------------------------------------------------------------------------------>")
        print("1. Check if file is empty.\n"
              "2. Number of lines in the file.\n"
              "3. Number of words in the file.\n"
              "4. Number of characters in the file.\n"
              "5. Number of unique words in the file.\n"
              "6. Five most frequent words in the file.\n"
              "7. Five least frequent words in the file.\n"
              "8. Capitalize the first and last letter of each line.\n"
              "9. Exit.")
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                print("File is empty: ", check_if_empty(content))
            elif choice == 2:
                print("Number of lines in the file: ", no_of_lines(lines))
            elif choice == 3:
                print("Number of words in the file: ",
                      len(no_of_words(content)))
            elif choice == 4:
                print("Number of characters in the file: ",
                      no_of_characters(content))
            elif choice == 5:
                print("Number of unique words in the file: ",
                      len(no_of_unique_words(content)))
            elif choice == 6:
                for word, freq in five_most_frequent_words(content):
                    print(word, ":", freq)
            elif choice == 7:
                for word, freq in five_least_frequent_words(content):
                    print(word, ":", freq)
            elif choice == 8:
                result = capitalize(lines)
                print("Capitalized lines: ")
                for line in result:
                    print(line)
            elif choice == 9:
                print("Exiting the program.")
                print("Thank you for using the program.")
                exit()
            else:
                print("Invalid choice. Please try again.")
        except (ValueError):
            print("Invalid choice. Please try again")
        # except:
        #     print("An error occurred. Please try again.")


if __name__ == "__main__":
    main()
