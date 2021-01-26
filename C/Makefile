build:
	gcc -o hello_world hello_world.c
	gcc -o roll_dice roll_dice.c
	gcc quicksort_openmp.c -o quicksort_openmp -fopenmp -lm
clean:
	rm hello_world roll_dice quicksort_openmp
test: build
	./hello_world
	./roll_dice
	./quicksort_openmp