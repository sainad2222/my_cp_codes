# source: gfg
from math import ceil, log2

def getMid(s, e) :
    return s + (e - s) // 2

def getXorUtil(st, ss, se, qs, qe, si) :
    if (qs <= ss and qe >= se) :
        return st[si];
    if (se < qs or ss > qe) :
        return 0;
    mid = getMid(ss, se);
    return getXorUtil(st, ss, mid, qs, qe, 2 * si + 1) ^ \
        getXorUtil(st, mid + 1, se, qs, qe, 2 * si + 2);

""" A recursive function to update the nodes
which have the given index in their range.
The following are parameters
st, si, ss and se are same as getXorUtil()
i --> index of the element to be updated.
      This index is in input array."""
def updateValueUtil(st, ss, se, i,
                    prev_val, new_val, si) :

    # Base Case: If the input index lies
    # outside the range of this segment
    if (i < ss or i > se) :
        return;

    # If the input index is in range of this node,
    # then update the value of the node and its children
    st[si] = (st[si] ^ prev_val) ^ new_val;
    if (se != ss) :

        mid = getMid(ss, se);
        updateValueUtil(st, ss, mid, i, prev_val,
                        new_val, 2 * si + 1);
        updateValueUtil(st, mid + 1, se, i,
                        prev_val, new_val, 2 * si + 2);

# The function to update a value in input
# array and segment tree. It uses updateValueUtil()
# to update the value in segment tree
def updateValue(arr, st, n, i, new_val) :

    # Check for erroneous input index
    if (i < 0 or i > n - 1) :

        print("Invalid Input");
        return;

    temp = arr[i];

    # Update the value in array
    arr[i] = new_val;

    # Update the values of nodes in segment tree
    updateValueUtil(st, 0, n - 1, i, temp, new_val, 0);

# Return Xor of elements in range from
# index qs (quey start) to qe (query end).
# It mainly uses getXorUtil()
def getXor(st, n, qs, qe) :

    # Check for erroneous input values
    if (qs < 0 or qe > n - 1 or qs > qe) :
        print("Invalid Input");
        return 0;

    return getXorUtil(st, 0, n - 1, qs, qe, 0);

# A recursive function that constructs
# Segment Tree for array[ss..se]. si is
# index of current node in segment tree st
def constructSTUtil(arr, ss, se, st, si) :

    # If there is one element in array,
    # store it in current node of segment
    # tree and return
    if (ss == se) :

        st[si] = arr[ss];
        return arr[ss];

    # If there are more than one elements,
    # then recur for left and right subtrees
    # and store the Xor of values in this node
    mid = getMid(ss, se);
    st[si] = constructSTUtil(arr, ss, mid, st, si * 2 + 1) ^ \
        constructSTUtil(arr, mid + 1, se, st, si * 2 + 2);

    return st[si];

""" Function to construct segment tree from given array.
This function allocates memory for segment tree and
calls constructSTUtil() to fill the allocated memory """
def constructST(arr, n) :

    # Allocate memory for segment tree

    # Height of segment tree
    x = (int)(ceil(log2(n)));

    # Maximum size of segment tree
    max_size = 2 * (int)(2**x) - 1;

    # Allocate memory
    st = [0] * (max_size);

    # Fill the allocated memory st
    constructSTUtil(arr, 0, n - 1, st, 0);

    # Return the constructed segment tree
    return st;
n,q = map(int,input().split())
lis = list(map(int,input().split()))
st = constructST(lis,n)
for i in range(q):
    t,x,y = map(int,input().split())
    x -= 1
    y -= 1
    if t==2:
        print(getXor(st, n, x, y))
    else:
        updateValue(lis, st, n, x, lis[x] ^ (y+1))
