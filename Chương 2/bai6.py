def nhap_mang_so():
    mang = input("Nhập mảng số (các chữ số cách nhau bằng khoảng trắng): ").split()
    return [int(x) for x in mang]
def Tru(a, b):
    num_a = int(''.join(map(str, a)))
    num_b = int(''.join(map(str, b)))

    result = num_a - num_b
    return result
a = nhap_mang_so()
b = nhap_mang_so()
result = Tru(a, b)
print("Kết quả của phép trừ là:", result)
