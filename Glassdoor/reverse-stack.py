'''
Reverse a stack using recursion
'''


def insert_at_bottom(stack, item):
    if len(stack) == 0:
        stack.append(item)

    else:
        temp = stack.pop()
        insert_at_bottom(stack, item)
        stack.append(temp)

def reverse_stack(stack):

    if len(stack) > 0:
        temp = stack.pop()
        reverse_stack(stack)
        insert_at_bottom(stack, temp)






def print_stack(stack):
    print "start of stack"
    for num in stack:
        print num
    print "end of stack"



arr = [1,2,3,4,5]
print_stack(arr)
reverse_stack(arr)
print_stack(arr)