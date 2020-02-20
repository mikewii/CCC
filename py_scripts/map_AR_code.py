def swapEndian(hex):
    hex = hex.strip().decode('hex')
    hex = hex[3] + hex[2] + hex[1] + hex[0]
    return hex

def mapCode(f):
    for line in f:
        if not line.startswith('[') | line.startswith(' '):
            line = line.strip('\r\n')
            list = line.split( )
            opcode = list[1]
            opcode = swapEndian(opcode)
            DbgWrite(addr, opcode)
            addr += 4

filename = AskFile(0, '.txt', 'Select AR code')
f = open(filename, 'r')
mapCode(f)
RefreshDebuggerMemory()