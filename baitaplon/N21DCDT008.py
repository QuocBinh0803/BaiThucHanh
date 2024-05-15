from collections import OrderedDict

def parse_line(line):
    parts = line.split(' - ')
    if len(parts) == 2:
        word_pos, definition = parts
        word, pos = word_pos.split(' (')
        pos = pos.rstrip(')')
        return word.strip(), pos.strip(), definition.strip()
    return None, None, None

def read_file_to_dict(file_path):
    dictionary = OrderedDict()
    current_key = None
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            
            if line[0].islower():
                current_key = line
                dictionary[current_key] = []
            elif line.split(': ')[0] == "Ví dụ":
                dictionary[current_key].append(line)
            else:
                word, pos, definition = parse_line(line)
                if current_key and word and pos and definition:
                    dictionary[current_key].append(f"{word} ({pos}) - {definition}")
    dictionary = dict(sorted(dictionary.items()))
    for key in dictionary:
        dictionary[key].sort()
    return dictionary

def napTuDien():
    file_path = 'N21DCDT008_mang.txt'
    dictionary = read_file_to_dict(file_path)

    for key, definitions in dictionary.items():
        print(f'{key}:')
        for definition in definitions:
            print(f'  {definition}')

def XoaTu():
    file_path = 'N21DCDT008_mang.txt'
    dictionary = read_file_to_dict(file_path)

    str = input("Nhập từ cần xóa: ")

    for key, definitions in dictionary.items():
        if key == str:
            del dictionary[key]
            print("THÔNG BÁO: ĐÃ XÓA THÀNH CÔNG!")
            print("---Từ đã xóa:")
            print(f'{key}:')
            for definition in definitions:
                print(f'  {definition}')
            break

    with open(file_path, 'w', encoding='utf-8') as file:
        for key, definitions in dictionary.items():
            file.write(key + "\n")
            for definition in definitions:
                file.write(definition + "\n")
    
def TraCuu():
    file_path = 'N21DCDT008_mang.txt'
    dictionary = read_file_to_dict(file_path)
    str = input("Nhập từ cần tra cứu: ") 

    for key, definitions in dictionary.items():
        if key == str:
            print("THÔNG BÁO: ĐÃ TÌM THẤY!")
            print("---Từ đã tìm:")
            print(f'{key}:')
            for definition in definitions:
                print(f'  {definition}')
            break
        else:
            for definition in definitions:
                if definition.split()[0] == str:
                    print("THÔNG BÁO: ĐÃ TÌM THẤY!")
                    print("---Từ đã tìm:")
                    print(definition)
                    break

def addTu():
    str = input("Nhập từ cần thêm: ")
    check = int(input("Nhập số thành phần của từ: "))
    while check != 0:
        str1 = input("Nhập từ tiếng anh: ")
        str2 = input("Nhập từ loại(n, a, v): ")
        str3 = input("Nhập nghĩa tiếng việt: ")

        check -= 1
        str += "\n" + str1 + " (" + str2 + ")" + " - " + str3
    str += ("\nVí dụ: " + input("Nhập ví dụ: "))
    print("Từ đã thêm: \n" + str)
    return str

def LuuTu():
    file_path = 'N21DCDT008_mang.txt'
    with open(file_path, 'a', encoding='utf-8') as file:
        a = addTu()
        file.write(a + "\n")

def main_menu():
    while True:
        print("\n-------TRANG CHỦ----------:")
        print("1. Thêm từ")
        print("2. Loại bỏ từ")
        print("3. Tra cứu định nghĩa")
        print("4. Nạp từ điển từ tệp")
        print("5. Kết thúc chương trình")
        choice = input("Nhập lựa chọn của bạn: ")

        if choice == "1":
            LuuTu()
        elif choice == "2":
            XoaTu()
        elif choice == "3":
            TraCuu()
        elif choice == "4":
            napTuDien()
        elif choice == "5":
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")

if __name__ == "__main__":
    main_menu()
