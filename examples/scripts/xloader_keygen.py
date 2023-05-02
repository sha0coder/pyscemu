import pyscemu
import sys

emu = pyscemu.init32()
emu.load_maps('/home/sha0/src/scemu/maps32/')
emu.load_binary('/home/sha0/samples/formbook/xloader/2022-10-05/unpacked.bin')

buff = emu.alloc("struct_buff", 1024*2)


xloader_key1_keygen = 0x3DB687
key_off = 1980
prekey_off = 1096

emu.set_verbose(3)
#emu.spawn_console_at_pos(6)
eax = emu.call32(xloader_key1_keygen, [buff])

print('RC4 Key1:')
emu.dump_n(buff+key_off, 20)

