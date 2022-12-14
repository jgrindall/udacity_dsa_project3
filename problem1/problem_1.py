class Sqrt:
    @staticmethod
    def sqrt(number):
        """
        Calculate the floored square root of a number
    
        Args:
           number(int): Number to find the floored squared root
        Returns:
           int: Floored Square Root
        """
        if number < 1:
            return 0
    
        elif number < 4:
            return 1
        
        elif number == 4:
            return 2
        
        estimate0 = 1
        
        # this is an upper bound if number>= 5
        estimate1 = number/2
        
        while estimate1 - estimate0 >= 0.5:
            midpoint = (estimate0 + estimate1)/2
            if midpoint*midpoint == number:
                return midpoint
            elif midpoint*midpoint > number:
                estimate1 = midpoint
            else:
                estimate0 = midpoint
        
        floor0 = int(estimate0 - estimate0 % 1)
        floor1 = int(estimate1 - estimate1 % 1)

        if floor1*floor1 <= number:
            return floor1
        return floor0
        

