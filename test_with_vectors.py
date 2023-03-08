
import decode_text
import encode_text
import sign_text
import authenticate_text

inputs = ["vector 1", "Vector 2", "Vector 3"];
outputs = [];


# @params: encode_text.main(vectorTest, input)
# boolean vectorTest - True: pass input as the second parameter from this script
#                    - False: use the plaintext/m.txt as input, pass whatever as the second parameter
# input: the plain text to decipher

# @params: decode_text.main(vectorTest, input, CRTon)
# boolean vectorTest - True: pass input as the second parameter from this script
#                    - False: use the plaintext/m.txt as input, pass whatever as the second parameter
# input: the plain text to decipher
# boolean CRTon - True: compute using the Chinese Remainder Theorem
#               - False: compute using the Square and Multiply algorithm


# testing encoding and decoding (without CRT):
print("\ntesting encoding and decoding (without CRT):\n");
for input in inputs:
    encodedMessage = encode_text.main(True, input);
    decodedMessage = decode_text.main(True, encodedMessage, True);
    print("");
    outputs.append(decodedMessage);

print("Initial test vector: ");
print(inputs);

print("Deciphered output: ");
print(outputs);

# testing encoding and decoding (with CRT):
print("\ntesting encoding and decoding (with CRT):\n");
for input in inputs:
    encodedMessage = encode_text.main(True, input);
    decodedMessage = decode_text.main(True, encodedMessage, False);
    print("");
    outputs.append(decodedMessage);

print("Initial test vector: ");
print(inputs);

print("Deciphered output: ");
print(outputs);


# testing signing and validating (without CRT):
print("\ntesting signing and validating (without CRT):\n");
outputs = [];

for input in inputs:
    signedMessage = sign_text.main(True, input, False);
    validatedMessage = authenticate_text.main(True, signedMessage);
    print("");
    outputs.append(validatedMessage);

print("Initial test vector: ");
print(inputs);

print("Validated output: ");
print(outputs);


# testing signing and validating (with CRT):
print("\ntesting signing and validating (with CRT):\n");
outputs = [];

for input in inputs:
    signedMessage = sign_text.main(True, input, True);
    validatedMessage = authenticate_text.main(True, signedMessage);
    print("");
    outputs.append(validatedMessage);

print("Initial test vector: ");
print(inputs);

print("Validated output: ");
print(outputs);