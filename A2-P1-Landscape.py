#Program 1 – Landscape Calculator
#A landscaping company needs a program that computes the price of landscaping for a new housing development. 

#Student #: W0198745   
#Student Name:  Jenille Cheney

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    print("Welcome to the Landscape Calculator")
#base pay variable   / Tree cost  
    baseCharge= 1000
    treeCost= 100
#inputs for  Address, property Depth, Property Width, Type of Grass,number of trees
    house=input("Enter house number: ")
    print("")
    Depth= int(input("Enter property depth (feet) :"))
    print("")
    Width= int(input("Enter property width (feet) :"))
    print("")
    grassType=input("Enter type of grass (fescue, bentgrass, campus) :").lower()
    print("")
    trees= int(input("Enter the number of trees :"))

# determine square footage
    totalSurface= Depth*Width
    treeCharge=treeCost*trees
#if square footage above 5000 add $500 / # if elif grass types 
    if totalSurface > 5000:                                      #orginally had >= but realized it only needed to be greater
        extraCharge= 500
    else:
        extraCharge= 0
    # no longer nested
    if grassType == "fescue":
            grassCharge= totalSurface*0.05
    elif grassType == "bentgrass":
            grassCharge= totalSurface*0.02
    else:
            grassCharge= totalSurface*0.01
        # realized that by originally nesting this if when the totalSurface was less than 5000 it didn't work so i Seperated the if statements found this out on my last set of testing numbers
# total cost equation
    totalCost=grassCharge+extraCharge+treeCharge+baseCharge
 #Final Print Statement
    print("Total cost for house {0} is: $ {1:.2f}".format(house,totalCost))









    # YOUR CODE ENDS HERE

main()