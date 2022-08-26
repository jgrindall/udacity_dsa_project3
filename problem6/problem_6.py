class MinMax():
    @staticmethod
    def get_min_max(ints):

        """
        Return a tuple(min, max) out of list of unsorted integers.
        Args:
            ints(list): list of integers containing one or more integers
            """
            
        n = len(ints)
        
        if n == 0:
            raise ValueError("length cannot be 0")
            
        min = float('inf')
        max = -float('inf')
    
        for item in ints:
            if item < min:
                min = item
            if item > max:
                max = item
        
        return (min, max)


