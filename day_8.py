from alphabet import alphabet

def cesar(text, shift, direction):
    shifted_text = []
    for i in text:
        if ord(i) >= 97 and ord(i) <= 122:
            z = alphabet.index(i)
            if direction == 'encode':
                shifted_text.append(alphabet[((z + shift) % (len(alphabet)))])
            else:
                shifted_text.append(alphabet[((z - shift + len(alphabet)) % (len(alphabet)))])
        else:
            shifted_text.append(i)
    return shifted_text

want_continue = True
while want_continue == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    print(cesar(text, shift, direction))
    decision = input("type 'yes' if you want to canotinue").lower()
    if decision != "yes":
        want_continue = False
