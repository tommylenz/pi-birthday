#include <stdio.h>

int outputBars(int grades[]);

int main(int argc, char* argv)
{
    if (argc == 1) //If you got 10 grades to eval
    {
        // Get grades:
        int grades[10], sum;
        float av, raw;
        for (int i = 0; i < 10; i++)
        {
            printf("Grade #%i: ", i + 1);
            int grade;
            scanf("%d", &grade);
            grades[i] = grade;
        }
        for (int i = 0; i < 10; i++)
        {
            sum += grades[i];
        }
        printf("SUM: %i", sum);
        av = sum / 10;
        raw = sum / 44 * 40;
        printf("\nInsgesamt hast du %i Punkte erziehlt.\n", sum);
        printf("Deine Noten sehen so aus:\n");
        outputBars(grades);
        printf("Das enspricht %f Rohpunkten fuer dein Abitur.\n", raw);
        printf("Dein Notendurchschnitt betraegt: %f Punkte\n", av);
        return 0;
    }
    else //If you got any number of grades but 10
    {
        printf("Sorry, that's not supported at the time.\n");
        printf("Try again without another parameter.\n");
        return 1;
    }
}

int outputBars(int grades[])
{
    printf("\n");
    for (int i = 0; i < 10; i++)
    {
        int grade = grades[i];
        if (i < 9)
        {
            printf(" %i: ", i + 1);
        }
        else
        {
            printf("%i: ", i + 1);
        }

        for (int j = 0; j < grade; j++)
        {
            printf("#");
        }
        printf("\n");
    }
    printf("\n");
}
