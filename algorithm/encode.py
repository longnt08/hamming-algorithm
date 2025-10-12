from .utils import *

def encode_hamming(plain_text: str) -> str:
    plain_text = plain_text.strip()

    if not is_binary_string(plain_text):
        return "Không phải chuỗi nhị phân. Vui lòng thử lại!"
    
    # tính lương bit chèn vào 
    r = calculate_the_number_of_extra_bits(len(plain_text))

    # tạo mảng một chiều sau khi chèn r bit 
    new_code_arr = insert_r_extra_bits(original_code=plain_text, number_of_extra_bits=r)

    # tính giá trị các bit chèn vào 
    for i in range(1, len(new_code_arr)):
        if is_power_of_2(i):
            group_bit_indexes = bit_positions(code=new_code_arr, r=i)
            group_bit_values = [new_code_arr[j] for j in group_bit_indexes]

            group_bit_values.pop(0)
            new_code_arr[i] = sum(group_bit_values) % 2
    
    new_code_arr.reverse()
    new_code_arr.pop()

    encoded_hamming = ''.join(str(bit) for bit in new_code_arr)
    return encoded_hamming

if __name__ == '__main__':
    plain_text = input('Enter plain text: ')
    encoded_text = encode_hamming(plain_text=plain_text)
    print(encoded_text)