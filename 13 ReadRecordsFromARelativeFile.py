def ReadRecordsFromARelativeFile():
    with open("ProductData", "r") as fd:
        ProductData = fd.readlines()

    for i in ProductData:



ReadRecordsFromARelativeFile()
