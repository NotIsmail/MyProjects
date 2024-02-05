// C PROJECT FOR SIMPLE CALCULATOR
#include <stdio.h>
int main()
{
    double number1;
    double number2;
    char operators;
    printf("enter first number:");
    scanf("%lf", &number1);

    while (getchar() != '\n')
        ;

    printf("Enter the operator:");
    scanf("%c", &operators);

    printf("Enter the second number:");
    scanf("%lf", &number2);

    switch (operators)
    {
    case '+':
        printf("%.lf+%.lf=%.lf", number1, number2, number1 + number2);
        break;
    case '-':
        printf("%.lf-%.lf=%.lf", number1, number2, number1 - number2);
        break;
    case '*':
        printf("%.lf*%.lf=%.lf", number1, number2, number1 * number2);
        break;
    case '/':
        printf("%.lf/%.lf=%.lf", number1, number2, number1 / number2);
        break;
    default:
        printf("Error,Invalid Input");
        break;
    }
}