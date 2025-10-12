from .utils import *

def decode_hamming(correct_encoded_text: str) -> str:
    correct_encoded_text.strip()

    if not is_binary_string(correct_encoded_text):
        return "Chuỗi chỉ được chứa giá trị 0 hoặc 1."
    
    correct_encoded_text = correct_encoded_text 
    reversed_code = correct_encoded_text[::-1]

    result = ''.join(
        char for i, char in enumerate(reversed_code, start=1)
        if not is_power_of_2(i)
    )

    return result[::-1]

if __name__ == '__main__':
    correct_code = '10011100101'
    result = decode_hamming(correct_encoded_text=correct_code)
    print(result)