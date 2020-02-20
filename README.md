# CCC meant to:
- Compile .c .cpp .s source
- link it to .elf ARM binary image
- extract all the linked code
- and format it in AR cheat code form.

It really shows it potential if used in assotiation with IDA and python scripts:
it allow you to write compiled AR code ritgh in memory of debugging process,
to test it out imidiately.

## How to use:
There is 2 ways you can use it:
- see SECTIONS in linker.ld and change .jump for entry offset, edit jump.s to change dst
- ignore jump completely and set ENTRY to fun, or any other function

### Credits:
Made possible with help from:
@luigoalma
@Rafa10
@piepie62