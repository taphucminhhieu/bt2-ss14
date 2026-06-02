# # Biến toàn cục lưu tổng điểm hiện tại của khách hàng
# total_points = 100

# # Hàm cộng điểm thưởng
# def add_reward_points(points_earned):
#     # Cố gắng lấy tổng điểm cũ cộng thêm điểm mới
#     total_points = total_points + points_earned
#     print("Đã cộng thêm", points_earned, "điểm.")

# # Khách mua hàng được thưởng 50 điểm
# add_reward_points(50)

# # In ra kết quả
# print("Tổng điểm hiện tại của khách hàng:", total_points)

# phân tích 
# Biến total_points ở dòng 2 là biến toàn cục (Global) vì nó được khai báo ở cấp độ cao nhất của chương trình, nằm ngoài phạm vi bất kỳ hàm nào.
# Thông báo UnboundLocalError xảy ra vì Python thấy phép gán = bên trong hàm nên mặc định coi biến đó là cục bộ, nhưng bạn lại cố gắng đọc giá trị của nó ở vế phải trước khi kịp gán giá trị mới cho nó.
# Python coi biến đó là cục bộ ngay khi thấy lệnh gán = bên trong hàm, vì quy tắc thiết kế của Python là ưu tiên cô lập dữ liệu bên trong hàm để tránh xung đột không mong muốn.
# Nếu chỉ muốn đọc (print) mà không thay đổi (gán) biến toàn cục bên trong hàm, chương trình sẽ không bị lỗi vì Python sẽ tự động tìm biến ở phạm vi bên ngoài nếu không tìm thấy trong hàm.
# Cách sửa 1: Sử dụng từ khóa global với dòng lệnh: global total_points.
# Cách sửa 2: Một hàm tốt nên dùng lệnh return để trả về giá trị tổng điểm mới cho chương trình chính. 

# sửa code : sửa theo cách 2
total_points = 100

def add_reward_points(current_points, points_earned):
    return current_points + points_earned

# Cập nhật biến ở ngoài phạm vi hàm
total_points = add_reward_points(total_points, 50)

print("Tổng điểm hiện tại:", total_points)