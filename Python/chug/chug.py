# Chug
#
# Chug is a symmetric encryption algorithm in which
# the key is calculated from a known plaintext and
# a known ciphertext.
#
# Author       :   https://github.com/sblmnl
# Date Created :   2020-12-05 (YYYY-MM-DD)
# License      :   MIT
#
# [!* Disclaimer *!]
# I am not a professional cryptographer, therefore
# it is advised that you do not rely on the
# security of this algorithm for any information.
# I am not liable for any damage caused by the use
# of this cipher. Use this cipher at your own risk!

import struct

class Chug:
    @staticmethod
    def create_key(plaintext: bytes, ciphertext: bytes):
        if (plaintext == None):
            raise ValueError("You must specify the plaintext!")

        if (ciphertext == None):
            raise ValueError("You must specify the ciphertext!")

        if (type(plaintext) != bytes):
            raise TypeError("The plaintext must be bytes!")

        if (type(ciphertext) != bytes):
            raise TypeError("The ciphertext must be bytes!")

        key = bytearray(len(plaintext) * 4)

        for i in range(0, len(plaintext)):
            value = plaintext[i]

            for j in range(0, len(ciphertext)):
                if (ciphertext[j] == 0):
                    continue

                operation = j % 4

                if (operation == 0):
                    value += ciphertext[j]
                elif (operation == 1):
                    value -= ciphertext[j]
                elif (operation == 2):
                    value *= ciphertext[j]
                elif (operation == 3):
                    value /= ciphertext[j]

            value = struct.pack(">f", value)

            for j in range(0, 4):
                key[j + (i * 4)] = value[j]

        return bytes(key)

    @staticmethod
    def decrypt(ciphertext: bytes, key: bytes):
        if (ciphertext == None):
            raise ValueError("You must specify the ciphertext!")

        if (key == None):
            raise ValueError("You must specify the key!")

        if (type(ciphertext) != bytes):
            raise TypeError("The ciphertext must be bytes!")

        if (type(key) != bytes):
            raise TypeError("The key must be bytes!")

        plaintext = bytearray(int(len(key) / 4))

        for i in range(0, len(key), 4):
            value = struct.unpack(">f", key[i:i + 4])[0]

            for j in range((len(ciphertext) - 1), -1, -1):
                if (ciphertext[j] == 0):
                    continue

                operation = j % 4

                if (operation == 0):
                    value -= ciphertext[j]
                elif (operation == 1):
                    value += ciphertext[j]
                elif (operation == 2):
                    value /= ciphertext[j]
                elif (operation == 3):
                    value *= ciphertext[j]

            plaintext[int(i / 4)] = round(value)

        return bytes(plaintext)
