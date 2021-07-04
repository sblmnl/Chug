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

const Chug = {
    createKey: function(plaintext, ciphertext) {
        if (plaintext === undefined || plaintext === null) throw new Error("You must specify the plaintext!");
        if (ciphertext === undefined || ciphertext === null) throw new Error("You must specify the ciphertext!");
        if (!plaintext instanceof Buffer) throw new TypeError("The plaintext must be a buffer!");
        if (!ciphertext instanceof Buffer) throw new TypeError("The ciphertext must be a buffer!");

        let key = Buffer.alloc(plaintext.length * 4);

        for (let i = 0; i < plaintext.length; i++) {
            let value = plaintext[i];

            for (let j = 0; j < ciphertext.length; j++) {
                if (ciphertext[j] === 0) continue;

                switch (j % 4) {
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

            key.writeFloatBE(value, i * 4);
        }

        return key;
    },
    decrypt: function(ciphertext, key) {
        if (ciphertext === undefined || ciphertext === null) throw new Error("You must specify the ciphertext!");
        if (key === undefined || key === null) throw new Error("You must specify the key!");
        if (!ciphertext instanceof Buffer) throw new TypeError("The ciphertext must be a buffer!");
        if (!key instanceof Buffer) throw new TypeError("The key must be a buffer!");

        let plaintext = Buffer.alloc(key.length / 4);

        for (let i = 0; i < key.length; i += 4) {
            let value = key.readFloatBE(i);

            for (let j = ciphertext.length - 1; j >= 0; j--) {
                if (ciphertext[j] === 0) continue;

                switch (j % 4) {
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

            plaintext.writeUInt8(Math.round(value), i / 4);
        }

        return plaintext;
    }
};

module.exports = Chug;
