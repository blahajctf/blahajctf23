#include <stdio.h>

int main() {
    setbuf(stdout, NULL);
    setbuf(stdin, NULL);
    setbuf(stderr, NULL);

    char data[40];
    void (*warp)();

    printf("CURRENT POSITION: %p\nWARP TO:", &warp);
    fgets(data, 40, stdin);
    sscanf(data, "%p", &warp);

    warp();
    return 0;
}