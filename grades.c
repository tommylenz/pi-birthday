#include <stdio.h>

int outputBars(int grades[]);

int main(int argc, char* argv)
{
    if (argc == 1) //If you got 10 grades to eval
    {
        // Get grades:
        int grades[10], sum = 0;
        float raw, jump, av;
        for (int i = 0; i < 10; i++)
        {
            printf("Grade #%i: ", i + 1);
            int grade;
            scanf("%d", &grade);
            grades[i] = grade;
            sum += grade;
        }
        printf("Insgesamt hast du %i Punkte erzielt.\n", sum);

        printf("Deine Noten sehen so aus:\n");
        outputBars(grades);

        raw = (float) sum / 44 * 40;
        int clean_raw = (int)(raw + 0.5);
        printf("Das enspricht %i Rohpunkten fuer dein Abitur, ", clean_raw);
        jump = (float) clean_raw / 17;
        int clean_jump = (int)(jump + 0.5);
        printf("womit du %i Kommaspruenge gemacht hast.\n", clean_jump);

        av = (float) sum / 10;
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
