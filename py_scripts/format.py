import sys

filename = sys.argv[1]

def start(): #open file to work with 
    f = open(filename, "r")
    of = open("out.txt", "w")
    return f, of

def end(f, of): #close both input and output files
    f.close()
    of.close()

def codeName(of, name):
    of.write(name + "\n")
            
def runFormat(f, of):
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
    
name = "[sample]"
f, of = start()
codeName(of, name)
runFormat(f, of)
end(f, of)
