#include<stdio.h>
#include<math.h>
#include<stdlib.h>
#include<limits.h>

int dp[100000];
// following is the greedy approach 

int MinCost(int n,int arr[]){

    int i=0;
    int cost = 0;
    while (i<n)
    {
        if (i==n-2){
            cost+=abs((arr[i+1]-arr[i]));
            return cost;
        }
        else if ( abs((arr[i+1]-arr[i])) >= abs((arr[i+2]-arr[i])) ){
            cost+=abs((arr[i+1]-arr[i]));
            i+=1;
        }
        else {
            cost+=abs((arr[i+2]-arr[i]));
            i+=2;
        }
    }
    printf("%d",i);
    return cost;

}

// This is brute force recursion
int MinCost1(int i,int arr[]){
    int cost=INT_MAX;
    if (i==0){
        return 0;
    }

    cost=fmin(cost,abs(arr[i]-arr[i-1]) + MinCost1(i-1,arr));

    if (i>1){
    cost=fmin(cost,abs(arr[i]-arr[i-2]) + MinCost1(i-2,arr));
    }
    return cost;
}


int MinCost2(int i,int arr[]){
    int cost=INT_MAX;
    if (i==0){
        return 0;
    }
    if (dp[i]!=-1){
        return dp[i];
    }

    cost=fmin(cost,abs(arr[i]-arr[i-1]) + MinCost1(i-1,arr));

    if (i>1){
    cost=fmin(cost,abs(arr[i]-arr[i-2]) + MinCost1(i-2,arr));
    }
    dp[i] = cost;
    return dp[i];
}


 
void main() {
    int a[] = {30 ,10, 60, 10, 60, 50};
    // int ans  = MinCost(4,a);
    // int ans  = MinCost1(1,a);
    for (int i=0;i<100000;i++){
        dp[i]=-1;
    }
    int ans  = MinCost2(5,a);

    printf("%d",ans);
}