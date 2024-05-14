import json
tu_dien = {}
def addTu():
    str = input("Nhập từ cần thêm: ")
    check = int(input("Nhập số thành phần của từ: "))
    while check != 0:
        str1 = input("Nhập từ tiếng anh: ")
        str2 = input("Nhập từ loại(n, a, v): ")
        str3 = input("Nhập nghĩa tiếng việt: ")
        check -= 1
        str += "\n" + str1 + " (" + str2 + ")" + " - " + str3
    print("Từ đã thêm: \n" + str)
    return str
def them_tu(tu):
    if tu not in tu_dien:
        tu_dien[tu] = []
        print(f"'{tu}' đã được thêm vào từ điển.")
    else:
        print(f"'{tu}' đã tồn tại trong từ điển.")

def xoa_tu(tu):
    if tu in tu_dien:
        del tu_dien[tu]
        print(f"'{tu}' đã được loại bỏ khỏi từ điển.")
    else:
        print(f"'{tu}' không tồn tại trong từ điển.")

def tra_cuu(tu):
    if tu in tu_dien:
        print(f"Định nghĩa cho '{tu}':")
        for idx, (loai_tu, dinh_nghia, vi_du) in enumerate(tu_dien[tu], start=1):
            print(f"{idx}. {loai_tu}: {dinh_nghia}")
            print(f"   Ví dụ: {vi_du}")
    else:
        print(f"'{tu}' không được tìm thấy trong từ điển.")

# def luu_tu_dien(filename):
#     with open(filename, 'w') as file:
#         json.dump(tu_dien, file)
#     print("Từ điển đã được lưu vào", filename)

# def nap_tu_dien(filename):
#     global tu_dien
#     with open(filename, 'r') as file:
#         tu_dien = json.load(file)
#     print("Từ điển đã được nạp từ", filename)

def ghi_File(filename):
    with open(filename, 'a', encoding='utf-8-sig') as file:
        a = addTu()
        file.write(a)
    print("Từ điển đã được nạp từ", filename)

def doc_File(filename):
    global tu_dien
    with open(filename, 'r', encoding='utf-8-sig') as file:
        for line in file:
            if line.strip():  # Kiểm tra xem dòng có trống không
                print(line)
    print("Từ điển đã được nạp từ", filename)

def main_menu():
    while True:
        print("\nTrang Chủ:")
        print("1. Thêm từ")
        print("2. Loại bỏ từ")
        print("3. Tra cứu định nghĩa")
        print("4. Lưu từ điển vào tệp")
        print("5. Nạp từ điển từ tệp")
        print("6. Kết thúc chương trình")
        choice = input("Nhập lựa chọn của bạn: ")

        if choice == "1":
            addTu()
        elif choice == "2":
            tu = input("Nhập từ cần loại bỏ: ")
            xoa_tu(tu)
        elif choice == "3":
            tu = input("Nhập từ cần tra cứu: ")
            tra_cuu(tu)
        elif choice == "4":
            ten_tep = input("Nhập tên tệp để lưu: ")
            ghi_File(ten_tep)
        elif choice == "5":
            ten_tep = input("Nhập tên tệp để nạp: ")
            doc_File(ten_tep)
        elif choice == "6":
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")

if __name__ == "__main__":
    main_menu()
