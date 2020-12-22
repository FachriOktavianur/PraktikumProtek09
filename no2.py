int=(input('Masukkan jumlah baris : '))
def bintang(n):
    baris = 0
    bintang = 1
    panjang = 1 + 2*(n-1)
    panjang += panjang
    ruang = ' '
    while baris < n :
          bintang = '*' * (1 + (baris-1)*2)
          baris+=1
          bintang+=2
          print(bintang.center(panjang, ruang))
bintang(input_bintang)

bintang(4)
