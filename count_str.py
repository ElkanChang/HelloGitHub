#!/usr/bin/env python3

def char_count(str):
    #char_list = set(str)
    #print(char_list)
    #for char in char_list:
    #    print(char, str.count(char))
    
    # reduce loop. more efficient
    char_dict = {}
    for char in str:
        if char_dict.get(char):
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    print(char_dict)

if __name__ == '__main__':
    s = input("Enter a string:")
    char_count(s)
