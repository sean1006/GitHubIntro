// template Program in C
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

// global variable for each language of hello world
char *string_array[] = {"Hello World", "世界好", "Hola Mundo", "Salve Mundi", "مرحبا بالعالم"};
int number_of_strings = 5;

int main()
{
  // use current time as seed for random generator
  srand(time(0));

  // prints out hello world in a random language out of the list above
  int random_number = rand() % number_of_strings;
  printf("%s\n", string_array[random_number]);
  return 0;
}
