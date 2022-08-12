simple-calculator:	simple-calculator.l simple-calculator.y
	bison -d simple-calculator.y
	flex simple-calculator.l
	cc -o $@ simple-calculator.tab.c lex.yy.c -lfl

clean:
	rm *tab* lex.yy.c
