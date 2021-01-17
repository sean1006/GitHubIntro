// template Program in C
#include <stdio.h>
#include <stdlib.h>
#include <getopt.h>
#include <time.h>

// global variable for each type of dice
int dice[] = {4, 6, 8, 10, 12, 20};
int dice_len = 6;
int max_num_dice = 1000;

// check if input was valid dice type
int valid_dice(int dice_type)
{
    int i;
    for (i = 0; i < dice_len; i++) {
        if (dice_type == dice[i]) {
            return 1;
        }
    }
    return 0;
}

// check if input was valid number of dice
int valid_num_dice(int num_dice)
{
    if (num_dice < 1 || num_dice > max_num_dice) {
        return 0;
    }
    return 1;
}

void initialize_random()
{
    srand(time(0));
}

// roll the dice and print out the numbers to stdout
void roll_dice(int dice_type, int num_dice)
{
    fprintf(stdout, "Dice Results: ");

    int total_roll = 0;
    int i;
    for (i = 0; i < num_dice; i++) {
        int roll = rand() % dice_type + 1;
        fprintf(stdout, "%d ", roll);
        total_roll += roll;
    }

    fprintf(stdout, "\nTotal Roll: %d\n", total_roll);
}

int main(int argc, char *argv[])
{
    // set up command line options
    static struct option long_options[] = {
        {"dice",    optional_argument, 0, 'd'},
        {"number",  optional_argument, 0, 'n'},
        {0, 0, 0, 0}
    };
    
    // set up default values for program
    int dice_type = 6;
    int num_dice = 1;

    // read in arguements
    int input;
    while (1) {
        input = getopt_long(argc, argv, "", long_options, 0);
        if (input == -1) {
            // if no input is given
            break;
        }
        switch (input) {
            case 'd':
                if (valid_dice(atoi(optarg))) {
                    dice_type = atoi(optarg);
                } else {
                    fprintf(stderr, "Invalid type of dice: Please enter %d, %d, %d, %d, %d, or %d\n", 4, 6, 8, 10, 12, 20);
                    return 0;
                }
                break;
            case 'n':
                if (valid_num_dice(atoi(optarg))) {
                    num_dice = atoi(optarg);
                } else {
                    fprintf(stderr, "Invalid number of dice: Please enter a number between 1 and %d\n", max_num_dice);
                    return 0;
                }
                break;
            default:
                // other invalid arguements
                fprintf(stderr, "Bad arguement: You can use \"d\" to specify the type of dice and \"n\" to specify the number of dice\n");
                return 0;
        }
    }

    initialize_random();
    roll_dice(dice_type, num_dice);

    return 0;
}
