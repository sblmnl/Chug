# Usage

## Installation
```
npm i chugjs --save
```

## Sample Code

```javascript
const Chug = require("chug");

let plaintext = Buffer.from("My secret", "utf8");
let ciphertext = Buffer.from("Not my secret", "utf8");
let key = Chug.createKey(plaintext, ciphertext);
let secret = Chug.decrypt(ciphertext, key);

console.log("plaintext\t:\t", plaintext.toString("hex"));
console.log("ciphertext\t:\t", ciphertext.toString("hex"));
console.log(`key\t\t:\t`, key.toString("hex"));
console.log("secret\t\t:\t", secret.toString("hex"));
```

## Expected Output
```
plaintext       :        4d7920736563726574
ciphertext      :        4e6f74206d7920736563726574
key             :        4324956f4356add042e2b330434fd908433fe88d433da19f434eb592433fe88d4350fc7f
secret          :        4d7920736563726574
```

# Documentation

## Methods
* **Chug.createKey(plaintext, ciphertext)**
    * `plaintext` [`<Buffer>`](https://nodejs.org/api/buffer.html#buffer_class_buffer) The plaintext bytes.
    * `ciphertext` [`<Buffer>`](https://nodejs.org/api/buffer.html#buffer_class_buffer) The ciphertext bytes.
    * Returns [`<Buffer>`](https://nodejs.org/api/buffer.html#buffer_class_buffer)
* **Chug.decrypt(ciphertext, key)**
    * `ciphertext` [`<Buffer>`](https://nodejs.org/api/buffer.html#buffer_class_buffer) The ciphertext bytes.
    * `key` [`<Buffer>`](https://nodejs.org/api/buffer.html#buffer_class_buffer) The key bytes.
    * Returns [`<Buffer>`](https://nodejs.org/api/buffer.html#buffer_class_buffer)