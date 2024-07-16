# Create a str that contains "The!quick!brown!fox!jumps!over!the!lazy!dog."
sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog."

# Use replace() function to replace every "!" with a blank space, then print the string
sentence = sentence.replace("!", " ")
print("sentence.replace(""!"", " "): {}".format(sentence)) 

# Use upper() function to print the str all in capital letters
sentence = sentence.upper()
print(f"sentence.upper: {sentence}")

# Use len() function to find out string length
# Use indexing to reverse print the string

# Print(f"sentence.len: {len(sentence)}") # sentence length is 44
print(f"sentence.reverse: {sentence[44: : -1]}")
