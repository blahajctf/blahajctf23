#include <stdlib.h>
#include <stdio.h>


int main() {
    setbuf(stdout, NULL);
    setbuf(stdin, NULL);
    setbuf(stderr, NULL);

    int balance = 0;
    int in_stock[3] = {1, 1, 0};
    char choice[8];

    while (1) {
        printf("Current balance: $%d\n", balance);
        do {
            printf("1) Beg for money\n");
            printf("2) Visit shop\n");
            printf("3) Exit\n");
            gets(choice);
        } while (!('1' <= *choice && *choice <= '3'));
        printf("\n");

        if (*choice == '1') {
            int r = rand() % 10;
            if (r < 2) {
                printf("A kind stranger gave you some money!\n");
                balance += (rand() % 10);
            } else if (r == 3) {
                printf("Someone took your money :(\n");
                if (balance == 0) printf("...but you didn't have any to begin with.\n");
                else balance -= (rand() % (balance+1));
            } else {
                printf("You got ignored...\n");
            }
            if (balance < 0) balance = 0;
        } else if (*choice == '2') {
            printf("Welcome to the shop! What would you like to buy?\n");
            do {
                printf("1) Small blahaj (%sin stock) - $10\n", in_stock[0] ? "" : "not ");
                printf("2) Big blahaj (%sin stock) - $30\n", in_stock[1] ? "" : "not ");
                printf("3) Flag (%sin stock) - $2,147,483,647\n", in_stock[2] ? "" : "not ");
                gets(choice);
            } while (!('1' <= *choice && *choice <= '3'));
            if (!in_stock[*choice-'1']) {
                printf("Sorry! That item is out of stock :(\n");
                continue;
            }
            if (*choice-'0' == 1) {
                if (balance < 10) {
                    printf("Hey! You don't have enough money!\n");
                    continue;
                }
                balance -= 10;
                printf("Congratulations! You now have your very own small blahaj!\n");
            } else if (*choice-'0' == 2) {
                if (balance < 30) {
                    printf("Hey! You don't have enough money!\n");
                    continue;
                }
                balance -= 30;
                printf("Congratulations! You now have your very own big blahaj!\n");
            } else if (*choice-'0' == 3) {
                if (balance < 2147483647) {
                    printf("Hey! You don't have enough money!\n");
                    continue;
                }
                balance -= 2147483647;
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

    return 0;
}
