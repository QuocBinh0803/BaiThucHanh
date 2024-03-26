class HanoiTower:
    def __init__(self, num_disks):
        self.num_disks = num_disks

    def move_disks(self, n, from_rod, to_rod, aux_rod):
        if n == 1:
            print(f"Di chuyển đĩa 1 từ tháp {from_rod} đến tháp {to_rod}")
            return
        self.move_disks(n-1, from_rod, aux_rod, to_rod)
        print(f"Di chuyển đĩa {n} từ tháp {from_rod} đến tháp {to_rod}")
        self.move_disks(n-1, aux_rod, to_rod, from_rod)

num_disks = int(input("Nhập số đĩa: "))
hanoi = HanoiTower(num_disks)
print("Các bước di chuyển:")
hanoi.move_disks(num_disks, '1', '3', '2')
