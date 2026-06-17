secret_code = int(input("Enter secret code (number): "))
access_key = int(input("Enter access key (number): "))

print("\n--- Binary Representation ---")
print("Secret Code:", bin(secret_code))
print("Access Key :", bin(access_key))

match = secret_code & access_key
print("\n--- Matching Bits (AND) ---")
print("Result:", bin(match))

difference = secret_code ^ access_key
print("\n--- Different Bits (XOR) ---")
print("Result:", bin(difference))

flipped = ~secret_code
print("\n--- Flipped Secret Code (NOT) ---")
print("Result:", bin(flipped))

left_shift = secret_code << 1
right_shift = secret_code >> 1

print("\n--- Bit Shifting ---")
print("Left Shift :", bin(left_shift))
print("Right Shift:", bin(right_shift))

count_ones = bin(secret_code).count('1')
print("\n--- Bit Count ---")
print("Number of 1s in Secret Code:", count_ones)