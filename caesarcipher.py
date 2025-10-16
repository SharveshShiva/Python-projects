import art
print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def caesar(encode_or_decode, original_text, shift_amount):
    index = 0
    cipher_text = []

    if encode_or_decode == "decode":
        shift_amount = shift_amount*-1

    for i in original_text:
        if i in alphabet:
            index = alphabet.index(i)
            index = shift_amount + index
            index = index % len(alphabet)  # 3 % 25 = 3 -- index more than the range of alphabet is maintained within the range of the alphabet list.
            cipher_text.append(alphabet[index])
        if i not in alphabet:
            cipher_text.append(i)

    print(f"Here is the {encode_or_decode}d result:", "".join(cipher_text))

should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(encode_or_decode=direction, original_text=text, shift_amount=shift)

    Yes_or_no = input("Type yes to restart the program and no to exit the program: ")
    if Yes_or_no == "no":
        should_continue = False
        print("Its Over..")

