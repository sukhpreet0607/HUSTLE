#include <stdio.h>
#include <stdlib.h>

struct ListNode {
     int val;
     struct ListNode *next;
}*head;
 
struct ListNode* deleteDuplicates(struct ListNode* node){
    int result[10],i,dup;
    struct ListNode *curr = node;
    struct ListNode *temp;
    dup = 0;
    i=0;

    while (curr!=NULL)
    {
        if (curr->val != curr->next->val && curr->val!=dup) {
            result[i] = curr->val;
            i++;
        }
        else {
            dup = curr->val;
        }
    }
    return result;
}

void main () {

    int *r = deleteDuplicates(head);
    for (int  i = 0; i < 10; i++)
    {
        printf("%d ",r[i]);
    }
    
}


void createList(int n)
{
    struct ListNode *newNode, *temp;
    int data, i;

    head = (struct ListNode *)malloc(sizeof(struct ListNode));

    // Terminate if memory not allocated
    if(head == NULL)
    {
        printf("Unable to allocate memory.");
        exit(0);
    }


    // Input data of node from the user
    printf("Enter the data of node 1: ");
    scanf("%d", &data);

    head->data = data; // Link data field with data
    head->next = NULL; // Link address field to NULL


    // Create n - 1 nodes and add to list
    temp = head;
    for(i=2; i<=n; i++)
    {
        newNode = (struct node *)malloc(sizeof(struct node));

        /* If memory is not allocated for newNode */
        if(newNode == NULL)
        {
            printf("Unable to allocate memory.");
            break;
        }

        printf("Enter the data of node %d: ", i);
        scanf("%d", &data);

        newNode->data = data; // Link data field of newNode
        newNode->next = NULL; // Make sure new node points to NULL 

        temp->next = newNode; // Link previous node with newNode
        temp = temp->next;    // Make current node as previous node
    }
}