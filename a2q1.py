file = open("raw_text.txt", "r")
def encrypt(text, n, m):
    encrypted_text = ""

# Don't use char as variable name as char is also a function you will need to use
# Can use something like char_to_encrypt
for char_to_encrypt in text: 
        # If you structure your if statements like this, then you don't need to nest them.
        # if 'a' <= char <= 'm':
        # elif 'n' <= char <= 'z':
        # elif 'A' <= char <= 'M':
        # elif 'N' <= char <= 'Z':
        # else:
        #    new_char = char
        # Note: else is required because non-letter characters need to be retained e.g. spaces, full stops etc
        if 'a' <= char_to_encrypt <= 'z':
            if 'a' <= char <= 'm':
                new_char = char(ord(a) + ord(char_to_encrypt) - ord(a) + (n * m) ) % 26)
                # This one can be done with one line: new_char = char(ord(a) + (ord(char_to_encrypt) - ord(a) + (n * m)) % 26)
        else:
            new_char = ord(char_to_encrypt) + (n + m) 
            new_char = (new_char - ord('a')) % 26 + ord('a')
            # This one needs to shift backwards and there are two scenarios:
            # 1) The shift back stays within the range of a-z
            #        can be tested by ord(char_to_encrypt) - ord(a) - ((n + m) % 26) >= 0
            #        then calculated as new_char = char(ord(char_to_encrypt) - ((n + m) % 26))
            # 2) The shift back goes below the range of a-z (this would be the else to the above test)
            #        then calculated as new_char = char(ord(char_to_encrypt) + 26 - ((n + m) % 26))

# Below what I've been working on in visual studio. I added a raw_text.file to the same folder i put this in 
import string

def encrypt_char(c, n, m): # c is the text in the raw_text file.
 if c.islower():
  if c in string.ascii_lowercase[:13]:  # a-m
   return chr(((ord(c) - ord('a') + (n * m)) % 26) + ord('a'))
  else:  # n-z
   return chr(((ord(c) - ord('a') - (n + m)) % 26) + ord('a'))
    
 elif c.isupper():
  if c in string.ascii_uppercase[:13]:  # A-M
   return chr(((ord(c) - ord('A') - n) % 26) + ord('A'))
  else:  # N-Z
   return chr(((ord(c) - ord('A') + (m ** 2)) % 26) + ord('A'))
    
 return c  # Keep numbers and special characters unchanged

def decrypt_char(c, n, m):
  if c.islower():
   shift_forward = n * m
   shift_backward = n + m

   # Try reverse of a–m shift - I ended up just using a shift back to read it back because the maths wasn't working so it uses the else if to refer to after getting 2 false's
   possible = chr(((ord(c) - ord('a') - shift_forward) % 26) + ord('a'))
   if possible in string.ascii_lowercase[:13]:
    return possible
   else:
    return chr(((ord(c) - ord('a') + shift_backward) % 26) + ord('a'))

  elif c.isupper():
   shift_backward = n
   shift_forward = m ** 2

   # Try reverse of A–M shift
   possible = chr(((ord(c) - ord('A') + shift_backward) % 26) + ord('A'))
   if possible in string.ascii_uppercase[:13]:
    return possible
   else:
    return chr(((ord(c) - ord('A') - shift_forward) % 26) + ord('A'))

  return c  # Keep numbers and special characters unchanged


def encrypt_text(text, n, m):
 return ''.join(encrypt_char(c, n, m) for c in text)

def decrypt_text(text, n, m):
 return ''.join(decrypt_char(c, n, m) for c in text)

def check_correctness(original, decrypted):
 return original == decrypted

def process_files(n, m):
 with open("raw_text.txt", "r", encoding="utf-8") as infile:
  raw_text = infile.read()

 encrypted_text = encrypt_text(raw_text, n, m)
 with open("encrypted_text.txt", "w", encoding="utf-8") as outfile:
  outfile.write(encrypted_text)

 decrypted_text = decrypt_text(encrypted_text, n, m)

 with open("decrypted_text.txt", "w", encoding="utf-8") as outfile:
  outfile.write(decrypted_text)

 if check_correctness(raw_text, decrypted_text):
  print("Decryption successful! The decrypted text matches the original.")
 else:
  print("Decryption failed! The decrypted text does not match the original.")

# Example usage
n = int(input("Enter value for n: "))
m = int(input("Enter value for m: "))
process_files(n, m)
