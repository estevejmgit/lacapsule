data = [ "ordre", "donner", "roder", "recevoir", "dorer", "plaisir", "aaaaa"]

def list_anagrams(data = data):
    anagrams = []
    origin_word = "ordre"
    
    # Insert your code here
    for word in data:
        if ''.join(sorted(word)) == ''.join(sorted(origin_word)):
            anagrams.append(word)
    
    # End of code insertion
    
    return anagrams
    
print(list_anagrams(data))


# string = "python"
# # return a string
# sorted_string = ''.join(sorted(string))
# # return a list
# simple_sort = sorted(string)

# print(sorted_string)
# print(simple_sort)