# Usage

## Installation
```
Install-Package ChugSharp
```

## Sample Code

```csharp
using System;
using System.Text;

class Program
{
    static void Main()
    {
        byte[] plaintext = Encoding.UTF8.GetBytes("My secret");
        byte[] ciphertext = Encoding.UTF8.GetBytes("Not my secret");
        byte[] key = Chug.CreateKey(plaintext, ciphertext);
        byte[] secret = Chug.Decrypt(ciphertext, key);

        Console.WriteLine("plaintext\t:\t{0}", BitConverter.ToString(plaintext).Replace("-", "").ToLower());
        Console.WriteLine("ciphertext\t:\t{0}", BitConverter.ToString(ciphertext).Replace("-", "").ToLower());
        Console.WriteLine("key\t\t:\t{0}", BitConverter.ToString(key).Replace("-", "").ToLower());
        Console.WriteLine("secret\t\t:\t{0}", BitConverter.ToString(secret).Replace("-", "").ToLower());
    }
}
```

## Expected Output
```
plaintext       :       4d7920736563726574
ciphertext      :       4e6f74206d7920736563726574
key             :       432495704356add042e2b331434fd909433fe88c433da1a0434eb592433fe88c4350fc7e
secret          :       4d7920736563726574
```

# Documentation

## Methods
* **Chug.CreateKey(plaintext, ciphertext)**
    * `plaintext` [`byte[]`](https://docs.microsoft.com/en-us/dotnet/api/system.byte) The plaintext bytes.
    * `ciphertext` [`byte[]`](https://docs.microsoft.com/en-us/dotnet/api/system.byte) The ciphertext bytes.
    * Returns [`byte[]`](https://docs.microsoft.com/en-us/dotnet/api/system.byte)
* **Chug.Decrypt(ciphertext, key)**
    * `ciphertext` [`byte[]`](https://docs.microsoft.com/en-us/dotnet/api/system.byte) The ciphertext bytes.
    * `key` [`byte[]`](https://docs.microsoft.com/en-us/dotnet/api/system.byte) The key bytes.
    * Returns [`byte[]`](https://docs.microsoft.com/en-us/dotnet/api/system.byte)