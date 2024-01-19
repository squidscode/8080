CC=gcc
FLAGS=-std=c89
VM_EXE=./vm.out
RUN_ARGS="./tests/invaders/invaders.e"

.PHONY: clean run dis

all: 8080vm.out

8080vm.out: 8080vm.c disassembler.c
	$(CC) $(FLAGS) -o $(VM_EXE) $^

clean:
	rm -f *.out *.o *.exe

run:
	@make all >> /dev/null
	- $(VM_EXE) $(RUN_ARGS)
	@make clean >> /dev/null

dis: e.dis f.dis g.dis h.dis

e.dis: tests/invaders/invaders.e
	./vm.out $^ > disassembler/$@
f.dis: tests/invaders/invaders.f
	./vm.out $^ > disassembler/$@
g.dis: tests/invaders/invaders.g
	./vm.out $^ > disassembler/$@
h.dis: tests/invaders/invaders.h
	./vm.out $^ > disassembler/$@