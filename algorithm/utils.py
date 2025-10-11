# hàm kiểm tra chuỗi nhị phân 
def is_binary_string(s: str) -> bool:
    return all(ch in ('0', '1') for ch in s)

# hàm tính số bit chèn vào 
def calculate_the_number_of_extra_bits(original_code_length: int) -> int:
    r = 0
    for i in range(original_code_length):
        if 2**i - original_code_length - i - 1 >= 0:
            r = i
            break
    
    return r 

# hàm chuyển giá trị nhị phân sang thập phân 
def binary_to_decimal(bits: list[int]) -> int:
    binary_str = ''.join(str(bit) for bit in bits)

    return int(binary_str, 2)

# hàm kiểm tra lũy thừa của 2 
def is_power_of_2(n: int) -> bool:
    return n > 0 and (n & (n-1)) == 0

# hàm tạo chuỗi mã mới sau khi chèn r bit 
def insert_r_extra_bits(original_code: str, number_of_extra_bits: int) -> list:
    original_code += '5'
    reverse_list_original_code = [int(ch) for ch in original_code[::-1]]
    
    new_length = len(reverse_list_original_code) + number_of_extra_bits
    new_code_list = [5] * (new_length)
    index = 1

    for i in range(1, new_length):
        if not is_power_of_2(i):
            new_code_list[i] = reverse_list_original_code[index]
            index += 1

    return new_code_list

# hàm tính vị trí các bit được quản lý bởi bit thêm vào 
def bit_positions(code: list, r: int) -> list:
    length_of_code = len(code)

    result = [i for i in range(1, length_of_code) if i & r]

    return result