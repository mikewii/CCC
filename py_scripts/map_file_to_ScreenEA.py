def mapFile(f, addr):
    buf = f.read()
    f.close()
    write_dbg_memory(addr, buf)


filename = AskFile(0, '.', 'Select File')
f = open(filename, 'rb')
addr = ScreenEA()
mapFile(f, addr)
refresh_debugger_memory()
