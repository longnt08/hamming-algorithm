from .utils import *

def check_encoded_hamming(encoded_text: str) -> int:
    encoded_text.strip()

    if not is_binary_string(encoded_text):
        return -1 
 
    # cộng thêm một ký tự để bắt đầu từ chỉ số 1 
    encoded_text = encoded_text + '5'
    
    arr_encoded = [int(ch) for ch in encoded_text]
    arr_encoded.reverse()

    # khởi tạo mảng chứa kết quả 
    check_arr = []

    # tính giá trị các bit kiểm tra 
    for i in range(1, len(arr_encoded)):
        if is_power_of_2(i):
            group_bit_indexes = bit_positions(code=arr_encoded, r=i)
            group_bit_values = [arr_encoded[j] for j in group_bit_indexes]

            checked_val = sum(group_bit_values) % 2
            check_arr.append(checked_val)

    check_number = binary_to_decimal(bits=check_arr)

    if check_number == 0:
        return 0
    else:
        return check_number


def fix_encoded_hamming(err_code: str, err_bit_index: int) -> str:
    err_code.strip()

    if not is_binary_string(err_code):
        return "Mã phải là chuỗi nhị phân. Vui lòng thử lại"

    err_code = err_code + '5'
    arr_code = [int(ch) for ch in err_code]
    arr_code.reverse()

    # sửa lại bit lỗi 
    arr_code[err_bit_index] ^= 1
    # bỏ giá trị 5 ở đầu mảng 
    arr_code.pop(0)
    arr_code.reverse()

    fixed_code = ''.join(str(bit) for bit in arr_code)

    return fixed_code
    
if __name__ == '__main__':
    encoded_text = input('enter encoded text: ')
    result = check_encoded_hamming(encoded_text=encoded_text)
    
    if result == -1:
        print('Du lieu phai la nhi phan')
    elif result == 0:
        print('Du lieu dung')
    else:
        print(f'Du lieu loi o bit thu {result}')
        fixed_code = fix_encoded_hamming(err_code=encoded_text ,err_bit_index=result)
        print('Du lieu sau khi sua:\n', fixed_code)