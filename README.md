# CCC is meant to:
- Compile .c .cpp .s source
- link it to .elf ARM binary image
- extract all the linked code
- and format it to out.txt in AR cheat code form:

[name] \
XXXXXXXX YYYYYYYY \
where: \
XXXXXXXX - offset \
YYYYYYYY - ARM instruction, or value, in little endian

It really shows it potential if used in assotiation with IDA and python scripts:
it allow you to write compiled AR code ritgh in memory of debugging process,
to test it out imidiately.

## How to use:
Prerequirements: DevkitARM must be installed in your environment \
Simply run make after setup.

There is 2 ways you can setup it:
- see SECTIONS in linker.ld and change .jump for entry offset, edit jump.s to change dst
- ignore jump completely and set ENTRY to fun, or any other function

### Credits:
Made possible with help from, in no particular order: \
@luigoalma \
@Rafa10 \
@piepie62
