import sys
from tabulate import tabulate

ecu02 = ["A4SG900C", "A4SGA00C", "A4SGC00C", "A4SGD10C", "A4SGE00C", "A4SGE01C"]
ecu03 = ["A4TC300K","A4TC101L","A4TC300L","A4TC400L","A4TC401L"]
ecu0405 = ["A4TF300E","A4TF400E","A4TF510E","A4TF300F","A4TF500F","A4TF510F","A4TF520F","A4TF800E","A4TF800F","	A4TF810F"]

ecuflash = False
stock = False
ecuId = ""
fb = []

def getPrimOLFueling():
    if(ecuId in ecu02): 
        if (ecuflash): rpmStart = 136029
        elif (stock): rpmStart = 168797
        rpmNum = 18
        loadNum = 16
    elif(ecuId in ecu03):
        if (ecuflash): rpmStart = 134611
        elif (stock): rpmStart = 167379
        rpmNum = 16
        loadNum = 14
    elif(ecuId in ecu0405):
        if (ecuflash): rpmStart = 134606
        elif (stock): rpmStart = 167374
        rpmNum = 16
        loadNum = 14
    else: sys.exit('Error, this ECU is not compatible yet.')
    rpms = []
    loadStart = rpmStart + 1 + rpmNum * 2
    loads = []
    afrStart = rpmStart + 3 + rpmNum * 2 + loadNum * 2
    afrs = []

    def getRPMs():
        for i in range(0,rpmNum):
            rpms.append(((fb[rpmStart+(2*i)])+((fb[rpmStart+1+(2*i)])/255))*50)

    def getLoads():
        for i in range(0, loadNum):
            loads.append(round(((fb[loadStart+(2*i)])+((fb[loadStart+1+(2*i)])/255))/64, 2))

    def getAFRS():
        for i in range(0, rpmNum):
            row = []
            for j in range(0, loadNum):
                #14.7/(1+byte*0.0078125)
                row.append(round(14.7/((0.0078125*fb[afrStart+j+(loadNum*i)])+1), 2))
            afrs.append(row)
    
    def printPrimOLFueling():
        table = []
        row = ["RPM\LOADS"]
        for i in loads: row.append(i)
        table.append(row)
        for i in range(len(rpms)):
            row = [rpms[i]]
            for j in range(len(loads)):
                row.append(afrs[i][j])
            table.append(row)
        print(tabulate(table))

    getRPMs()
    getLoads()
    getAFRS()
    printPrimOLFueling()

def setup():
    global ecuId
    global ecuflash
    global stock
    global fb

    table = sys.argv[1]
    rom = sys.argv[2]

    #read ROM as an array of bytes
    with open(rom, "rb") as f:
        fb = f.read()

    #get ECU ID to determine ecu-specific settings
    ecuId = fb[512:520].decode("utf-8")
    print('ECU ID: ', ecuId)

    #determine if ecu is stock map or saved from EcuFlash
    if(len(fb) == 163840): ecuflash = True
    elif(len(fb) == 196608): stock = True
    else: sys.exit("The ROM provided cannot be interpreted properly. This is likely an issue on our side. Please create an issue with your specific ECU ID and we'll hopefully have it working soon.")


if (len(sys.argv) < 2): 
    sys.exit("No arguments specified. Please run with --help for available arguments.")
elif(len(sys.argv) >= 3 and sys.argv[1] == "--primary-ol-fueling"):
    setup()
    getPrimOLFueling()
elif(sys.argv[1] == "--help"):
    sys.exit("Commands:\n--help: Print this help menu\n--primary-ol-fueling {file}: Print the Primary OL Fueling table encoded in the specified rom file")
else:
    sys.exit("The argument provided is not recognized")


