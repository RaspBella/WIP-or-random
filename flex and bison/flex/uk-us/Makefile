run: compile
	./uk-us

compile: lex
	cc -lfl -o uk-us uk-us.yy.c

lex:
	lex -o uk-us.yy.c uk-us.l

clean:
	rm uk-us uk-us.yy.c
