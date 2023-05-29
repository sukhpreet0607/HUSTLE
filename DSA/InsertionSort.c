#include<stdio.h>
#include<stdlib.h>


int InsertionSort(int arr[], int size,int right);

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
        scanf("%d",&arr[i]);
    } 
    // int arr[] = {8, 6, 4, 20, 24, 2, 10, 12}; 
    // int size = sizeof(arr)/sizeof(arr[0]);

	printf("Input: ");
    display(arr,size);

    InsertionSort(arr,size,0);
	printf("Output: ");
    display(arr,size);
}

int InsertionSort(int a[], int size,int right)
{
    int end  = right;
    if (end==size-1){
        return 0;
    }
    else {
        for (int i = end+1; i >= 0 ; i--)
        {
            if (a[i]<=a[i-1]){
                int temp = a[i-1];
                a[i-1] = a[i];
                a[i] = temp;
            }

        }
        return InsertionSort(a,size,end+1);
    }
}
