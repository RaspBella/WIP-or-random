run: compile
	./wc

compile: lex
	cc -lfl -o wc wc.yy.c

lex:
	lex -o wc.yy.c wc.l

clean:
	rm wc wc.yy.c
