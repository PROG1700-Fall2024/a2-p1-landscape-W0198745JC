#Program 1 – Landscape Calculator
#A landscaping company needs a program that computes the price of landscaping for a new housing development. 

#Student #: W0198745   
#Student Name:  Jenille Cheney

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
#base pay variable   / Tree cost  
    baseCharge= 1000
    treeCost= 100
#inputs for  Address, property Depth, Property Width, Type of Grass,number of trees
    Depth= int(input("Enter property depth (feet) :"))
    print("")
    Width= int(input("Enter property width (feet) :"))
    print("")
    grassType=input("Enter type of grass (fescue, bentgrass, campus) :").lower()
    print("")
    trees= int(input("Enter the number of trees :"))

# determine square footage
    totalSurface= Depth*Width
#if square footage above 5000 add $500 / # if elif grass types 
    if totalSurface >= 5000:
        extraCharge= baseCharge+totalSurface
        if grassType == "fescue":
            grassCharge= totalSurface*0.05
        elif grassType == "bentgrass":
            grassCharge= totalSurface*0.02
        else:
            grassCharge=totalSurface*0.01
    else:
        extraCharge= 0









    # YOUR CODE ENDS HERE

main()