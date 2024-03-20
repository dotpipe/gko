import random
import math as Math

def antiderivative(n, x):
    return ((2 * n) + x) / (n + 1) / 10

def find_correct_pattern(differential, threshold, number, f):
    largess = differential
    while (test_highest_order_bit(round(largess)) > threshold):# (test_highest_order_bit(largess) >= threshold + 1):# and largess > number):
        i = 3
        while i >= 2:
            largess = round(largess / i)
            if test_highest_order_bit(round(largess)) <= largess:
                return i, number
            # if Math.ceil(((largess * f) // (f - 1)) - (2 * f) // 3) == number:
            #     return i, number
            # if Math.floor(((largess * f) // (f - 1)) - (2 * f) // 3) == number:
            #     return i, number
            # largess = Math.ceil(((largess * f) // (f - 1)) - (2 * f) // 3)
            i -= 1
    return None, round((largess + f) * (f)) # Math.ceil(((largess * f) // (f - 1)) - (2 * f) // 3)

def undo_integration(largess, thresholds, patterns):
    binary_pattern = ""
    for pattern, threshold in zip(patterns, thresholds):
        divisor = pattern[0] if pattern == "0" else pattern[1]
        division = largess // threshold
        largess -= division * threshold
        binary_pattern += pattern
    return largess, binary_pattern

def test_highest_order_bit(number):
    # Shift the number right until it becomes zero
    # Count the number of shifts needed to reach zero
    # The number of shifts corresponds to the position of the highest order bit
    highest_order_bit_position = 0
    while number:
        number >>= 1
        highest_order_bit_position += 1
    return highest_order_bit_position

def main():
    # count = input("Enter the count for generating random numbers: ")

    count = 24
    integration = 1
    differentials = []
    numbers = []
    for diff in range(1,count):
        a = random.randint(0,256)
        numbers.insert(0,a)
        differentials.append((antiderivative(diff, a)))
        integration *= (antiderivative(diff, a))

    print(numbers)
    print("Integration:", integration)
    continuum = integration
    thresholds = []
    patterns = []
    for i, num in zip(range(count,1,-1), numbers):
        b = test_highest_order_bit(num)
        pattern, threshold = find_correct_pattern(integration, b-1, num, i)
        print(f"The correct pattern for differential {num} is: {pattern}")
        print(f"Threshold (binary): {threshold}")
        print(f"Threshold (power of 2): {2**(b)} {i}")
        integral = int(threshold)
        integration /= integral
        continuum -= (integration)
        integration = continuum
    print("Final Largess after undoing integration:", continuum)

if __name__ == "__main__":
    main()
