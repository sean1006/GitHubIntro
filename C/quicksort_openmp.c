// template Program in C using OpenMP
#include <stdio.h>
#include <stdlib.h>
#include <omp.h>
#include <time.h>


// helper functions

void initialize_random()
{
    srand(time(0));
}

void print_int_array(int *a, int n) {
    for (int i = 0; i < n; i++) {
        printf("%i ", a[i]);
    }
    printf("\n");
}

// output basic information to show if openmp is working,
// will output each thread id as well as total num physical processors
int openmp_info() {
    int thread_id = omp_get_thread_num();
    int num_threads = omp_get_num_threads();
    int num_processors = omp_get_num_procs();
    printf("thread id: %i of %i with %i cores\n", thread_id, num_threads, num_processors);
    return 1;
}

// quicksort implements the quick sort algorithm
void quicksort(int *a, int p, int r) {
    // printf("thread num: %i, %i, %i\n", omp_get_thread_num(), p, r - p);
    if (r > p) {
        int pivot = a[r];
        int i = p - 1;
        for (int j = p; j < r; j++) {
            if (a[j] < pivot) {
                i++;
                int t = a[i];
                a[i] = a[j];
                a[j] = t;
            }
        }
        int t = a[i + 1];
        a[i + 1] = a[r];
        a[r] = t;
        #pragma omp task
        quicksort(a, p, i);
        #pragma omp task
        quicksort(a, i + 2, r);
    }
}

// test the quicksort algorithm
void test_quicksort() {
    int LENGTH_ARRAY = 10;
    int arr[LENGTH_ARRAY];

    // setup testing
    initialize_random();
    for (int i = 0; i < LENGTH_ARRAY; i++) {
        arr[i] = rand() % LENGTH_ARRAY + 1;
    }
    print_int_array(arr, LENGTH_ARRAY);

    // sort
    #pragma omp parallel
    {
        #pragma omp single
        quicksort(arr, 0, LENGTH_ARRAY - 1);
    }

    // print results
    print_int_array(arr, LENGTH_ARRAY);
}

int main()
{
    // test openmp functions
    // #pragma omp parallel num_threads(1)
    // openmp_info();

    // test quicksort
    // #pragma omp parallel
    test_quicksort();

    return 0;
}
