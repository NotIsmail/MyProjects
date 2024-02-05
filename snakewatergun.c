#include <stdio.h>
#include <time.h>
#include <stdlib.h>
int snakewatergun(int you, int comp)
{
    if (you == comp)
    {
        return 0;
    }
    else if ((you == 's' && comp == 'w') || (you == 'w' && comp == 'g') || (you == 'g' && comp == 's'))
    {
        return 1;
    }
    else
    {
        return -1;
    }
}
int main()
{
    char you, comp;
    srand(time(0));
    int num = rand() % 100 + 1;
    if (num < 33)
    {
        comp = 's';
    }
    else if (num < 66)
    {
        comp = 'w';
    }
    else
    {
        comp = 'g';
    }
    printf("Type To Choose : S for snake,W for water,G for gun\n ");
    scanf("%c", &you);
    int result = snakewatergun(you, comp);
    if (result == 0)
    {
        printf("The Game Is Drawn\n");
    }
    else if (result == 1)
    {
        printf("You Win\n");
    }
    else
    {
        printf("You Lose\n");
    }
    printf("You Chose %c and Your Opponent Chose %c\n", you, comp);
}