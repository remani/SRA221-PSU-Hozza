# Simple script to crack password hashes. Very limited input/output

import hashlib

hashlist = "hashes.txt"
dictlist = "dictionary.txt"

# Method to run
def crack():
    # Opens the dictionary file
    with open(dictlist, "r") as dictreader:
        try:
            # Starts for loop
            for dictline in dictreader:
                # Opens hash file
                with open(hashlist, "r") as hashreader:
                    # Starts nested for loop
                    for hashline in hashreader:
                        # If statement compares the hashed version of the password in dictionary.txt with the hash in hashes.txt
                        if hashlib.md5(dictline.rstrip().encode()).hexdigest().lower() == hashline.rstrip().lower():
                            # If they match, print the hash and the line in dictionary.txt we're currently at
                            print("MD5 hash cracked -- " + hashline.lower().rstrip() + " : " + dictline)
                        else:
                            # If they're not the same, don't do anything
                            pass
        except:
            pass

print("\n")
# Run the script
crack()
