liste = ["bonjour", "kayak", "salut", "ressasser", "toto", "python", "été", "algo"]

def is_palindrome(liste = liste):
    palindromes = []
    
    # Insert your code here
    for word in liste:
        
        if word == word[::-1]:
            palindromes.append(word)
    
    if len(palindromes) == 0:
        return False    
    # End of code insertion
    
    return palindromes

print(is_palindrome(liste))