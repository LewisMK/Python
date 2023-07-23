# chr() gives the character match for a unicode value
# ord() gives the unicode value for a character

# Example

for ch in "abc":
    print(chr(ord(ch) + 1), end='')
    
 
 # will output "bcd" because;

    # chr(ord(x)) == x and ord(chr(x)) == x 