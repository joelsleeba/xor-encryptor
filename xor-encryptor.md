% xor-encryptor(7) 0.0.1
% Joel Sleeba
% Jan 2022

# NAME
xor-encryptor - encrypt text keyphrase

# SYNOPSIS
**xor-encryptor** -[e,d] -i {input_file} -o {output_file}

# DESCRIPTION
**xor-encryptor** encrypt/decrypt texts with the logical xor. It takes input from the input_file and output to output_file

# OPTIONS
**-e**
: to encrypt

**-d**
: to decrypt

**-i** *input_file*
: specify the input file

**-o** *output_file*
: specify the output file

# EXAMPLES
**xor-encryptor -e -i plaintext.txt -o cipher.txt**
: Encrypts the content in *plaintext.txt* and saves it in *cipher.txt*

**xor-encryptor -d -i ciphertext.txt -o plaintext.txt**
: Decrypts the content in *ciphertext.txt* and saves it in *plaintext.txt*
