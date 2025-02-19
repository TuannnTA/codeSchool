# cho danh sách A
# xóa phần tử giữa danh sách nếu số phần tử của A lẻ
# in ra màn hình các giá trị của A

A = [1, 3, 3, 5, 7, 9, 9]

if len(A) % 2 == 1:
    del A[int( len(A)/2 )]

for i in range(len(A)):
    print(A[i], end=" ")
        
