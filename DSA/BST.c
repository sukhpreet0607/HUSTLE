#include <stdio.h>
#include <stdlib.h>

struct Node
{
    int data;
    struct Node *left;
    struct Node *right;
} *root;

struct Node *insert(struct Node *root, int data);
void Inorder(struct Node *root);
void Preorder(struct Node *root);
void Postorder(struct Node *root);
int search(struct Node *node, int value);


void main()
{
    // int n;
    // printf("Enter number of nodes :");
    // scanf("%d", &n);
    // root = NULL;
    // for (int i = 0; i < n; i++)
    // {
    //     int data;
    //     printf("Enter data for node :");
    //     scanf("%d", data);
    //     if (i == 0)
    //     {
    //         root = insert(root, data);
    //     }
    //     else
    //     {
    //         insert(root, data);
    //     }
    // }
    root = insert(root, 12);
    insert(root, 10);
    insert(root, 15);
    insert(root, 9);

    Inorder(root);
    printf("\n");
    Preorder(root);
    printf("\n");
    Postorder(root);
    printf("The value is : %d",search(root,9));
}

struct Node *insert(struct Node *node, int data)
{

    if (node == NULL)
    {
        struct Node *node = (struct Node *)malloc(sizeof(struct Node));
        node->data = data;
        node->left = NULL;
        node->right = NULL;

        return node;
    }

    else
    {

        if (data <= node->data)
        {
            // struct Node *node = (struct Node *)malloc(sizeof(struct Node));
            // node->data = data;
            node->left = insert(node->left, data);
        }
        else
        {
            // struct Node *node = (struct Node *)malloc(sizeof(struct Node));
            // node->data = data;
            node->right = insert(node->right, data);
        }
    }
    return node;
}

void Inorder(struct Node *root)
{
    // base condition for recursion
    // if tree/sub-tree is empty, return and exit
    if (root == NULL)
        return;

    Inorder(root->left);       // Visit left subtree
    printf("%d ", root->data); // Print data
    Inorder(root->right);      // Visit right subtree
}

void Preorder(struct Node *root)
{
    // base condition for recursion
    // if tree/sub-tree is empty, return and exit
    if (root == NULL)
        return;

    printf("%d ", root->data); // Print data
    Preorder(root->left);      // Visit left subtree
    Preorder(root->right);     // Visit right subtree
}

void Postorder(struct Node *root)
{
    if (root == NULL)
        return;

    Postorder(root->left);     // Visit left subtree
    Postorder(root->right);    // Visit right subtree
    printf("%d ", root->data); // Print data
}



int search(struct Node *node, int value)
{

    if (node->data == value)
    {       
        return node->data;
    }

    else
    {

        if (value <= node->data)
        {
            return search(node->left, value);
        }
        else
        {
            return search(node->right, value);
        }
    }
   
}