import random
import shutil
import FMapDat_lists as fmd

shutil.copyfile("FMapDat-ReadOnly/FMapDat.dat", "FMapDat-Randomized/FMapDat.dat")
data = fmd.Locations
shuffled = list(data.values())
random.shuffle(shuffled)
x = dict(zip(data, shuffled))
z = list(x.values())
listaddress = list(x.keys())

print(listaddress[1])
with open("FMapDat-Randomized/FMapDat.dat", mode="r+b") as f:
    i = 0
    while i < 632:
        if listaddress[i] != 0x0EC835B0:
            if listaddress[i] + 0xC == listaddress[i+1]:
                bincorrect = z[i] & 0xFEFFFFFF
                f.seek(listaddress[i])
                f.write(int(bincorrect).to_bytes(4))
                print("0x%.8x: %.8x" % (listaddress[i], bincorrect))
            else:
                bincorrect = z[i] | 0x01000000
                f.seek(listaddress[i])
                f.write(int(bincorrect).to_bytes(4))
                print("0x%.8x: %.8x (end)" % (listaddress[i], bincorrect))
        else:
            bincorrect = z[i] | 0x01000000
            f.seek(listaddress[i])
            f.write(int(bincorrect).to_bytes(4))
            print("0x%.8x: %.8x (end)" % (listaddress[i], bincorrect))
        i += 1