#include <stdio.h>
#include <ctype.h>
#include <unistd.h>

#define RED   "\x1B[31m"
#define GRN   "\x1B[32m"
#define YEL   "\x1B[33m"
#define BLU   "\x1B[34m"
#define MAG   "\x1B[35m"
#define CYN   "\x1B[36m"
#define WHT   "\x1B[37m"
#define GRY   "\x1B[90m"
#define RESET "\x1B[0m" // 从 https://stackoverflow.com/questions/3585846/

#define top(n) { printf("┌"); for (int i=1; i<n; i++) { printf("────┬"); } printf("────┐\n"); }
#define bot(n) { printf("└"); for (int i=1; i<n; i++) { printf("────┴"); } printf("────┘\n"); }

#define BOLD "\x1B[1m"
#define ITAL "\x1B[3m"

#define CR "\r"

#define LEN 24 //should be 24
#define L0 8
#define L1 12
#define L2 16
#define L3 20

#define CODE1 "\n\
"GRY"  17   │             "CYN"printf"RESET"("YEL"\"1) Beg for money\\n\""RESET");\n\
"GRY"  18   │             "CYN"printf"RESET"("YEL"\"2) Visit shop\\n\""RESET");\n\
"GRY"  19   │             "CYN"printf"RESET"("YEL"\"3) Exit\\n\""RESET");\n\
"GRY"  20   │             "CYN BOLD"gets"RESET"(choice);"

#define CODE2 "\n\
"GRY"  10   │     "CYN"int"RESET" balance "RED"= "MAG"0"RESET";\n\
"GRY"  11   │     "CYN"int"RESET" in_stock["MAG"3"RESET"] "RED"="RESET" {"MAG"1"RESET", "MAG"1"RESET", "MAG"0"RESET"};\n\
"GRY"  12   │     "CYN"char"RESET" choice["MAG"8"RESET"];"

#define CODE3 GRY"\n\
  10   │     "RED BOLD"int balance "RESET GRY"= "RED BOLD"0"RESET GRY";\n\
  11   │     int"BOLD" in_stock[3] "RESET GRY"= {"BLU BOLD"1"RESET GRY", "GRN BOLD"1"RESET GRY", "YEL BOLD"0"RESET GRY"};\n\
  12   │     "WHT BOLD"char choice[8]"RESET GRY";"RESET

#define CODE4 "\n\
"GRY"  45   │             "RED"if"RESET" ("RED"!"RESET"in_stock["RED"*"RESET"choice"RED"-"YEL"'1'"RESET"]) {\n\
"GRY"  46   │                 "CYN"printf"RESET"("YEL"\"Sorry! That item is out of stock :(\\n\""RESET");\n\
"GRY"  47   │                 "RED"continue"RESET";\n\
"GRY"  48   │             "RESET"}"

#define wait() { printf("\n<PRESS ENTER TO CONTINUE>"); fflush(stdout); getchar(); printf("\x1B[1F\x1B[2K"); fflush(stdout); }
#define clear() { printf("\x1B[2J\x1B[;H"); fflush(stdout); }

#define stack(arr, fmt, str) { \
    printf(RED fmt RESET,  str); \
    puts(""); \
    top(LEN); \
\
    printf("│"); \
    for (int i=0; i<LEN; i++) { \
        printf(i<L0 ? WHT : (i<L1 ? BLU : (i<L2 ? GRN : (i<L3 ? YEL : RED)))); \
        printf(BOLD " %02x " RESET "│", arr[i]); \
    } \
\
    printf("\n"); \
    bot(LEN); \
    printf("   " CYN BOLD); \
        for (int i=0; i<LEN; i++) { \
            if isprint(arr[i]) { \
                printf("%-5c", arr[i]); \
            } else { \
                printf("%-5c", ' '); \
            } \
        } \
    printf(RESET "\n\n"); \
}

#define cstack(arr, fmt, str) { clear(); stack(arr, fmt, str); }

#define STKSTR1 RESET"lower >---------------------------------------------stack direction----------------------------------------------> higher"
#define STKSTR2 BOLD "  "WHT"choice                                  "BLU"in_"GRN"sto"YEL"ck                                                    "RED"balance"RESET

#define dstack(arr) cstack(arr, "%s", STKSTR1"\n"STKSTR2)
#define zero(arr) { arr[0]='\x00'; arr[1]='\x00'; arr[2]='\x00'; arr[3]='\x00'; arr[4]='\x00'; arr[5]='\x00'; arr[6]='\x00'; arr[7]='\x00'; }


int cchal() {
    int balance = 0; // sTOP MOVING
    int in_stock[3] = {1, 1, 0};
    unsigned char choice[8];
    
    chal(&balance, in_stock, choice);
}

int chal(int* balance, int* in_stock, unsigned char* choice) {

    zero(choice);
    dstack(choice);

    while (1) {
        printf("Current balance: $%d\n", *balance);
        do {
            printf("1) Beg for money\n");
            printf("2) Visit shop\n");
            printf("3) Exit\n");

            gets(choice);
            dstack(choice);

        } while (!('1' <= *choice && *choice <= '3'));
        printf("\n");

        if (*choice == '1') {
            int r = rand() % 10;
            if (r < 2) {
                

                *balance += (rand() % 10);
                dstack(choice);
                printf("A kind stranger gave you some money!\n");

            } else if (r == 3) {
                
                if (*balance == 0) { printf("Someone took your money :(\n"); printf("...but you didn't have any to begin with.\n"); }
                else { *balance -= (rand() % (*balance+1)); dstack(choice); printf("Someone took your money :(\n"); }
            } else {
                printf("You got ignored...\n");
            }
            if (*balance < 0) *balance = 0;
        } else if (*choice == '2') {
            printf("Welcome to the shop! What would you like to buy?\n");
            do {
                printf("1) Small blahaj (%sin stock) - $10\n", in_stock[0] ? "" : "not ");
                printf("2) Big blahaj (%sin stock) - $30\n", in_stock[1] ? "" : "not ");
                printf("3) Flag (%sin stock) - $2,147,483,647\n", in_stock[2] ? "" : "not ");

                gets(choice);
                dstack(choice);

            } while (!('1' <= *choice && *choice <= '3'));
            if (!in_stock[*choice-'1']) {
                printf("Sorry! That item is out of stock :(\n");
                continue;
            }
            if (*choice-'0' == 1) {
                if (*balance < 10) {
                    printf("Hey! You don't have enough money!\n");
                    continue;
                }
                *balance -= 10;
                dstack(choice);

                printf("Congratulations! You now have your very own small blahaj!\n");
            } else if (*choice-'0' == 2) {
                if (*balance < 30) {
                    printf("Hey! You don't have enough money!\n");
                    continue;
                }
                *balance -= 30;
                dstack(choice);

                printf("Congratulations! You now have your very own big blahaj!\n");
            } else if (*choice-'0' == 3) {
                if (*balance < 2147483647) {
                    printf("Hey! You don't have enough money!\n");
                    continue;
                }
                *balance -= 2147483647;
                dstack(choice);
                
                printf("Congratulations! You now have your very own flag!\n");
                FILE* fptr;
                fptr = fopen("./flag.txt", "r");
                if (fptr == NULL) {
                    printf("Oops, something bad happened... please make a ticket!");
                }
                char flag[50];
                fgets(flag, 50, fptr);
                printf("Here's your flag: %s\n", flag);
            }

        } else if (*choice == '3') {
            return 0;
        }
        printf("\n");
    }
}

int main() {
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);

    int balance = 0;
    int in_stock[3] = {1, 1, 0};
    unsigned char choice[8];

    puts("Hey, you actually showed up.");
    puts("So here's the plan:");

    puts("if you remember the source code for the shop, it used "BOLD CYN"gets"RESET", which is known to be weak against a "ITAL"buffer overflow"RESET" attack:");
    puts(CODE1);
    puts(" ");
    wait();

    puts("What's a buffer overflow attack, you ask?");
    puts("well, I think it might be best to illustrate with a diagram:");
    sleep(0.5);
    puts("give me a sec");

    clear();
    puts("");
    stack(choice, "%s", " ");
    puts("this little diagram shows a portion of "BOLD"the stack"RESET", a region of memory where local variables are stored.");
    wait();
    puts("you might remember this snippet of code from the source, where some variables were initialised:");
    // sleep(1);
    puts(CODE2);
    wait();

    printf("\x1B[s\x1B[;H");
    fflush(stdout);
    printf(STKSTR1);
    printf("\x1B[1E");
    fflush(stdout);
    printf(STKSTR2);
    printf("\x1B[9E");
    fflush(stdout);
    puts(CODE3);
    printf("\x1B[u");
    fflush(stdout);
    

    printf("illustrated above are their locations on the stack: "WHT BOLD"choice"RESET", being a 8 char array, takes up 8 bytes; "BLU BOLD"in_"GRN"sto"YEL"ck"RESET" & "RED BOLD"balance"RESET", on the other hand, are each 32-bit integers which only take up 4.");
    wait();
    printf("values are pushed onto the stack from top to bottom: variables declared earlier will have higher addresses than those declared later.");
    wait();
    printf("however, buffers (like "WHT BOLD"choice"RESET") grow from bottom to top, towards higher addresses:");
    wait();

    sprintf(choice, "%s", "hello");
    dstack(choice);
    printf("here, i have entered \"hello\" into the "WHT BOLD"choice"RESET" buffer, using "BOLD CYN"gets"RESET".");
    wait();
    puts("but "BOLD CYN"gets"RESET" has no limit on the number of characters it reads; it reads until a newline (\\x20) or EOF.");
    puts("as such, what would happen if we tried to get more than 8 chars into "WHT BOLD"choice"RESET"?");
    wait();

    sprintf(choice, "%s", "binary exploitation");
    dstack(choice);
    printf("aha! It keeps writing characters even after the buffer ends, \"overflowing\" into "BLU BOLD"in_"GRN"sto"YEL"ck"RESET" & "RED BOLD"balance"RESET"!");
    wait();
    printf("this is the essence of a "ITAL"buffer overflow attack"RESET" -- we overflow a buffer to overwrite values stored higher in the stack.");
    wait();
    puts("in fact, we have already found a use for this exploit! Refer back to the code that checks whether an item is in stock:");
    puts(CODE4);
    puts(" ");
    puts("it may not be obvious at first glance, but it only checks if its "BLU BOLD"in_"GRN"sto"YEL"ck"RESET" if 0 for each item. \nAs such, overwriting "BLU BOLD"in_"GRN"sto"YEL"ck"RESET" of each item to be anything other than 0 has made it become in stock!");
    wait();
    puts("anyhow, that's all the time I have to teach you.");
    puts("I'll let you keep the stack viewer, just as a memento.");
    puts("now go get that flag!");
    wait();

    cchal();

    return 0;
}