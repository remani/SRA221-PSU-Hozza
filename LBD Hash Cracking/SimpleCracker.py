# Simple script to crack lowercase MD5 password hashes
# Brant Goings

# Library needed to hash dictionary file
import hashlib

# Files to import
hashlist = "hashes.txt"
dictlist = "dictionary.txt"

# Method to run
def crack():
    # Opens dictionary file as read-only referred to as dictreader
    with open(dictlist, "r") as dictreader:
        try:
            # Starts for loop in dictreader
            for dictline in dictreader:
                # Opens hash file as read-only referred to as hashreader
                with open(hashlist, "r") as hashreader:
                    # Starts nested for loop in hashreader
                    for hashline in hashreader:

# ------------------------------------------------------------ BEGIN SUPER IMPORTANT PART ------------------------------------------------------------ #
                        # If statement compares the hashed version of the password in dictionary.txt with the hash in hashes.txt
                        if hashlib.md5(dictline.rstrip().encode()).hexdigest() == hashline.rstrip():
                            # If they match, print the hash and the line in dictionary.txt we're currently at
                            print("MD5 hash cracked -- " + hashline.rstrip() + " : " + dictline)
                        # If they're not the same, continue without doing anything
                        else:
                            pass
# ------------------------------------------------------------ END SUPER IMPORTANT PART ------------------------------------------------------------ #

        except:
            pass

# Spaces the output for readability
print("\n")
# Run the script
crack()
