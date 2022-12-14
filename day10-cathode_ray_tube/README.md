# Day 10 - Cathode Ray Tube
Given a list of instructions - either no-operation or add value to X. The former taken one clock cycle, the latter two and is implemented at the end of the clock cycles.

All quite straight-forward today.

## Part 1
We want to find the register value at cycle 20, 60, 100... The register value needs to be multiplied by the cycle no and then all of these will be added.

The issue here is keeping track of the cycle number and register number when you jump 2 at a time with an `addx` instruction. The solution is quite simple.


## Part 2
Find all the cycles where the register is within 1 either side of the cycle number (corrected to 1 line so reduced down with modulo)
and use it to draw an image.
