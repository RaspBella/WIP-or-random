run: compile
	./simple-calculator

compile: lex
	cc -lfl -o simple-calculator simple-calculator.yy.c

lex:
	lex -o simple-calculator.yy.c simple-calculator.l

clean:
	rm simple-calculator simple-calculator.yy.c
