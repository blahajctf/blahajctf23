#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

void setup() {
  setvbuf(stdin, NULL, _IONBF, 0);
  setvbuf(stdout, NULL, _IONBF, 0);
  setvbuf(stderr, NULL, _IONBF, 0);
}

int main() {
  setup();

  struct s {
    char var1[16];
    int n;
    char *end;
    char *ptr1;
  } stack;
  stack.n = 16;
  stack.end = malloc(0x100);
  strcpy(stack.end, "thanksbb");
  stack.ptr1 = stack.var1;

  puts("Enter your note: ");

  gets(stack.var1);

  puts("Received");
  memcpy(stack.ptr1, stack.var1, stack.n);
  puts(stack.end);
  exit(0);
}
