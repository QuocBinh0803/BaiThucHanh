def nhap_mang_so():
    mang = input("Nhập mảng số (các chữ số cách nhau bằng khoảng trắng): ").split()
    return [int(x) for x in mang]

def Cong(a, b):
    num_a = int(''.join(map(str, a)))
    num_b = int(''.join(map(str, b)))

    result = num_a + num_b
    if result < 10**len(a):
        return [int(x) for x in str(result)]
    else:
        return [-1] * len(a)

a = nhap_mang_so()
b = nhap_mang_so()

result = Cong(a, b)
if -1 in result:
    print("Kết quả bị tràn")
else:
    print("Kết quả của phép cộng là:", result)
