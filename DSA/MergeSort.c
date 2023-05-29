#include<stdio.h>
#include<stdlib.h>

void mergeSort(int[],int,int); 
void merge(int[],int,int,int);

void display(int arr[], int size){
    int i;
    for(i = 0; i < size; i++){
        printf("%d ",arr[i]);
    }
    printf("\n");
}

void main() 
{
    int size;
    printf("Enter the size of array:");
    scanf("%d",&size);
    int *arr = (int *)malloc(size*sizeof(int));

    for(int i = 0; i < size; i++){
        scanf("%d ",&arr[i]);
    } 

	printf("Input: ");
    display(arr,size);

    mergeSort(arr, 0, size-1);
	printf("Output: ");
    display(arr, size);
}

void mergeSort(int a[], int left, int right)
{
    int mid;
    if(left < right)
    {
       
        mid = (left + right)/2;
        
        // recursive calls to sort first half and second half subarrays
        mergeSort(a, left, mid);
        mergeSort(a, mid + 1, right);
        merge(a, left, mid, right);
    }
}

void merge(int arr[], int left, int mid, int right)
{
    int i, j, k;
    int n1 = mid - left + 1;
    int n2 = right - mid;
    
    // create temp arrays to store left and right subarrays
    int L[n1], R[n2];
    
    // Copying data to temp arrays L[] and R[]
    for (i = 0; i < n1; i++)
        L[i] = arr[left + i];
    for (j = 0; j < n2; j++)
        R[j] = arr[mid + 1 + j];
        
    // here we merge the temp arrays back into arr[l..r]
    i = 0; // Starting index of L[i]
    j = 0; // Starting index of R[i]
    k = left; // Starting index of merged subarray
    
    while (i < n1 && j < n2) 
    {
        // place the smaller item at arr[k] pos
        if (L[i] <= R[j]) {
            arr[k] = L[i];
            i++;
        }
        else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }
    // Copy the remaining elements of L[], if any 
    while (i < n1) {
        arr[k] = L[i];
        i++;
        k++;
    }
    // Copy the remaining elements of R[], if any 
    while (j < n2) {
        arr[k] = R[j];
        j++;
        k++;
    }
}