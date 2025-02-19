# cho danh sách B
# tìm giá trị nhỏ nhất của danh sách B và in nó ra màn hình

B = [5, 7, 3, 8, 9, 4]

gtnn = B[0]

for i in range(len(B)):
    if B[i] < gtnn:
        gtnn = B[i]
        
print(gtnn)
