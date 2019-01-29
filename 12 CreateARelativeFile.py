def CreateARelativeFile():
    with open("ProductData", "w") as fp:
        for i in range(10):
            print("Please enter the details for the next product...")
            ProdNumber = input("Product Number: ")
            Description = input("Description: ")
            Quantity = input("Quantity: ")

            outstr = ProdNumber + "\t" + Description + ", " + Quantity + "\n"
            fp.write(outstr)

CreateARelativeFile()
