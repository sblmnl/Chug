# Usage

## Installation
```
pip install chug
```

## Sample Code

```python
import binascii
from chug import Chug

plaintext = "My secret".encode("utf8")
ciphertext = "Not my secret".encode("utf8")
key = Chug.create_key(plaintext, ciphertext)
secret = Chug.decrypt(ciphertext, key)

print("plaintext\t:\t%s" % binascii.hexlify(plaintext).decode("utf8"))
print("ciphertext\t:\t%s" % binascii.hexlify(ciphertext).decode("utf8"))
print("key\t\t:\t%s" % binascii.hexlify(key).decode("utf8"))
print("secret\t\t:\t%s" % binascii.hexlify(secret).decode("utf8"))
```

## Expected Output
```
plaintext       :       4d7920736563726574
ciphertext      :       4e6f74206d7920736563726574
key             :       4324956f4356add042e2b330434fd908433fe88d433da19f434eb592433fe88d4350fc7f
secret          :       4d7920736563726574
```

# Documentation

## Methods
* **Chug.create_key(plaintext, ciphertext)**
    * `plaintext` [`bytes`](https://docs.python.org/3/c-api/bytes.html) The plaintext bytes.
    * `ciphertext` [`bytes`](https://docs.python.org/3/c-api/bytes.html) The ciphertext bytes.
    * Returns [`bytes`](https://docs.python.org/3/c-api/bytes.html)
* **Chug.decrypt(ciphertext, key)**
    * `ciphertext` [`bytes`](https://docs.python.org/3/c-api/bytes.html) The ciphertext bytes.
    * `key` [`bytes`](https://docs.python.org/3/c-api/bytes.html) The key bytes.
    * Returns [`bytes`](https://docs.python.org/3/c-api/bytes.html)