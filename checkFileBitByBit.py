/*
Diyar 
diypa571@gmail.com

*/
def check_file_bit_by_bit(file_path):
    try:
        with open(file_path, "rb") as file:
            byte_counter = 0
            while True:
                byte = file.read(1)
                if not byte:
                    break  # Slutet av filen
                for bit in range(8):
                    bit_value = (byte[0] >> bit) & 1
                    #  Bit Operation
                    print(f"Byte {byte_counter}, Bit {bit}: {bit_value}")
                byte_counter += 1
    except FileNotFoundError:
        print("Filen hittades inte....")
 
file_path = "path/to/your/file"
check_file_bit_by_bit(file_path)
