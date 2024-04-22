def Hieu(a, b):
    # Loại bỏ các phần tử trùng lặp và sắp xếp các mảng a và b
    set_a = sorted(set(a))
    set_b = sorted(set(b))
    # Tìm các phần tử có trong a nhưng không có trong b
    c = [x for x in set_a if x not in set_b]
    return c

# Nhập mảng a từ bàn phím
a = input("Nhập mảng a các số, cách nhau bởi dấu cách: ").split()
a = [int(x) for x in a]

# Nhập mảng b từ bàn phím
b = input("Nhập mảng b các số, cách nhau bởi dấu cách: ").split()
b = [int(x) for x in b]

# Gọi phương thức Hieu() và in kết quả
c = Hieu(a, b)
print("Mảng c chứa các số không trùng nhau có trong mảng a nhưng không có trong mảng b và được sắp xếp tăng dần là:", c)
