run: compile
	./flex-scanner

compile: lex
	cc -lfl -o flex-scanner flex-scanner.yy.c

lex:
	lex -o flex-scanner.yy.c flex-scanner.l

clean:
	rm flex-scanner flex-scanner.yy.c
