saving_accounts = [
    {
        "account_id": "STK001",
        "customer_name": "Nguyễn Văn An",
        "balance": 50000000,
        "term_months": 6,
        "interest_rate": 6.5,
        "status": "active"
    },
    {
        "account_id": "STK002",
        "customer_name": "Trần Thị Bình",
        "balance": 120000000,
        "term_months": 12,
        "interest_rate": 7.2,
        "status": "active"
    }
]

choice = 0
while True:
    choice = input('''
===== HỆ THỐNG QUẢN LÝ TÀI KHOẢN TIẾT KIỆM TECHBANK =====
1. Xem danh sách sổ tiết kiệm
2. Mở sổ tiết kiệm mới
3. Cập nhật thông tin sổ tiết kiệm
4. Tất toán hoặc xóa sổ tiết kiệm
5. Tính lãi dự kiến khi đến hạn
6. Kiểm tra điều kiện rút trước hạn
7. Thoát chương trình    
''')
    
        #  nhập số cho choice thay vì nhập chữ
    if not choice.isdigit:
        print("nhập số không phải chữ")
        continue
    
    # chỉ được chọn từ 1 đên s5
    if choice < '1' or choice > '7':
        print("Lựa chọn không hợp lệ, vui lòng nhập lại từ 1-5!")
        continue

    match choice : 
        case '1': 
            print("")
            print('Danh sách sổ tiết kiệm')
            
            if saving_accounts == []:
                print("Danh sách sổ tiết kiệm hiện đang trống")
            else :
                for index, value in enumerate(saving_accounts,start= 1):
                    print(f"{index} . Mã số: {value['account_id']:<10} | Khách hàng: {value['customer_name']:<10} | Số tiền gửi : {value['balance']:<10} |  Kỳ hạn: {value['term_months']:<5} | Lãi xuất: {value['interest_rate']:<5} %/năm | Trạng thái: {value['status']:<10}")
        
        case '2': 
            # tạo danh sách mới 
            print("")
            new_id = input("Nhập mã số tiết kiệm: ").strip().upper()

            
            for index  in saving_accounts:
                # check trùng
                if index['account_id'] == new_id : 
                    print("Trùng dữ liệu . Không được để trùng ")
                    break
                else:
                    new_name = input("Nhập tên khách hàng: ")
                    new_send_money = input('Nhập số tiền gửi: ')
                    new_time = input("NHập kỳ hạn gửi theo tháng : ")
                    new_interest = input("nhập lãi suất năm: ")
                    new_status = input("Trạng thái")
                
                #check trống  
                if new_id ==[] or new_name ==[] or new_send_money == [] or new_time == [] or new_interest == []: 
                    print("không được để trống mã sổ tiết kiểm , tên khách hàng, số tiền gửi , kỳ hạn hoặc lãi suất")
                    break
                
                # check số thực 
                if new_interest.isdecimal():
                    interest = float(new_interest)

                # check tiền, kỳ hạn gửi âm dương , 
                if new_send_money > '0' and new_time > '0'  :
                    new_saving_accounts = {
                        "account_id":new_id ,
                        "customer_name": new_name,
                        "balance":  new_send_money,
                        "term_months": new_time,
                        "interest_rate": new_interest,
                        "status": "active"
                    }
                    saving_accounts.append(new_saving_accounts)
                    print("Thêm sản phẩm thành công ")
                    break
                else:
                    print("tiền , kỳ hạn  phải là nguyên dương   ")
                    break
            
        case '3':
            # cạt nhập 
            print("")
            update_id = input("Nhập id cần cật nhập: ")
            
            for index in saving_accounts:
                if update_id == index['account_id']:
                    print(f"Cật nhập sản phẩm :{index['customer_name']}")

                    update_name  = input('nhập tên :')
                    update_price = input('nhập hoá đơn : ')
                    update_time = input('Nhập số tiền gửi mới')
                    update_rate = input('Nhập lãi suất năm mới:')
                    update_status  = 'active'

                # check tên khách hàng không được để trống 
                    if update_name ==[]:
                        print("không được để trống tên")

                # check số thực 
                    if update_rate.isdecimal():
                        interest = float(update_rate)

                # số tiền và kyỳ hạn phải lớn hơn 0
                    if update_price > '0' and  update_time > '0':
                        # cật nhập
                        index['account_id'] = update_id
                        index['customer_name'] = update_name
                        index['balance'] = update_price
                        index['term_months'] = update_time
                        index['interest_rate'] = update_rate
                        index['status'] = update_status

                        print("Cật nhập thành công ")
                        break
                    else: 
                        print("số tiền và ky hạn phải lớn hơn 0")
                else:
                    print("không tìm thấy ID cần cật nhập") 


        case '4': 
            # xoá 
            print("")
            print("=== Xoá sản phẩm === ")
            delete_id = input("Nhập id cần xoá : ").strip().upper()

            check = False

            for index  in saving_accounts:
                if index['account_id'] == delete_id : 
                    if index.get('status') == 'closed':
                        print (f"số {delete_id} đã được xoá ")
                    else: 
                        index['status'] = 'closed'
                        print(f"Đã tất toán thành công sổ: {delete_id}")
                        
                    check = True 
                    break
                
                if not check : 
                    print("không tim thấy id càn xoá")

        case '5' : 
            # cho người dùng nhập id và chuẩn hoá dữ liệu 
            # Kiểm tra mã sổ tiết kiệm mà người dùng vừa nhập 
            #  sau đó lọc status những trạng thái active 
            # tính lãi những trạng thái active
            # Hiển thị số tiền lãi vừa tính và tổng tiến khi đến hạn 

            # Nhập mã số tiết kiệm và chuẩn hóa
            input_id = input('Nhập mã số tiết kiệm cần tính lãi').strip().upper()
            check = False
            # Tìm số cần tính lãi
            for account in saving_accounts:
                if account['account_id'] == input_id:
                    check = True
                    # Kiểm tra trạng thái số
                    if(account['status'] == 'active'):
                        # Tính lãi và hiển thị tổng tiền
                        interest = account['balance']*account['interest_rate']/100*account['term_months']/12
                        total = account['balance'] + interest
                        print(f'Tiền lãi: {interest}, tiền thực nhận: {total}')
                    else:
                        # In thông báo nếu số inactive
                        print('Trạng thái số không active')
                    break
            if not check:
                # In thông báo nếu không tìm thấy
                print('Không tìm thấy số tiết kiệm')
            
        case '6':
            input_id = input('Nhập mã sổ tiết kiệm cần kiểm tra: ').strip().upper()
            check = False
            for account in saving_accounts:
                if account['account_id'] == input_id:
                    check = True
                    if account['status'] == 'closed':
                        print("Không thể thao tác với sổ tiết kiệm đã tất toán")
                        break
                    
                    try:
                        month = int(input('Nhập số tháng thực gửi: '))
                        if month <= 0:
                            print("Số tháng thực gửi không hợp lệ!")
                            break
                        
                        # Logic rút tiền
                        if month < account['term_months']:
                            rate = 0.5 # Lãi suất không kỳ hạn
                        else:
                            rate = account['interest_rate'] # Lãi suất ban đầu
                        
                        interest = account['balance'] * rate / 100 * month / 12
                        total = account['balance'] + interest
                        print(f'Tiền lãi: {interest:.2f}, tổng tiền: {total:.2f}')
                    except ValueError:
                        print("Số tháng phải là số nguyên!")
                    break
            if not check:
                print("Không tìm thấy mã sổ tiết kiệm")

        case '7':
            print("Thoát chương trình ")
            break
