def Duynhat():
    # Nhập mảng từ bàn phím
    a = input("Nhập mảng các số, cách nhau bởi dấu cách: ").split()
    # Chuyển đổi các phần tử của mảng từ chuỗi sang số nguyên
    a = [int(x) for x in a]
    # Sử dụng set để loại bỏ các phần tử trùng lặp
    unique_numbers = set(a)
    # Sắp xếp các số duy nhất theo thứ tự tăng dần
    sorted_unique_numbers = sorted(unique_numbers)
    return sorted_unique_numbers

# Thực thi phương thức Duynhat() và in kết quả
b = Duynhat()
print("Mảng b chứa các số duy nhất từ mảng a và được sắp xếp tăng dần là:", b)
