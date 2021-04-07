# menampilkan informasi program
print('Program Menghitung Rata-Rata')
print('============================')
# input data
data = []
total = 0
n = int(input('masukkan banyaknya elemen data: '))
for x in range(n):
    nilai = float(input('masukkan nilai ke-{} : '.format(x+1)))
    data.append(nilai)

print('\n hasil nilai total adalah : {} '.format(sum(data)))
print('\n hasil rata-rata adalah : {} '.format(sum(data)/n))
