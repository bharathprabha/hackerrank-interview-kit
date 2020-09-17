def findMergeNode(head1, head2):
    a = head1
    b = head2
    while(a.next != None):
        temp = a
        a = a.next
        temp.next = None
    while(b.next != None):
        b = b.next
    return b.data

#1 2 3 4 5
#9 8 7 3


