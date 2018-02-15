import csv

##read CSV
newFile = open("C:\Projects\python\doc.txt", 'r')
reader = csv.reader(newFile)
controlPoints = list(reader)

##User Input Section
print 'First, input your datum adjustment factor. Something like 1.00002'
print 'If no datum adjustment is needed, enter 1 below'
datumAdjustmentFactor = float(input('Enter Datum adjustment factor: '))
print ''
print 'Next, input your rod height. Something like 5.5'
print 'If no rod height is needed (unlikely), enter 0 below'
rodHeight = float(input('Enter Rod Height: '))

print ''
print 'User input:'
print 'DA Factor is: ' + str(datumAdjustmentFactor) + ' and Rod Height is: ' + str(rodHeight)
print ''

print "Original Data: "
print controlPoints

##Apply DA Factor | Rearrange Easting/Northing | Add Rod Height
temp1, temp2, temp3 = 0.0, 0.0, 0.0 ##Set temp variables to 0.0 for use in calculations
count = 0  #sets counter to 0

while count < len(controlPoints):  #cycles through all rows to make adjustments
    temp1 = str((float(controlPoints[count][1]) * datumAdjustmentFactor)) ##Get northing and apply DA factor
    temp2 = str((float(controlPoints[count][2]) * datumAdjustmentFactor))  ##Get easting and apply DA factor
    temp3 = str((float(controlPoints[count][3]) + rodHeight)) ##gets elevation and adds rod height
    del controlPoints[count][1:4]  ##deletes original northing, easting, elevation
    controlPoints[count].insert(1,temp2) ##reinsert easting first at index 1
    controlPoints[count].insert(2,temp1) ##reinsert northing second at index 2
    controlPoints[count].insert(3,temp3) ##reinsert new elevation at index 3
    count += 1

print ''
print "Updated Data: "
print controlPoints

## Writes newly formatted & calculated data to a CSV
with open('control-points-formatted.csv', 'wb') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_NONE, escapechar='', quotechar='')
    wr.writerows(controlPoints)
    myfile.close()

## Require enter to close out terminal window
print ''
raw_input('Script executed successfully, press ENTER to exit')
