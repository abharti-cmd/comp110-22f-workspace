"""An example of a list utility algorithm"""

 # Name: contains 
 # Functions with 2 parameters: 
 # needle - what we're searching for 
 # haystack - what we're searching through 
 # Return type: bool
def contains(needle: str, haystack: list[str]) -> bool: 
 # Start from first index
 int: int = 0
 # Loop through each index of list
 while i < len(haystack): 
    #  Test, if the item at this index is equal to needlde
    if haystack[1] == needle:
    #      #Yes! Return True
        return True 
    i += 1
 #Return False
 return False 