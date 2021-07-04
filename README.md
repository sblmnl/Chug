# Chug

[![License](https://img.shields.io/static/v1?label=license&message=MIT&color=brightgreen)](https://github.com/sblmnl/Chug/blob/main/LICENSE)

Chug is a symmetric encryption algorithm in which the key is calculated from a known plaintext and a known ciphertext.

## Suggestions & Bug Reports

If you would like to suggest a feature or report a bug please see the [issues](https://github.com/sblmnl/Chug/issues) page.

## Mathematic Overview

### Key Creation

```
p = (10, 20)
c = (1, 2, 3, 4)
k = (
        ((((p(1) + c(1)) - c(2)) * c(3)) / c(4)),
        ((((p(2) + c(1)) - c(2)) * c(3)) / c(4))
    )
```

### Decryption

```
c = (1, 2, 3, 4)
k = (6.75, 14.25)
p = (
        ((((k(1) * c(4) / c(3)) + c(2)) - c(1)),
        ((((k(2) * c(4) / c(3)) + c(2)) - c(1))
    )
```

### Variable Definitions

* **p** :   The variable that represents the plaintext value.
* **c** :   The variable that represents the ciphertext value.
* **k** :   The variable that represents the key value.

## Authors

* **Developer** - [sblmnl](https://github.com/sblmnl)

See the [contributors](https://github.com/sblmnl/Chug/contributors) page for a list of all project participants.

## License

This project is licensed under the MIT license - see the [LICENSE](https://github.com/sblmnl/Chug/blob/main/LICENSE) file for details.