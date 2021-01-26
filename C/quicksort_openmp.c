// template Program in C using OpenMP
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
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

int HIST_INPUT_LEN = 999999;
int HIST_NUM_BUCKETS = 20;
// histogram counts the number of elements in each bucket
void histogram(int *a, int *h) {
    int N = HIST_INPUT_LEN;
    int m = HIST_NUM_BUCKETS;
    // initialize histogram by setting buckets to zero
    #pragma omp parallel for
    for (int i = 0; i < m; i++) {
        h[i] = 0;
    }
    // populate histogram by number of appearences
    #pragma omp parallel for
    for (int i = 0; i < N; i++) {
        int index = a[i] - 1;
        if (index >= 0 && index < N) {
            #pragma omp atomic
            h[index]++;
        }
    }
}

// test the histogram algorithm
void test_histogram() {
    int arr[HIST_INPUT_LEN];
    int hist[HIST_NUM_BUCKETS];

    // setup testing
    initialize_random();
    for (int i = 0; i < HIST_INPUT_LEN; i++) {
        arr[i] = rand() % HIST_NUM_BUCKETS + 1;
    }
    print_int_array(arr, HIST_INPUT_LEN);

    // create histgram
    histogram(arr, hist);

    // print results
    print_int_array(hist, HIST_NUM_BUCKETS);
}

// integrate root(x) / (1 + x^3) between 0 and 1 using 16 threads NUMBER_1
double integration_1() {
    int accuracy = 100;
    double width = 1.0/(double) accuracy;
    double answer = 0.0;
    double x = 0.0;
    double step = 0.0;

    #pragma omp parallel for num_threads(8) private(x, step)
    for (int i = 0; i < accuracy; i++) {
        x = width * (i + 0.5);
        step = width * sqrt(x) / (1 + x * x * x);
        #pragma omp atomic
        answer += step;
    }
    
    return answer;
}

// integrate root(x) / (1 + x^3) between 0 and 1 using 16 threads NUMBER_2
double integration_2() {
    int accuracy = 100;
    double width = 1.0/(double) accuracy;
    double answer = 0.0;
    double x = 0.0;
    double step = 0.0;

    #pragma omp parallel for num_threads(8) reduction(+:answer) private(x, step)
    for (int i = 0; i < accuracy; i++) {
        x = width * (i + 0.5);
        step = width * sqrt(x) / (1 + x * x * x);
        answer += step;
    }
    
    return answer;
}

int main()
{
    // test_quicksort();
    // test_histogram();
    printf("Integration 1 Result: %lf\n", integration_1());
    printf("Integration 2 Result: %lf\n", integration_2());
    return 0;
}
