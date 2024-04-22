def Hop(a, b):
    # Kết hợp hai mảng a và b, loại bỏ các phần tử trùng lặp và sắp xếp mảng kết quả
    set_a = set(a)
    set_b = set(b)
    merged_set = sorted(set_a.union(set_b))
    return merged_set
# Nhập mảng a từ bàn phím
a = input("Nhập mảng a các số, cách nhau bởi dấu cách: ").split()
a = [int(x) for x in a]
# Nhập mảng b từ bàn phím
b = input("Nhập mảng b các số, cách nhau bởi dấu cách: ").split()
b = [int(x) for x in b]
# Gọi phương thức Hop() và in kết quả
c = Hop(a, b)
print("Mảng c chứa các số không trùng nhau có trong mảng a hoặc trong mảng b và được sắp xếp tăng dần là:", c)
