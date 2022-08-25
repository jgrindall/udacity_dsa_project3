class RotatedArray:

    @staticmethod
    def find_pivot(input_list):
        """
        n = len(input_list)
        
        p = index that the minimum element occupies after being rotated (0 <= p <= n-1)
        
        index:            0 1 2        (p-1)  p  (p+1)                   n-1
        input_list:      [.................] [.] [.........................]
        
        A := {0....p-1}
        B := {p}
        C := {p+1 ......... n-1}
        
        @return 'p'
    
        """
        
        # Maintain two pointers:
        # p0 in A union B
        # p1 in B union C
        
        n = len(input_list)
        
        if n == 0:
            raise ValueError("length cannot be 0")
    
        p0 = 0
        p1 = n - 1
        
        while p1 - p0 >= 3:
            
            pmid = int((p0 + p1) // 2)
        
            v0 = input_list[p0]
            v1 = input_list[p1]
            vmid = input_list[pmid]
            
            #These are the only possible cases:
            
            #case 1: p0 in A, p1 in B, pmid in A.  v1 < v0 < vmid
            #case 2: p0 in A, p1 in C, pmid in A.  v1 < v0 < vmid
            #case 3: p0 in A, p1 in C, pmid in B.  vmid < v1 < v0
            #case 4: p0 in A, p1 in C, pmid in C.  vmid < v1 < v0
            #case 5: p0 in B, p1 in C, pmid in C.  v0 < vmid < v1
            
            if v1 < v0 and v0 < vmid:
                # cases 1 and 2 can both be solved by narrowing our search to [pmid...p1]
                p0 = pmid
            
            elif vmid < v1 and v1 < v0:
                # cases 3 and 4 can both be solved by narrowing our search to [p0...pmid]
                p1 = pmid
            
            else:
                # case 5 can both be solved by narrowing our search to [p0...pmid]
                p1 = pmid
        
        
        # small lists are simple
        v0 = input_list[p0]
        v1 = input_list[p1]
            
        if p1 - p0 == 2:
            pmid = int((p0 + p1)/2)
            vmid = input_list[pmid]
            if v0 < vmid and vmid < v1:
                return p0
            elif vmid < v1 and v1 < v0:
                return pmid
            else:
                return p1
        else:
            #p1 - p0 == 1
            if v0 < v1: 
                return p0
            else:
                return p1
    
    
    
    @staticmethod
    def rotated_array_search(input_list, number):
        """
        Find the index by searching in a rotated sorted array
    
        Args:
           input_list(array), number(int): Input array to search and the target
        Returns:
           int: Index or -1
        """
        n = len(input_list)
        p = RotatedArray.find_pivot(input_list)
        
        # now do a binary search but instead of using eg. [4, 5, 6, 7, 0, 1, 2, 3] we do it on an augmented array [4, 5, 6, 7, 0, 1, 2, 3, 4, 5, 6, 7]
        # consider the augmented array, from index p to the end (index p + n - 1)
        p0 = p
        p1 = p + n - 1
        
        def get_value(i):
            return input_list[i % n]
        
        index = None
        
        while p1 - p0 >= 2:
        
            pmid = int((p0 + p1) // 2)
            
            v0 = get_value(p0)
            v1 = get_value(p1)
            vmid = get_value(pmid)
            
            if vmid == number:
                index = pmid
                break
            elif vmid > number:
                p1 = pmid
            else:
                p0 = pmid
        
        if index is not None:
            #found it
            return index % n
            
        else:
            #small arrays are simple
            v0 = get_value(p0)
            v1 = get_value(p1)
            vmid = get_value(pmid)
            if v0 == number:
                return p0 % n
            elif vmid == number:
                return pmid % n
            elif v1 == number:
                return p1 % n
        
        return -1
    
    @staticmethod
    def linear_search(input_list, number):
        for index, element in enumerate(input_list):
            if element == number:
                return index
        return -1
    

