# Define alphabet & cipher
alph = "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()"
cipher = "defghijklmnopqrstuvwxyzabc9876543210)(*&^%$#@!)"

#Determine Direction of Translation
io = input("Please type 'Decode' or 'Endcode' based on your need: ").lower()

# Receive message to be encoded
if io == "encode":
    output = "encoded"
    message = input("Enter the message to be encoded: ").lower()
    new_message = ""

    for char in message:
        if char in alph:
            # Find the index of the character in the alphabet
            index = alph.index(char)
            # Use the same index to get the corresponding cipher character
            new_message += cipher[index]
        else:
            # If the character is not in the alphabet, keep it as is
            new_message += char

# Receive message to be decoded
else:
    output = "decoded"
    message = input("Enter the message to be decoded: ").lower()
    new_message = ""

    for char in message:
        if char in cipher:
            # Find the index of the character in the cipher
            index = cipher.index(char)
            # Use the same index to get the corresponding cipher character
            new_message += alph[index]
        else:
            # If the character is not in the alphabet, keep it as is
            new_message += char



print("Please find your", output, "message below: \n", new_message)
