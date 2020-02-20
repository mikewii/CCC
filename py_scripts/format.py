import sys

filename = sys.argv[1]
mode = sys.argv[2]

def start(): #open file to work with 
    f = open(filename, "r")
    of = open("out.txt", "w")
    return f, of

def end(f, of): #close both input and output files
    f.close()
    of.close()

def codeName(of, name):
    of.write(name + "\n")
            

def runFormat0(f, of):
    for line in f:
        if line.startswith("  "):
            line = line.split(" ")
            line = line[2].split(":")
            
            part1 = line[0]
            part2 = line[1].strip("\t")

            # fix offset lenght for AR standart, and to upper both parts
            while len(part1) < 8:
                part1 = "0" + part1.upper()
                part2 = part2.upper()

            combo = part1 + " " + part2 + "\n"
            of.write(combo)
            print(part2)
            #print(line[0])

def runFormatE(f, of):
    lines = f.read().splitlines()
    val = int(lines[-1].split(":")[0], 16)

    i = 0
    for line in lines:
        if line.startswith("  "):
            line = line.split(" ")
            line = line[2].split(":")

            # fix offset lenght for AR standard, and to upper both parts
            part2 = line[1].strip("\t").upper()
            if i == 0:
                part1 = '%08X' % int(line[0], 16)
                combo = part1 + " " + part2 + "\n"

            else:
                combo = part2 + (" " if (i & 1 != 0) else "\n")
                if i == 1:
                    part1 = int(line[0], 16)
                    combo = ('%08X %08X' % ((0xE0000000 | part1), (val - part1 + 4))) + "\n" + combo
            
            of.write(combo)
            print(part2)
            i = i + 1
            #print(line[0])
    
name = "[sample]"
f, of = start()
codeName(of, name)
runFormatE(f, of) if mode == "E" else runFormat0(f, of)
end(f, of)
