def encrypt(letter, n):
    """
        This is help-function to encrypt a character
        -- input
            letter - Character which needs to be encrypted
            n - shift 
        -- output
            enc - encrypted character
    """
    enc = chr(ord(letter) + n)
    return enc


def decrypt(letter, n):
    """
        This is help-function to decrypt a character
        -- input
            letter - Character which needs to be decrypted
            n - shift 
        -- output
            dec - decrypted character
    """
    dec = chr(ord(letter) - n)
    return dec


def encrypt_sentence(sentence, shift):
    """
        This function helps to encrypt sentence
        -- input
            sentence - sentence which needs to be encrypted
            shift - shift of the character
        -- output
            encrypted sentence as string.
    """
    sentence = sentence.replace(" ", "{")

    encryptSent = ""
    for char in sentence:
        encryptSent += encrypt(char, shift)

    return encryptSent

 
def decrypt_sentence(sentence, shift):

    """
        This function helps to decrypt sentence
        -- input
            sentence - sentence which needs to be decrypted
            shift - shift of the character
        -- output
            decrypt sentence as string.
    """
    decryptSent = ""
    for char in sentence:
        decryptSent += decrypt(char, shift)

    decryptSent = decryptSent.replace("{", " ")
    return decryptSent



if __name__ == "__main__":
    sentence = "this is a secret message about the class "
    encryptSentence = encrypt_sentence(sentence, 5)
    print(sentence)
    print(encryptSentence)
    print(decrypt_sentence(encryptSentence, 5))
