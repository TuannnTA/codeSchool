# cho danh sách A
# tìm giá trị lớn nhất của danh sách A và in nó ra màn hình

A = [5, 7, 3, 8, 9, 4]

gtln = A[0]

for i in range(len(A)):
    if A[i] > gtln:
        gtln = A[i]
        
print(gtln)
