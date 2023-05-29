#include <stdio.h>
#include<stdlib.h>

struct Node
{
    int data;
    struct Node *next;
    struct Node *prev;
}*top;


void push(){

    struct Node *node = (struct Node *)malloc(sizeof(struct Node));
    int value;
    printf("Enter the value: ");
    scanf("%d",&value);
    node->data = value;
    node->prev = top;
    node->next = NULL;
    top = node;


}

void pop(){
    
    if (top==NULL) {
        printf("Stack is empty");
    }
    printf("The value at top of the stack is : %d",top->data);
    struct Node *temp = top;
    top = top->prev;
    free(temp);

}


void main(){

    top = NULL;
    push();
    push();
    push();
    push();
    pop();
    pop();

}

