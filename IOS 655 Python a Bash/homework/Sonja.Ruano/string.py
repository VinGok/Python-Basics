#!/usr/bin/env python3

stringA="0100100100100000011000010110110100100000011010000110111101101110011011110111001001100101011001000010000001110100011011110010000001110111011001010110110001100011011011110110110101100101001000000111100101101111011101010010000001100001011011000110110000100000011010010110111000100000011101000110100001100101001000000101000001111001011101000110100001101111011011100010000001100011011011110111010101110010011100110110010100111010"
stringB="010101100110000101101100011000010111001000100000010011010110111101110010011001110110100001110101011011000110100101110011001000000101011001100001011011000110000101110010001000000100010001101111011010000110000101100101011100100110100101110011"

start=0
length=8
stringAA=""

while length <= len(stringA):
        stringAA += chr(int(stringA[start:length:1],2))
        start += 8
        length += 8
        
print("The first message is: '",stringAA,"'")

start=0
length=8
stringBB=""

while length <= len(stringB):
        stringBB += chr(int(stringB[start:length:1],2))
        start += 8
        length += 8

print("The second message is: '",stringBB,"'")
