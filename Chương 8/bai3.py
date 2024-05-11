
class TuDien:
    def __init__(self):
        self.tudien = {}  # Từ điển dạng dict lưu trữ thông tin album

    def NhapAlbum(self, album):
        """
        Hàm nhập thông tin album vào từ điển.

        Args:
            album (dict): Từ điển chứa thông tin album, bao gồm:
                - ten: Tên album (str)
                - bai_hat: Danh sách các bài hát trong album (list[dict]), mỗi bài hát là một dict
                    bao gồm:
                        - ten_bai_hat: Tên bài hát (str)
                        - nhac_si: Tên nhạc sĩ sáng tác (str)
                        - ca_si: Tên ca sĩ hát (str)
        """
        ten_album = album["ten"]
        if ten_album in self.tudien:
            print(f"Album '{ten_album}' đã tồn tại!")
            return
        self.tudien[ten_album] = album

    def XemAlbum(self, ten_album):
        """
        Hàm hiển thị thông tin của album có tên `ten_album`.

        Args:
            ten_album (str): Tên album cần xem.
        """
        if ten_album not in self.tudien:
            print(f"Không tìm thấy album '{ten_album}'!")
            return
        album = self.tudien[ten_album]
        print(f"\n**Album: {album['ten']}**")
        for bai_hat in album["bai_hat"]:
            print(f"- {bai_hat['ten_bai_hat']}")
            print(f"  - Sáng tác: {bai_hat['nhac_si']}")
            print(f"  - Trình bày: {bai_hat['ca_si']}")
# Tạo từ điển
td = TuDien()
# Nạp thông tin album
album_1 = {
    "ten": "Bài hát cho em",
    "bai_hat": [
        {"ten_bai_hat": "Yêu", "nhac_si": "Nguyễn Văn A", "ca_si": "Trần Thị B"},
        {"ten_bai_hat": "Nhớ", "nhac_si": "Nguyễn Văn A", "ca_si": "Trần Thị B"},
    ],
}
album_2 = {
    "ten": "Sóng",
    "bai_hat": [
        {"ten_bai_hat": "Cơn gió", "nhac_si": "Trần Thị C", "ca_si": "Lê Văn D"},
        {"ten_bai_hat": "Biển rộng", "nhac_si": "Trần Thị C", "ca_si": "Lê Văn D"},
    ],
}
td.NhapAlbum(album_1)
td.NhapAlbum(album_2)
# Xem thông tin album
td.XemAlbum("Bài hát cho em")
td.XemAlbum("Sóng")
