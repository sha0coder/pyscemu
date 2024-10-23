import pyscemu
import sys

emu = pyscemu.init64()
emu.load_maps('/Users/jesus/src/scemu/maps64/')
emu.load_binary('msedge_exe_PID1530_codechunk_225DB910000_x64.dll')


comm_protocol = 0x225db9138e0

emu.set_verbose(0)
count = 0


def GetUserNameA():
    retaddr = emu.stack_pop64()
    print('GetUserNameA')
    emu.write_string(emu.get_reg('rcx'), 'baremetal\x00')
    emu.write_qword(emu.get_reg('rdx'), 9)
    emu.set_reg('rax', emu.get_reg('rcx'))

def recv():
    retaddr = emu.stack_pop64()
    rip = emu.get_reg('rip')
    rcx = emu.get_reg('rcx')
    rdx = emu.get_reg('rdx')
    r8 = emu.get_reg('r8')
    print(f'{rip:x}: recv({rcx}, {rdx:x}, {r8})')
    emu.write_dword(rdx, 3)
    emu.set_reg('rax', 4)


emu.set_reg('rip', comm_protocol)
while True:
    addr, name = emu.run_until_apicall()
    if name == 'getusernamea':
        GetUserNameA()
    elif name =='recv':
        recv()
    else:
        emu.handle_winapi(addr)


