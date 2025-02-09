#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void merge(int arr[], int l, int m, int r) {
    int n1 = m - l + 1;
    int n2 = r - m;
    int L[n1], R[n2];

    for (int i = 0; i < n1; i++)
        L[i] = arr[l + i];
    for (int j = 0; j < n2; j++)
        R[j] = arr[m + 1 + j];

    int i = 0, j = 0, k = l;
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            arr[k] = L[i];
            i++;
        } else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }

    while (i < n1) {
        arr[k] = L[i];
        i++;
        k++;
    }

    while (j < n2) {
        arr[k] = R[j];
        j++;
        k++;
    }
}

void mergeSort(int arr[], int l, int r) {
    if (l < r) {
        int m = l + (r - l) / 2;
        mergeSort(arr, l, m);
        mergeSort(arr, m + 1, r);
        merge(arr, l, m, r);
    }
}

int main() {
    int input_sizes[] = {1000, 5000, 10000, 50000, 100000};
    int num_sizes = sizeof(input_sizes) / sizeof(input_sizes[0]);

    for (int i = 0; i < num_sizes; i++) {
        int n = input_sizes[i];
        int *arr = (int *)malloc(n * sizeof(int));

        srand(time(NULL));
        for (int j = 0; j < n; j++) {
            arr[j] = rand() % 100000;
        }

        // Measure execution time
        clock_t start_time = clock();
        mergeSort(arr, 0, n - 1);
        clock_t end_time = clock();
        double time_taken = (double)(end_time - start_time) / CLOCKS_PER_SEC;

        printf("Input size: %d, Time taken: %f seconds\n", n, time_taken);
        free(arr);
    }

    return 0;
}