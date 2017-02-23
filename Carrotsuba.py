""" Carrotsuba.py: a negative handling, pretty, educational version of the Karatsuba method """
""" by jaystings.com """

""" carrot ascii image credit goes to ascii.co.uk/art/carrot """
""" algorithm credit to https://pythonandr.com/2015/10/13/karatsuba-multiplication-algorithm-python-code/ """


import sys

def negKaratsuba(x,y):
	"""Function to multiply 2 numbers in a more efficient manner than the grade school algorithm"""
        
        print("               ___")
        print("      `-.   |     `~~-----,_")
        print("      -------|              `~~--.,_")
        print(" jgs  _.    |.____,,,,-------~~```'")

        """ Hack to deal with negative numbers """
        neg = False
        if(x<0 or y<0):
            neg = True
            x = abs(x)
            y = abs(y)

	bsx = len(str(x))
        bsy = len(str(y))

        print("bsx = {0}".format(bsx))

        print("bsy = {0}".format(bsy))
        

        if bsx == 1 or bsy == 1:
                print("they're both 1, dummy!")
		return x*y
	else:
                n = max(bsx,bsy)

		nby2 = n / 2
		
                print("n=max(lsx, lsy) = n (={0}) / 2 = nby2 (={1})".format(n, nby2))        
        
		a = x / 10**(nby2)
		b = x % 10**(nby2)
		c = y / 10**(nby2)
		d = y % 10**(nby2)
		
		print("a = x / 10**(nby2)={0}".format(a))

		print("b = x % 10**(nby2)={0}".format(b))

		print("c = y / 10**(nby2)={0}".format(c))

		print("d = y % 10**(nby2)={0}".format(d))
                
                print("now, let's use the same method to find a*c and b*d recursively:")

		ac = negKaratsuba(a,c)
		bd = negKaratsuba(b,d)
                ad_plus_bc = negKaratsuba(a+b,c+d) - ac - bd

                print("carrot(ac) = {0}, carrot(bd) = {1}, carrot(a+b,c+d) - ac - bd = {2}".format(ac, bd, ad_plus_bc))
        
        	# this little trick, writing n as 2*nby2 takes care of both even and odd n
		prod = ac * 10**(2*nby2) + (ad_plus_bc * 10**nby2) + bd
        
        if(neg == True):
            prod = prod * -1
	return prod

if(len(sys.argv) != 3 or sys.argv[0] == "-h"):
    print("carrotsuba takes 2 arguments: f(actor)1 and f(actor)2")
    sys.exit()

f1 = int(sys.argv[1])
f2 = int(sys.argv[2])

print("\n\n\nTHE PRODUCT OF {0} AND {1} IS\n\n\n {2}\n\n\n".format(f1, f2, negKaratsuba(f1,f2)))

enter = raw_input("\n\nPress enter or ^[[A^[[A or whatever to continue . . . \n\n")

print("\n\n\nnumber of carrots = number of recursions\n\n\n")
