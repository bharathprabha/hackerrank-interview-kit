/*
Detect a cycle in a linked list. Note that the head pointer may be 'NULL' if the list is empty.

A Node is defined as: 
    struct Node {
        int data;
        struct Node* next;
    }
*/

bool has_cycle(Node *head)
{
    if (head == nullptr)
        return 0;
    Node *second = head;
    Node *first= head ->next;
    while (first != second)
    {
        if (first == nullptr || first->next == nullptr)
            return 0;
        first=first->next->next;
        second =second->next;
    }
    return 1;
}


"""
#!/usr/bin/py
def flipBits(a):
   return a ^ 4294967295 
 
if __name__ == '__main__':
    n = int(raw_input())
    for i in range(0,n):
        a = int(raw_input())
        res = flipBits(a)
        print res
"""