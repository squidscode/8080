/* gcc -std=c89 -o runtime.out runtime.c */

#include <assert.h>
#include <stdio.h>
#include <stdlib.h>

#include "8080vm.h"
#include "disassembler.h"

int main(int argc, char** argv) {
    if (argc != 2) print_help_message();
    FILE *f = fopen(argv[1], "r");
    fseek(f, 0L, SEEK_END);
    long sz = ftell(f);
    fseek(f, 0L, SEEK_SET);
    char *file_contents = (char*) malloc(sz);
    long i = 0L;
    printf("File size: %ld\n", sz);
    while(i < sz) {
        file_contents[i] = fgetc(f);
        i += 1;
    }
    size_t pc = 0;
    while(pc < sz) {
        pc += disassemble((unsigned char*) file_contents, pc);
    }
    return 0;
}

void print_help_message() {
    printf(
        "Usage: 8080vm file_name\n"
    );
    exit(1);
}