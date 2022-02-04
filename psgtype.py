print("""
█▀█ █░█ █▀█ ▄▀█ █▀ █▀▀   █▀ ▀█▀ █▀█ █░█ █▀▀ ▀█▀ █░█ █▀█ █▀▀   █▀▀ █▀█ ▄▀█ █▀▄▀█ █▀▄▀█ ▄▀█ █▀█
█▀▀ █▀█ █▀▄ █▀█ ▄█ ██▄   ▄█ ░█░ █▀▄ █▄█ █▄▄ ░█░ █▄█ █▀▄ ██▄   █▄█ █▀▄ █▀█ █░▀░█ █░▀░█ █▀█ █▀▄ 
by yourld\n""")


# input data
num = int(input("Enter number of production: "))

# declaring list for Right Hand Side and Left Hand Side of production
RHS = []
LHS = []

# input production data and stored in list
for x in range(num):
    
    LHS.append(input("\nEnter the left hand side of the production: "))
    RHS.append(input("Enter the right hand side of the production: "))
  

# determine each production type
prodType = [] 

for x in range(num):

    if(len(LHS[x]) == 1 ):
        if((len(RHS[x]) == 1 and RHS[x].islower() == True) or (( RHS[x][0].islower() == True) and RHS[x][1].isupper() == True)): # single terminal or ( single terminal + single non terminal )                    
            prodType.append(3)          # type 3
        else :                      
            prodType.append(2)          # type 2
    elif (len(RHS[x]) > len(LHS[x])):   # comparing RHS and LHS length
                          
        prodType.append(1)              # type 1
    else :                          
        prodType.append(0)              # type 0

print("")

for x in range(num):

    print("Type for production", x + 1 , ":" , prodType[x])
