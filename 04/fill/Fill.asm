// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

(RECHECK)
@KBD
D=M
@BLACK		//make screen blank if D!=0
D;JNE

(WHITE) //make screen white
@i		//iterator i = 0
M=0
	(LOOP1)
		@8192		//if i == 8192 break
		D=A
		@i
		D=D-M
		@ENDLOOP1
		D;JEQ
		
		@i		//M=Screen + i
		D=M
		@SCREEN
		A = A+D
		M=0
		
		@i		//i=i+1
		M=M+1
		@LOOP1
		0;JMP
	(ENDLOOP1)

@RECHECK
0;JMP	

(BLACK) //make screen black
@i		//iterator i = 0
M=0
	(LOOP2)
		@8192		//if i == 8192 break
		D=A
		@i
		D=D-M
		@ENDLOOP2
		D;JEQ
		
		@i		//M=Screen + i
		D=M
		@SCREEN
		A = A+D
		M=-1
		
		@i		//i=i+1
		M=M+1
		@LOOP2
		0;JMP
	(ENDLOOP2)

@RECHECK
0;JMP