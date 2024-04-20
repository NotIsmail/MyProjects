#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main()
{
    int number, guess, nguesses = 1;
    srand(time(0));
    number = rand() % 100 + 1;
    // printf("The Number Is :%d", number);
    do
    {
        printf("Guess The Number Between 1 to 100\n ");
        scanf("%d", &guess);
        if (guess > number)
        {
            printf("Little Lower\n");
        }
        else if (guess < number)
        {
            printf("A Little  Higher\n");
        }
        else
        {
            printf("Bingo, You Got It Right\n Your  Attempts %d", nguesses);
        }
     nguesses++;

    } while (guess != number);
}
