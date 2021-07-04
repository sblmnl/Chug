// Chug
//
// Chug is a symmetric encryption algorithm in which
// the key is calculated from a known plaintext and
// a known ciphertext.
//
// Author       :   https://github.com/sblmnl
// Date Created :   2020-12-05 (YYYY-MM-DD)
// License      :   MIT
//
// [!* Disclaimer *!]
// I am not a professional cryptographer, therefore
// it is advised that you do not rely on the
// security of this algorithm for any information.
// I am not liable for any damage caused by the use
// of this cipher. Use this cipher at your own risk!

using System;

public static class Chug
{
    public static byte[] CreateKey(byte[] plaintext, byte[] ciphertext)
    {
        if (plaintext == null) throw new ArgumentNullException(nameof(plaintext), "You must specify the plaintext!");
        if (ciphertext == null) throw new ArgumentNullException(nameof(ciphertext), "You must specify the ciphertext!");

        byte[] key = new byte[plaintext.Length * 4];

        for (int i = 0; i < plaintext.Length; i++)
        {
            float value = plaintext[i];

            for (int j = 0; j < ciphertext.Length; j++)
            {
                if (ciphertext[j] == 0) continue;

                switch (j % 4)
                {
                    case 0:
                        value += ciphertext[j];
                        break;
                    case 1:
                        value -= ciphertext[j];
                        break;
                    case 2:
                        value *= ciphertext[j];
                        break;
                    case 3:
                        value /= ciphertext[j];
                        break;
                }
            }

            byte[] buffer = BitConverter.GetBytes(value);
            if (BitConverter.IsLittleEndian)
                Array.Reverse(buffer);

            Buffer.BlockCopy(buffer, 0, key, i * 4, 4);
        }

        return key;
    }

    public static byte[] Decrypt(byte[] ciphertext, byte[] key)
    {
        if (ciphertext == null) throw new ArgumentNullException(nameof(ciphertext), "You must specify the ciphertext!");
        if (key == null) throw new ArgumentNullException(nameof(key), "You must specify the key!");

        byte[] plaintext = new byte[key.Length / 4];

        for (int i = 0; i < key.Length; i += 4)
        {
            byte[] buffer = new byte[4];
            Buffer.BlockCopy(key, i, buffer, 0, 4);
            if (BitConverter.IsLittleEndian)
                Array.Reverse(buffer);

            float value = BitConverter.ToSingle(buffer, 0);

            for (int j = ciphertext.Length - 1; j >= 0; j--)
            {
                if (ciphertext[j] == 0) continue;

                switch (j % 4)
                {
                    case 0:
                        value -= ciphertext[j];
                        break;
                    case 1:
                        value += ciphertext[j];
                        break;
                    case 2:
                        value /= ciphertext[j];
                        break;
                    case 3:
                        value *= ciphertext[j];
                        break;
                }
            }

            plaintext[i / 4] = (byte)value;
        }

        return plaintext;
    }
}