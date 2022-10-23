#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

#define MAX_N_Q 100000

#define MAX_X_Y 1000000000

typedef struct linklist {
    int data;
    struct linklist *next;
}linknode, *linklistp;

typedef struct {
    linklistp head;
    int size;
}SEQUENCE;

linklistp insert_tail(linklistp head,linklistp newnode)
{

    if (head == NULL) {
        head = newnode;
    } else {
        linklistp temp = head;
        while(temp->next != NULL)
            temp = temp->next;

        newnode->next = NULL;
        temp->next = newnode;
    }

    return head;
}

void outputlinklist(linklistp head) {
    linklistp temp = head;
    while(temp)    {
        printf("%d",temp->data);
        temp = temp->next;
        if (temp!=NULL)
            printf("\n");
    }
}

int main()
{
    int N, Q;
    int i = 0;
    int choice, x, y, index;
    int lastans = 0;
    SEQUENCE *s = NULL;
    linklistp node, temp, output = NULL, outnode;

    scanf("%d", &N);
    if (N < 1 || N > MAX_N_Q) {
        return 1;
    }
    scanf("%d", &Q);
    if (Q < 1 || Q > MAX_N_Q) {
        return 1;
    }

    s = malloc(sizeof(SEQUENCE)*N);
    if(s == NULL) {
        return 1;
    }

    memset(s, 0, sizeof(SEQUENCE)*N);

    do {
        scanf("%d", &choice);
        scanf("%d", &x);
        scanf("%d", &y);

        if (choice != 1 && choice != 2) {
            return 1;
        }

        if (x < 0 || x > MAX_X_Y) {
            return 1;
        }

        if (y < 0 || y > MAX_X_Y) {
            return 1;
        }

        switch(choice){
            case 1:
                index = (x^lastans)%N;
                node = malloc(sizeof(linknode));
                if (node == NULL)
                    return 1;
                node->data = y;
                node->next = NULL;

                s[index].size ++;
                s[index].head = insert_tail(s[index].head, node);
                break;

            case 2:
                index = (x^lastans)%N;
                y = y % (s[index].size);
                temp = s[index].head;

                while ( y > 0) {
                    temp = temp->next;
                    y--;
                }

                lastans = temp->data;
                outnode = malloc(sizeof(linknode));
                outnode ->data = temp->data;
                output = insert_tail(output, outnode);
                break;

        }

        i++;

    }while (i < Q);

    if (output != NULL)
        outputlinklist(output);

    return 0;
}

