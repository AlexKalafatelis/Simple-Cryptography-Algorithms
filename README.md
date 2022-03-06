# Simple Cryptography Algorithms

Analysis of basic cryptographic algoritms for a university course. 
The code is written mainly in MATLAB and in python.

## A. Ceasar's Cipher 

The Caesar Cipher technique is one of the earliest and simplest method of encryption technique. It’s simply a type of substitution cipher, i.e., each letter of a given text is replaced by a letter some fixed number of positions down the alphabet. For example with a shift of 1, A would be replaced by B, B would become C, and so on. The method is apparently named after Julius Caesar, who apparently used it to communicate with his officials. 

Thus to cipher a given text we need an integer value, known as shift which indicates the number of position each letter of the text has been moved down. 
The encryption can be represented using modular arithmetic by first transforming the letters into numbers, according to the scheme, A = 0, B = 1,…, Z = 25. Encryption of a letter by a shift n can be described mathematically as. 

E_n(x)=(x+n)mod\ 26   
(Encryption Phase with shift n)

D_n(x)=(x-n)mod\ 26   
(Decryption Phase with shift n)

![image](https://user-images.githubusercontent.com/47864776/150894642-fc447eba-024b-424c-961f-85514cd00931.png)

https://www.geeksforgeeks.org/caesar-cipher-in-cryptography/


## B. Playfair Cipher

The Playfair cipher was the first practical digraph substitution cipher. The scheme was invented in 1854 by Charles Wheatstone but was named after Lord Playfair who promoted the use of the cipher. In playfair cipher unlike traditional cipher we encrypt a pair of alphabets(digraphs) instead of a single alphabet.

It was used for tactical purposes by British forces in the Second Boer War and in World War I and for the same purpose by the Australians during World War II. This was because Playfair is reasonably fast to use and requires no special equipment.

https://www.geeksforgeeks.org/playfair-cipher-with-examples/
