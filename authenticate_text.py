import sys
import json
from egcd import egcd

def squareAndMultiply(x, k, n):
    k = reverseBits(k);
    res = 1;
    while (k > 0):
        if (k & 1 == 0):
            res = (res * res) % n;
            res * x  # fake multiplication
        else:
            res = (res * res * x) % n;
        k = k >> 1
    return res;


def reverseBits(number):
    bit_size = sys.getsizeof(number);
    string = "{:" + str(bit_size) + "b}";
    reversedInt = int(string.format(number)[::-1], 2);
    return reversedInt

def main(vectorTest=False, input=0):
    # Opening JSON file

    path = "./keys/public/pub.json"
    with open(path, 'r') as openfile:
        # Reading from json file
        json_object = json.load(openfile)

    e = json_object['e'];
    #print("public key e = " + str(e));
    n = json_object['n'];
    #print("public key n = " + str(n));

    path = "./signaturetext/sig.txt"
    signaturetext = [];

    if (vectorTest == False):
        with open(path) as f:
            for line in f:
                signaturetext.append(line);
    else:
        signaturetext = input.splitlines()

    print("validating = " + str(signaturetext));


    plaintext = "";

    for charInt in signaturetext:
        c = squareAndMultiply(int(charInt), e, n);
        plaintext += chr(c);
        #print("authenticated character = " + chr(c));

    # write to file:
    print("authenticated: " + str(plaintext));

    path = "./plaintext/m.txt"
    with open(path, 'w+') as f:
        f.write(str(plaintext));

    return plaintext;


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])