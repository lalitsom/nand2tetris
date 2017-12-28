// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)


@R0		//first variable var0 = Ram[0]
D=M

@var0
M=D

@R1		//second variable var1 = Ram[1]
D=M

@var1
M=D

@R2		//final output result=0
M=0

@i		//iterator i=0
M=0

(loop1)
	@i
	D=M
	@var1
	D=D-M
	@END
	D;JEQ	// i==var1 then end loop1 
	
	@R2		//result = result + var0
	D=M
	@var0
	D=D+M
	@R2
	M=D
	
	@i	//i=i+1
	M=M+1
	
	@loop1
	0;JMP		//goto loop1
	
(END)

(loop2)
@loop2
0;JMP		 // infinite loop