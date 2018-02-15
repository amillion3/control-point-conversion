# Survey Control Point Conversion

This python script will convert and format control points from the data collector to FARO Scene format.

This script will also allow for a datum adjustment to be made and for a rod height to be added to the elevation.


##Input file format required:
Unique Number, Northing, Easting, Elevation, Type of Point
134,247808.131,2211159.261,692.901,XCP/SNG


##How to use this glorious script:

1. Create a folder at this specific location:
    C:\Projects\python

2. Copy the 'control-point-converter.py'.

3. Make a copy of the original control points text file. Name the new file exactly as 'doc.txt'.

4. Right click on the 'control-point-converter.py' and select 'Open'.

5. Enter datum adjustment (as needed).

6. Enter rod height (in feet).

7. A new file named 'control-points-formatted.csv' should have been created. This will contain the calculated and formatted control points.

8. Double check with the original control points file that changes have been made.
