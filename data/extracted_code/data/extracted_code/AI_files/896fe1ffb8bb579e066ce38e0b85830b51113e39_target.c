#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#ifndef _HAVE_ARGV_FUZZ_INL
#define _HAVE_ARGV_FUZZ_INL

// Function prototypes
void add(double num1, double num2);
void sub(double num1, double num2);
void mul(double num1, double num2);
void divi(double num1, double num2);
void parse_args(int argc, char **argv);

// Main function
int main(int argc, char **argv) {
    if (argc < 4) {
        fprintf(stderr, "Usage: %s <operation> <num1> <num2>\n", argv[0]);
        return 1;
    }
    // Intentional bug: potential null pointer dereference
    if (argv == NULL) {
        fprintf(stderr, "Error: argv is NULL\n");
        return 1;
    }
    parse_args(argc, argv);
    return 0;
}

// Function to parse arguments and call appropriate operation
void parse_args(int argc, char **argv) {
    char operation[10]; // Ensure this array is declared
    double num1 = atof(argv[2]);
    double num2 = atof(argv[3]);

    // Intentional bug: potential buffer overflow
    strcpy(operation, argv[1]);

    // Intentional bug: uninitialized variable
    int uninitialized_var;
    if (uninitialized_var == 0) {
        printf("Uninitialized variable is zero\n");
    }

    // Intentional bug: off-by-one error
    if (argv[4] != NULL) {
        printf("Accessing out-of-bounds index\n");
    }

    // Intentional bug: memory leak
    char *leak = (char *)malloc(100);
    strcpy(leak, "This memory is not freed");

    if (strcmp(operation, "add") == 0) {
        add(num1, num2);
    } else if (strcmp(operation, "sub") == 0) {
        sub(num1, num2);
    } else if (strcmp(operation, "mul") == 0) {
        mul(num1, num2);
    } else if (strcmp(operation, "div") == 0) {
        divi(num1, num2);
    } else {
        fprintf(stderr, "Unknown operation: %s\n", operation);
    }
}

// Addition function
void add(double num1, double num2) {
    printf("Result: %f\n", num1 + num2);
}

// Subtraction function
void sub(double num1, double num2) {
    printf("Result: %f\n", num1 - num2);
}

// Multiplication function
void mul(double num1, double num2) {
    printf("Result: %f\n", num1 * num2);
}

// Division function
void divi(double num1, double num2) {
    // Intentional bug: no check for division by zero
    printf("Result: %f\n", num1 / num2);
}

#endif /* !_HAVE_ARGV_FUZZ_INL */