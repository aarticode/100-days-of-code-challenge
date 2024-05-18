#Python program that translates a message into secret code language and can decode it based on the rules you provided.
#The program asks whether you want to encode or decode the message:

import random
import string

def encode_message(message):
    secret_code = ""
    for word in message.split():
        if len(word) >= 3:
            # Remove the first letter and append it at the end
            modified_word = word[1:] + word[0]
            # Append three random characters at the start and end
            random_chars = ''.join(random.choices(string.ascii_lowercase, k=3))
            secret_code += random_chars + modified_word + random_chars + ' '
        else:
            # Simply reverse the string
            secret_code += word[::-1] + ' '
    return secret_code.strip()

def decode_message(secret_code):
    decoded_message = ""
    for word in secret_code.split():
        if len(word) < 3:
            # Reverse the string
            decoded_message += word[::-1] + ' '
        else:
            # Remove 3 random characters from start and end
            trimmed_word = word[3:-3]
            # Remove the last letter and append it to the beginning
            decoded_word = word[-1] + trimmed_word
            decoded_message += decoded_word + ' '
    return decoded_message.strip()

def main():
    choice = input("Do you want to code (encode) or decode the message? (code/decode): ").lower()
    if choice == "code":
        message = input("Enter your message: ")
        encoded_message = encode_message(message)
        print("Secret code:", encoded_message)
    elif choice == "decode":
        secret_code = input("Enter the secret code: ")
        decoded_message = decode_message(secret_code)
        print("Decoded message:", decoded_message)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
