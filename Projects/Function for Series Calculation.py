class series_calc ():



    """
    This function can be used to calculate different aspects of various series.

    For arithmetic series use series_calc.arithmetic

    For geometric series use series_calc.geometric

     Functions:

        series_calc.arithmetic.nth (fitst_element, number_of_elements, difference_between_two_elements)

        returns the nth element of the arithmetic series

        series_calc.arithmetic.sum (fitst_element, number_of_elements, difference_between_two_elements)

        returns the sum of the arithmetic series


        series_calc.geometric.nth (fitst_element, number_of_elements, quotient_of_two_elements)

        returns the nth element of the geometric series

        series_calc.geometric.sum (fitst_element, number_of_elements, quotient_of_two_elements)

        returns the sum of the geometric series

    """



    class arithmetic ():


        def nth (a,n,d):
                return (a + ((n - 1) * d))

        def sum (a,n,d):
                return ((n / 2) * ((2 * a) + ((n - 1) * d)))


    class geometric ():


        def nth (a,n,r):
            return (a * ((r) ** (n-1)))
            
        def sum (a,n,r):
            if r < 1:
                return ((a * (1- (r ** n))) / (1-r))
            elif r > 1:
                return ((a * ((r ** n) - 1)) / (r-1))



#print (help(series_calc))

#fe = float (input("FE: "))
#le = float (input("N: "))
#dif = float (input("D/R: "))

#print (series_calc.arithmetic.nth(fe,le,dif))
#print (series_calc.arithmetic.sum(fe,le,dif))

#print (series_calc.geometric.nth(fe,le,dif))
#print (series_calc.geometric.sum(fe,le,dif))
