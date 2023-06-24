def check_file_bit_by_bit(file_path):
    try:
        with open(file_path, "rb") as file:
            byte_counter = 0
            while True:
                byte = file.read(1)
                if not byte:
                    break  # End of file
                for bit in range(8):
                    bit_value = (byte[0] >> bit) & 1
                    # Perform your desired operations on the bit value
                    print(f"Byte {byte_counter}, Bit {bit}: {bit_value}")
                byte_counter += 1
    except FileNotFoundError:
        print("File not found.")

# Example usage
file_path = "/home/crazyDog/Desktop/test.pdf"
check_file_bit_by_bit(file_path)
