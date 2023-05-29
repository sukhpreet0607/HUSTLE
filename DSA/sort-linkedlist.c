#include <stdio.h>
#include <stdlib.h>

struct Node
{
    int data;
    struct Node *next;
} *head;

void createList(int n);
void traverseList(struct Node *temp);

void main()
{

    int n;
    printf("Enter the number of Nodes: ");
    scanf("%d", &n);
    createList(n);
    printf("\n");
    traverseList(head);
    printf("\n");
    merge(head,0,n/2,n-1);


}

void createList(int n)
{
    struct Node *newNode, *temp;
    int data, i;

    head = (struct Node *)malloc(sizeof(struct Node));

    // Terminate if memory not allocated
    if (head == NULL)
    {
        printf("Unable to allocate memory.");
        exit(0);
    }

    // Input data of Node from the user
    printf("Enter the data of Node 1: ");
    scanf("%d", &data);

    head->data = data; // Link data field with data
    head->next = NULL; // Link address field to NULL

    // Create n - 1 Nodes and add to list
    temp = head;
    for (i = 2; i <= n; i++)
    {
        newNode = (struct Node *)malloc(sizeof(struct Node));

        /* If memory is not allocated for newNode */
        if (newNode == NULL)
        {
            printf("Unable to allocate memory.");
            break;
        }

        printf("Enter the data of Node %d: ", i);
        scanf("%d", &data);

        newNode->data = data; // Link data field of newNode
        newNode->next = NULL; // Make sure new Node points to NULL

        temp->next = newNode; // Link previous Node with newNode
        temp = temp->next;    // Make current Node as previous Node
    }
}

/*
 * Display entire list
 */
void traverseList(struct Node *temp)
{
    
    // Return if list is empty
    if (temp == NULL)
    {
        printf("List is empty.");
        return;
    }

    while (temp != NULL)
    {
        printf("Data = %d\n", temp->data); // Print data of current Node
        temp = temp->next;                 // Move to next Node
    }
}

void merge(struct Node *head, int left, int mid, int right)
{
 
    struct Node *temp = head;
    struct Node *temp1;
    struct Node *temp2;
    int n1 = mid - left + 1;
    int n2 = right - mid;
    prev = (struct Node *)malloc(sizeof(struct Node));

    for (int i = 0; i < n1; i++)
    {

        if (i == 0)
        {
            temp1 = (struct Node *)malloc(sizeof(struct Node));

            if (newNode == NULL)
            {
                printf("Unable to allocate memory.");
                break;
            }
            temp1->data = temp->data;
            temp1->next = NULL;
            prev = temp1
        }
        else
        {

            newNode = (struct Node *)malloc(sizeof(struct Node));

            if (newNode == NULL)
            {
                printf("Unable to allocate memory.");
                break;
            }

            newNode->data = temp->data;
            newNode->next = NULL;
            prev->next = newNode;
            prev = newNode
        }
        temp = temp->next; 
        
    }


    for (int i = 0; i < n2; i++)
    {

        if (i == 0)
        {
            temp2 = (struct Node *)malloc(sizeof(struct Node));

            if (newNode == NULL)
            {
                printf("Unable to allocate memory.");
                break;
            }
            temp2->data = temp->data;
            temp2->next = NULL;
            prev = temp2
        }
        else
        {

            newNode = (struct Node *)malloc(sizeof(struct Node));

            if (newNode == NULL)
            {
                printf("Unable to allocate memory.");
                break;
            }

            newNode->data = temp->data;
            newNode->next = NULL;
            prev->next = newNode;
            prev = newNode
        }
        temp = temp->next; 
        
    }

    traverseList(temp1);
    traverseList(temp2);


}