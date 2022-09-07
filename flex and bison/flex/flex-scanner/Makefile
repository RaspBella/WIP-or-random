default:
	lex -o flex-scanner.yy.c flex-scanner.l
	cc -lfl -o flex-scanner flex-scanner.yy.c

clean:
	rm flex-scanner flex-scanner.yy.c
