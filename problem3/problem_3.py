
"""Rearrange Array Elements so as to form two number such that their sum is maximum. Return these two numbers.

You can assume that all array elements are in the range [0, 9]. 

The number of digits in both the numbers cannot differ by more than 1. You're not allowed to use any sorting function that Python provides and the expected time complexity is O(nlog(n)).

for e.g. [1, 2, 3, 4, 5]

The expected answer would be [531, 42]. Another expected answer can be [542, 31]. In scenarios such as these when there are more than one possible answers, return any one.
"""


class Node:
    def __init__(self, value, data = None):
        self.value = value
        self.left = None
        self.right = None
        self.data = data
        

    def __gt__(self, other):
        return self.value > other.value

    def __repr__(self):
        s = "Node:" + str(self.value)
        if self.data is not None:
            s += " data " + str(self.data)
        if self.left:
            s += " left " + str(self.left)
        if self.right:
            s += " right " + str(self.right)
        return s
     
    def __str__(self):
         return self.__repr__()


class MinHeap:
    def __init__(self, elements = []):
        self.elements = []
        if len(elements) >= 1:
            self.elements.append(elements[0])
        for element in elements[1:]:
            self.insert(element)
        
    def __swap(self, i, j):
        t = self.elements[i]
        self.elements[i] = self.elements[j]
        self.elements[j] = t

    def __get_child_indices(self, i):
        """ Parent at index 'i' has two children at these indices """
        return [
            2*i + 1,
            2*i + 2
        ]

    def get_size(self):
        """total size"""
        return len(self.elements)

    def __get_parent_index(self, i):
        """Find the index in the array of the element which is the parent of element[i] """
        return (i - 1)//2
    
    def __get_children(self, i):
        """ get the nodes at the child indices (if they exist) """
        children = []
        num_elements = self.get_size()
        for index in self.__get_child_indices(i):
            if index <= num_elements - 1:
                children.append(self.elements[index]);
        return children
    
    def is_valid(self):
        """ helper function for tests - check that the heap property is satisfied"""
        for i in range(self.get_size()):
            if not self.__check_heap_property(i):
                return False
        return True
    
    def __check_heap_property(self, index):
        """check heap propert is ok at index 'index' """
        elt = self.elements[index]
        children = self.__get_children(index)
        #get the children and find ones that are wrong
        incorrect_children = list(filter(lambda child: elt > child, children))
        return len(incorrect_children) == 0;
    
    def insert(self, node):
        """ insert new node """
        current_len = len(self.elements)
        # add it
        self.elements.append(node)
        index = current_len
        parent_index = self.__get_parent_index(index)
        # cheeck heap property is ok
        while parent_index >= 0 and not self.__check_heap_property(parent_index):
            # if not, bubble up
            self.__swap(index, parent_index)
            index = parent_index
            if parent_index == 0:
                # we have set the root
                parent_index = -1
            else:
                # keep going
                parent_index = self.__get_parent_index(parent_index)
        
    def get(self):
        """ get the top (min) element """
        num_elements = self.get_size()
        if num_elements == 0:
            return None
        return self.elements[0]
    
    def remove(self):
        """ remove the top (min) element """
        num_elements = self.get_size()
        if num_elements == 0:
            return None
        else:
            root = self.elements[0]
            last = self.elements[-1]
            self.elements[0] = last
            self.elements.pop()
            if len(self.elements) == 0:
                return root
            else:
                # bubble down
                index = 0;
                while not self.__check_heap_property(index):
                    children = self.__get_children(index);
                    if len(children) == 0:
                        raise ValueError("heap property failed");
                    else:
                        #decide which to use
                        child_index = None
                        num_children = len(children)
                        child_indices = self.__get_child_indices(index)
                        if num_children == 1 or (num_children == 2 and children[0] < children[1]):
                            # left child
                            child_index = child_indices[0]
                        else:
                            # right child
                            child_index = child_indices[1]
                        self.__swap(index, child_index)
                        index = child_index
                return root
        
    def __repr__(self):
        return "MinHeap:" + str(self.elements)
     
    def __str__(self):
         return self.__repr__()



class Rearrange:
    
    @staticmethod
    
    def bruteforce(input_list):
        
        n = len(input_list)
        
        sorted_list = sorted(input_list)
        
        #check all possibilities
        subsets = [[]]
        
        def append_using(item):
            new_subsets = []
            for s in subsets:
                clone = s.copy()
                clone.append(item)
                new_subsets.append(clone)
            return new_subsets
        
        for item in input_list:
            subsets = subsets + append_using(item)
        
        subsets = list(filter(lambda s: len(s) <= int((n + 1)//2) and len(s) >= int(n//2), subsets))
            
        max_sum = -float('inf')
        best_pair = None
        
        for s1 in subsets:
            for s2 in subsets:
                if abs(len(s1) - len(s2)) <= 1 and sorted(s1 + s2) == sorted_list:
                    #candidate
                    s1 = sorted(s1, reverse=True)
                    s2 = sorted(s2, reverse=True)
                    n1 = Rearrange.to_num(s1)
                    n2 = Rearrange.to_num(s2)
                    sum = n1 + n2
                    if sum > max_sum:
                        max_sum = sum
                        best_pair = [n1, n2]
        
        return best_pair
    
    
    @staticmethod
    def to_num(arr):
        """ [5, 4, 1] -> 541"""
        arr = arr.copy()
        n = 0
        place_val = 1
        while len(arr) >= 1:
            val = arr.pop()
            n += place_val * val
            place_val *= 10
        return n
    
    @staticmethod
    def rearrange_digits(input_list):
        
        """
        Rearrange Array Elements so as to form two number such that their sum is maximum.
    
        Args:
           input_list(list): Input List
        Returns:
           (int),(int): Two maximum sums
        """
        
        n = len(input_list)
        
        if n <= 1:
            raise ValueError("at least two numbers are required")
        
        heap = MinHeap()
        for item in input_list:
            heap.insert(Node(item))
        sorted_list = []
        while heap.get_size() >= 1:
            node = heap.remove()
            sorted_list.append(node.value)

        a = []
        b = []
        
        list_to_use = a
        while len(sorted_list) >= 1:
            val = sorted_list.pop()
            list_to_use.append(val)
            if list_to_use is a:
                list_to_use = b
            else:
                list_to_use = a

        return [Rearrange.to_num(a), Rearrange.to_num(b)]
