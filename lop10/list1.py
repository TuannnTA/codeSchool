# cho danh sách B
# thêm phần tử 7 vào cuối danh sách nếu số phần tử của B chẵn
# in ra màn hình các giá trị của B

B = [1, 3, 3, 55, 7, 9, 9]

if len(B) % 2 == 0:
    B.append(7)

for i in range(len(B)):
    print(B[i], end=" ")
        

