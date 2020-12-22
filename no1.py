def ubahHuruf(teks, a, b):
    datateks = list(teks)

    output = ''
    for hurufteks in datateks:
        if  hurufteks == a:
             hurufteks = b
        output = ''.join([output,hurufteks])
    return output

print(ubahHuruf('MATEMATIKA', 'T', 'S'))
