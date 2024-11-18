#include<stdio.h>
#include<stdlib.h>
struct node{
    int data;
    struct node *next;
};

int main()
{
    struct node *head=NULL,*newnode,*current;
    int max,i;
    printf("enter the number of nodes : ");
    scanf("%d",&max);
    printf("enter the data : ");
    for ( i = 0; i < max; i++)
    {
        newnode=(struct node*)malloc(sizeof(struct node));
        scanf("%d",&newnode->data);
        if(head==NULL)
        {
            head=newnode;
            current=newnode;
        }
        else
        {
            current->next=newnode;
            current=newnode;
        }
    }
    struct node *temp=head;
    // display
    for ( i = 0; i < max; i++)
    {
        printf("%d",temp->data);
        printf("->");
        temp=temp->next;
    }
        // insert in middle
    temp=head;
    int count;
    printf("enter the position to insert : ");
    scanf("%d",&count);
    for (int i = 0; i < count; temp=temp->next)
    {
        
    }
    
}