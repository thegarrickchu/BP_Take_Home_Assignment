#import all necessary libraries, in this case just arg parse is needed so the script can be run with arguments from CLI

import argparse

#parses the arguments passed on the CLI when invoking this script
parser = argparse.ArgumentParser()
parser.add_argument("string1", help="first string to evaluate",
                     type=str)
parser.add_argument("string2", help="second string to evaluate",
                     type=str)

args = parser.parse_args()

def longest_common_subsequence(str1: "string", str2: "string"):
    #get length of each string
    m = len(str1)
    n = len(str2)
    
    """instantiate a 2-D array to store the results of evaluating/storing character evaluations. 
    Basically, this will be a table with each row and column being an element of the string and the fields will be the running length count of the longest common substring.
    We will use this array as well as a pointer to identify the associated elements of the string.
    here we'll use list comprehension to generate.
    """
    length_lcs = [[0 for x in range(n+1)] for x in range(m+1)] 
    
    
    #Now we'll build/fill in the values of length_lcs[m+1][n+1] using a "bottom-up" approach
    for i in range(m+1):
        for j in range(n+1):
            #starting logic in iterating through the 2-d array length_lcs
            if i == 0 or j == 0:
                length_lcs[i][j] = 0
            elif str1[i-1] == str2[j-1]: #case when there is a element match, increment the previous length_lcs by 1
                length_lcs[i][j] = length_lcs[i-1][j-1] + 1
            else: # the case where there is no match
                length_lcs[i][j] = max(length_lcs[i-1][j], length_lcs[i][j-1])
    
    """
    At this point we have a 2-d array with values that consists of either 0, an intermediate running count of the longest common subsequence or the final count of the longest common subsequence
    Now let's use these values to access via indexing the actual elements of the string
    """
    
    #instantiate the pointer for indexing
    pointer = length_lcs[m][n]
    
    #instantiate an array with length of the longest common subsequence to store the common elements
    lcs = [""] * (pointer+1)
    
    #copy lengths of strings so they can be incremented for below while loop
    p, q = m, n
    
    while p > 0 and q > 0:
        if str1[p-1] == str2[q-1]: #if the str1 char matches the str2 character, then it is part of the longest common subsequence
            lcs[pointer-1] = str1[p-1]
            #increment index and pointer to work through the remaining 2-d array
            p -= 1
            q -= 1
            pointer -= 1
            
        #if not the same, find the larger value of 2 adjacent elements of 2-d array, length_lcs and return corresponding element. This prevents double entry of the matching elements
        elif length_lcs[p-1][q] > length_lcs[p][q-1]:
            p -= 1
        else:
            q -= 1
            
    
    print("The longest common subsequence is '{}' and is of length {}".format("".join(lcs), length_lcs[m][n]))

    
if __name__ == "__main__":
    longest_common_subsequence(args.string1, args.string2)