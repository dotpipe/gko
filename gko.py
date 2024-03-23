# def derivative(n, x):
#     return ((2 * n) + x) / (n-1)
import random
import struct
def find_correct_pattern(differential, f):
    largess = round(differential)
    f = 2 if f <= 12 else f
    x = 0
    while ((largess) > 2):# (test_highest_order_bit(largess) >= threshold + 1):# and largess > number):
        i = 3
        while i >= 2:
            largess = (largess / i)
            x =  abs(largess)
            i -= 1
    largess = 1 if x == 0 else largess
    return largess, ((f*largess)%16)

# def process_file(input_file, output_file, count):
#     with open(output_file, "wb") as outfile:
#         with open(input_file, "rb") as file:
#             while True:
#                 data = file.read(count)
#                 if not data:
#                     break
#                 string = 0
#                 for i in range(len(data)*8):
#                     t, thr = find_correct_pattern(4, i)
#                     thr = 1 if thr % 2 != 1 else 0
#                     string <<= 1
#                     string += thr
#                 outfile.write(string.to_bytes((len(data) + 7) // 8, byteorder='big'))
def derivative(n, x):
    # Dummy implementation, replace with your actual derivative function
    return ((2 * n) + x) / (n-1)

def flip_bit(bit):
    return 1 if bit == 0 else 0

def process_file(input_file, output_file, count):
    with open(output_file, "wb") as outfile:
        with open(input_file, "rb") as file:
            while True:
                byte = file.read(1)
                if not byte:
                    break
                b = int(byte[0])
                binary = 0
                for i in range(count*8 - 1, -1, -1):
                    # Pass each bit through find_correct_pattern
                    _, thr = find_correct_pattern(b, i)
                    thr = 1 if thr % 2 != 1 else 0
                    binary <<= 1
                    binary = binary + (thr)

                    if (i % 64 == 0):
                        # out = int(binary, 2)
                        while (binary > 0):
                            y = (binary%256)
                            v = chr(y)
                            outfile.write(v.encode())
                            binary >>= 8

def main():
    count = 100
    differentials = []
    numbers = []
    with open("out3.bin", "wb") as outfile:
        with open("out2.bin", "rb") as file:
            while True:
                differentials.clear()
                numbers.clear()
                data = file.read(count)
                if not data:
                    break
                diff = 0
                for a in data:
                    binary_representation = bin(a)[2:].zfill(8)  # Convert byte to binary and ensure it's 8 bits long
                    for b in binary_representation:    
                        # diff += 1
                        numbers.insert(0,b)
                x = 0
                while True:
                    x += 1
                    for i, num in zip(range(len(numbers),0,-1), numbers):
                        threshold = find_correct_pattern(x, i)
                        if threshold == num:
                            break
                    outfile.write(struct.pack('I',x))
                    break
    
    process_file("out3.bin", "out4.bin", 1)
    print("Finished")

if __name__ == "__main__":
    main()
