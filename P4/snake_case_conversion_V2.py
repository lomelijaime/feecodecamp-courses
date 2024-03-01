def convert_to_snake_case(pascal_or_camel_cased_string):
    # Using the python comprehension syntax to achieve the same result as the previous function
    #First, we create a list of characters, where each character is either the original character or a modified character
    snake_cased_char_list = [
        '_' + char.lower() if char.isupper()
        else char
        for char in pascal_or_camel_cased_string
    ]
    #Then, we join the list of characters into a single string, join will 
    return ''.join(snake_cased_char_list).strip('_')

def main():
    print(convert_to_snake_case('ThisIsAPascalCasedLargeString'))

    

if __name__ == '__main__':
    main()