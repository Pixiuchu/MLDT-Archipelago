import random
import shutil
import FMapDat_lists as fmd

with open("00040000000D9000_v00.standard.cia", mode="rb") as f:
    ### Copy FMapDat.dat from .cxi
    f.seek(0x07636F60)
    copyfmapdat = f.read(0x14CFF000)
    fmdfile = open("FMapDat-Randomized/FMapDat.dat", mode="w+b")
    fmdfile.write(copyfmapdat)

data = fmd.Locations
shuffled = list(data.values())
random.shuffle(shuffled)
x = dict(zip(data, shuffled))
z = list(x.values())
listaddress = list(x.keys())

#print(listaddress[1])
### Randomize the blocks --- no beans, no sneeze-blocks: they need their own checking so that they don't become blocks.
#### Logic needs to be added: Luigi blocks should not be in Mini Mario areas, these are inaccessible without glitches.
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