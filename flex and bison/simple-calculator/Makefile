default:
	bison -d simple-calculator.y
	flex -o simple-calculator.yy.c simple-calculator.l
	cc -o simple-calculator simple-calculator.tab.c simple-calculator.yy.c -lfl

clean:
	rm simple-calculator{,.yy.c,.tab.?}
