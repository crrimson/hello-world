#
# implement a stack in python


class StackNode():
    """ a node in a stack """
    
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node
        
    def get_next_node(self):
        return self.next_node
        
    def get_value(self):
        return self.value
        
    def set_next_node(self, node):
        self.next_node = node

class Stack():
    """ 
    define a stack object, that supports
    push/pop
    """

    def __init__(self):
        self.top_node = None
        self.length = 0
    
    def push(self, value):
        """ add a new node to the top of the stack """
        # add the new item to the stack.
        self.current_top_node = self.top_node
        self.top_node = StackNode(value, next_node=self.current_top_node)
        self.length += 1

    def pop(self):
        """ remove the node from the top, return it's value """
        if self.top_node == None:
            return None
        else:
            # get the value, and then set the new top node, to the one below
            self.value = self.top_node.get_value()
            self.top_node = self.top_node.get_next_node()
            self.length -= 1
            return self.value
    
    def get_length(self):
        return self.length
            

            
class SetOfStacks():
    """ Create a set of stacks, with each being x height """
    
    def __init__(self, stack_height=10):
        
        self.stack_height = stack_height
        self.array_of_stacks = []
        
        # Add the first stack to the array
        self.active_stack = Stack() 
        self.array_of_stacks.append(self.active_stack)
        self.num_stacks = 1
        
        self.active_stack
        
        
    def push(self, value):
        # Add a new item to the active stack, if we aren't too high
        if self.active_stack.get_length() < self.stack_height:
            self.active_stack.push(value)
        else:
            #too high, create a new Stack and add it to the array
            self.active_stack = Stack()
            self.active_stack.push(value)
            self.array_of_stacks.append(self.active_stack)
            self.num_stacks += 1
            
    def pop(self):
        # take the top item off the active stack
        
        # if the stack is not empty, pop.  If it is, we need to look for the previous stack.
        if self.active_stack.get_length() > 0:
            return self.active_stack.pop()
        elif self.num_stacks > 1:
            del self.array_of_stacks[self.num_stacks - 1]
            self.num_stacks -= 1
            self.active_stack = self.array_of_stacks[self.num_stacks - 1]
            return self.active_stack.pop()
        else:
            return None
            
            
    def pop_at(self, index):
        # pop item off stack at a given index
        if index < self.num_stacks and index >= 0:
            return self.array_of_stacks[index].pop()
        else:
            return None
    def get_length(self):
        return self.num_stacks
        
        
    
    