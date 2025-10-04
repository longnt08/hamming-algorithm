
# ham tinh so bit chen vao
def calculate_the_number_of_extra_bits(original_code_length: int) -> int:
    r = 0
    for i in range(original_code_length):
        if 2**i - original_code_length - i - 1 >= 0:
            r = i
            break
    
    return r 

# ham kiem tra luy thua cua 2
def is_power_of_2(n: int) -> bool:
    return n > 0 and (n & (n-1)) == 0

# ham tao ma moi sau khi chen r bit
def insert_r_extra_bits(original_code: str, r: int) -> list:
    original_code += '5'
    reverse_list_original_code = [int(ch) for ch in original_code[::-1]]
    
    new_length = len(reverse_list_original_code) + r
    new_code_list = [5] * (new_length)
    index = 1

    for i in range(1, new_length):
        if not is_power_of_2(i):
            new_code_list[i] = reverse_list_original_code[index]
            index += 1

    # new_code_list.pop(0)

    return new_code_list

# ham tinh vi tri cac bit duoc quan ly boi bit them vao
def bit_positions(code: list, r: int) -> list:
    length_of_code = len(code)

    result = [i for i in range(1, length_of_code) if i & r]

    return result


n = calculate_the_number_of_extra_bits(10)
l = insert_r_extra_bits('1001101', 4)

print(l)

for i in range(1, len(l)):
    if is_power_of_2(i):
        group_bits_index = bit_positions(code=l, r=i)
        group_bit_values = [l[j] for j in group_bits_index]
        
        group_bit_values.pop(0)
        l[i] = sum(group_bit_values) % 2

print(l)