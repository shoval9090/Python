class Cipher:
    """
       encrypt: abcz -> cdeb
       decrypt: cdeb -> abcz
       """
    """
    private static int default_shift = 2
    private static int alphabet_length = 26
    private encrypted
    this.encrypted = textToEncrypt
    """
    default_shift = 2
    alphabet_length = 26

    def __init__(self, textToEncrypt: str, shift=2):
        # instance data members
        self.encrypted = textToEncrypt

    @staticmethod
    def get_string(text):
        if isinstance(text, str):
            return text

    @staticmethod
    def input_user():
        original_text = input("Please enter the text to encrypt: ")
        return original_text


if __name__ == '__main__':
    my_text = Cipher.input_user()

