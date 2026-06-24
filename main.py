class Order:
    def __init__(self, id, customer_name, product_name, unit_price, quantity, shipping_fee, voucher):
        self.id = id
        self.customer_name = customer_name
        self.product_name = product_name
        self.unit_price = unit_price
        self.quantity = quantity
        self.shipping_fee = shipping_fee
        self.voucher = voucher
        self.total_amount = 0.0
        self.order_type = ""
        self.calculate_total_amount()
        self.classify_order()

    def calculate_total_amount(self):
        self.total_amount = self.unit_price * self.quantity + self.shipping_fee - self.voucher
        if self.total_amount < 0:
            self.total_amount = 0

    def classify_order(self):
        if self.total_amount < 500000:
            self.order_type = "Nhỏ"
        elif self.total_amount < 2000000:
            self.order_type = "Trung bình"
        elif self.total_amount < 10000000:
            self.order_type = "Lớn"
        else:
            self.order_type = "VIP"


class OrderManager:
    def __init__(self):
        self.orders = []

    def show_all(self):
        if not self.orders:
            print("Danh sách đơn hàng đang rỗng!")
            return
        print(f"{'Mã ĐH':<12} | {'Tên khách hàng':<20} | {'Tên sản phẩm':<20} | {'Đơn giá':<12} | {'SL':<6} | {'Phí VC':<12} | {'Voucher':<12} | {'Tổng tiền':<14} | {'Phân loại'}")
        for o in self.orders:
            print(f"{o.id:<12} | {o.customer_name:<20} | {o.product_name:<20} | {o.unit_price:<12.0f} | {o.quantity:<6} | {o.shipping_fee:<12.0f} | {o.voucher:<12.0f} | {o.total_amount:<14.0f} | {o.order_type}")

    def add_order(self):
        print("--- Thêm đơn hàng mới ---")
        while True:
            id = input("Mã đơn hàng: ").strip()
            if not id:
                print("Không được để trống!")
                continue
            found = False
            for o in self.orders:
                if o.id == id:
                    found = True
                    break
            if found:
                print("Mã đơn hàng đã tồn tại!")
                continue
            break
        while True:
            customer_name = input("Tên khách hàng: ").strip()
            if not customer_name:
                print("Không được để trống!")
                continue
            break
        while True:
            product_name = input("Tên sản phẩm: ").strip()
            if not product_name:
                print("Không được để trống!")
                continue
            break
        while True:
            unit_price = input_float("Đơn giá (>= 0): ")
            if unit_price < 0:
                print("Đơn giá không được âm!")
                continue
            break
        while True:
            quantity = input_int("Số lượng (1-1000): ")
            if quantity < 1 or quantity > 1000:
                print("Số lượng phải từ 1 đến 1000!")
                continue
            break
        while True:
            shipping_fee = input_float("Phí vận chuyển: ")
            if shipping_fee < 0:
                print("Phí vận chuyển không được âm")
                continue
            break
        while True:
            voucher = input_float("Voucher: ")
            if voucher < 0:
                print("Voucher không được âm")
                continue
            break
        o = Order(id, customer_name, product_name, unit_price, quantity, shipping_fee, voucher)
        self.orders.append(o)
        print("Thêm đơn hàng thành công!")

    def update_order(self):
        if not self.orders:
            print("Danh sách đơn hàng đang rỗng")
            return
        id = input("Nhập mã đơn hàng cần cập nhật: ").strip()
        found = None
        for o in self.orders:
            if o.id == id:
                found = o
                break
        if found is None:
            print("Không tìm thấy đơn hàng cần cập nhật")
            return
        while True:
            unit_price = input_float("Đơn giá mới: ")
            if unit_price < 0:
                print("Đơn giá không được âm!")
                continue
            break
        while True:
            quantity = input_int("Số lượng mới: ")
            if quantity < 1 or quantity > 1000:
                print("Số lượng phải từ 1 đến 1000!")
                continue
            break
        while True:
            shipping_fee = input_float("Phí vận chuyển mới: ")
            if shipping_fee < 0:
                print("Phí vận chuyển không được âm!")
                continue
            break
        while True:
            voucher = input_float("Voucher mới: ")
            if voucher < 0:
                print("Voucher không được âm!")
                continue
            break
        found.unit_price = unit_price
        found.quantity = quantity
        found.shipping_fee = shipping_fee
        found.voucher = voucher
        found.calculate_total_amount()
        found.classify_order()
        print("Cập nhật đơn hàng thành công!")

    def delete_order(self):
        if not self.orders:
            print("Danh sách đơn hàng đang rỗng!")
            return
        id = input("Nhập mã đơn hàng cần xóa: ").strip()
        found = None
        for o in self.orders:
            if o.id == id:
                found = o
                break
        if found is None:
            print("Không tìm thấy đơn hàng cần xóa!")
            return
        confirm = input("Bạn có chắc muốn xóa đơn hàng này không? (Y/N): ").strip().lower()
        if confirm == "y":
            self.orders.remove(found)
            print("Xóa đơn hàng thành công!")
        elif confirm == "n":
            print("Đã hủy thao tác xóa!")
        else:
            print("Lựa chọn không hợp lệ!")

    def search_order(self):
        if not self.orders:
            print("Danh sách đơn hàng đang rỗng!")
            return
        keyword = input("Nhập từ khóa tìm kiếm (tên khách hàng hoặc tên sản phẩm): ").strip().lower()
        results = []
      


def input_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Dữ liệu không hợp lệ!")


def input_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Dữ liệu không hợp lệ!")


def menu():
    print("================ MENU ================")
    print("1. Hiển thị danh sách đơn hàng")
    print("2. Thêm đơn hàng mới")
    print("3. Cập nhật đơn hàng")
    print("4. Xóa đơn hàng")
    print("5. Tìm kiếm đơn hàng")
    print("6. Thoát")
    print("=====================================")


def main():
    manager = OrderManager()
    while True:
        menu()
        choice = input("Nhập lựa chọn của bạn: ").strip()
        match choice:
            case "1":
                manager.show_all()
            case "2":
                manager.add_order()
            case "3":
                manager.update_order()
            case "4":
                manager.delete_order()
            case "5":
                manager.search_order()
            case "6":
                print("Đã thoát")
                break
            case _:
                print("Lựa chọn không hợp lệ. Vui lòng nhập từ 1 đến 6.")

if __name__ == "__main__":
    main()