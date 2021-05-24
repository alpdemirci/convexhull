import os
import math
import operator

# Checking the existence of file using os.path.isfile()
# -----------------------------------------------------
f_name = input("Enter the name of the dataset file:")
ff = os.path.isfile(f_name)
while ff is False:
    f_name = input("File could not exist, enter again:")
    ff = os.path.isfile(f_name)
h = open(f_name, "r")
line = h.readlines()
h.close()
# -----------------------------------------------------
coor = {}
for i in line:
    i = i.split()
    try:
        coor[i[0]] = [float(i[2]), float(i[1])]
    except IndexError:
        pass
sort = sorted(coor.items(), key=operator.itemgetter(1))
add = sort[0]
minx = sort[0][1][1]
miny = sort[0][1][0]
id1 = sort[0][0]
checkx = sort[-1][1][1]
checky = sort[-1][1][0]
idlist = []
del sort[0]  # It deletes when point was determined
# Calculation part
# From left to right it sorts y axis from minimum to maximum...
# -------------------------------------------------------------
while checkx != minx and checky != miny:
    radlist = []
    for i in range(len(sort)):
        # Azimuth Calculations...
        nextx = sort[i][1][1]
        nexty = sort[i][1][0]
        if nextx - minx >= 0 and nexty - miny < 0:  # 4. region
            rad = 2 * math.pi - math.atan2(abs(miny - nexty),
                                           abs(minx - nextx))
        elif nextx - minx <= 0 and nexty - miny < 0:  # 3. region
            rad = math.pi + math.atan2(abs(miny - nexty), abs(minx - nextx))
        elif nextx - minx <= 0 and nexty - miny > 0:  # 2. region
            rad = math.pi - math.atan2(abs(miny - nexty), abs(minx - nextx))
        elif nextx - minx >= 0 and nexty - miny > 0:  # 1. region
            rad = math.atan2(abs(miny - nexty), abs(minx - nextx))
        else:
            if nextx - minx > 0 and nexty - miny == 0:
                rad = math.pi
            elif nextx - minx < 0 and nexty - miny == 0:
                rad = 0

        rad = rad % (2 * math.pi)
        radlist.append(rad)
    minrad = min(radlist)

    s = radlist.index(minrad)
    minx = sort[s][1][1]
    miny = sort[s][1][0]
    id2 = sort[s][0]
    idlist.append([id1, id2])  # For backward calculation it keeps y coordinate
    id1 = sort[s][0]
    del sort[s]
# -------------------------------------------------------------
sort.append(add)
checkx = sort[-1][1][1]
checky = sort[-1][1][0]
# From right to left it sorts y axis from minimum to maximum...
# -------------------------------------------------------------
while checkx != minx and checky != miny:
    radlist = []
    for i in range(len(sort)):
        # Opposite direction of azimuth Calculation...
        nextx = sort[i][1][1]
        nexty = sort[i][1][0]
        if nextx - minx >= 0 and nexty - miny < 0:  # 4. region
            rad = 2 * math.pi - math.atan2(abs(miny - nexty),
                                           abs(minx - nextx))
        elif nextx - minx <= 0 and nexty - miny < 0:  # 3. region
            rad = math.pi + math.atan2(abs(miny - nexty), abs(minx - nextx))
        elif nextx - minx <= 0 and nexty - miny > 0:  # 2. region
            rad = math.pi - math.atan2(abs(miny - nexty), abs(minx - nextx))
        elif nextx - minx >= 0 and nexty - miny > 0:  # 1. region
            rad = math.atan2(abs(miny - nexty), abs(minx - nextx))
        else:
            if nextx - minx > 0 and nexty - miny == 0:
                rad = math.pi
            elif nextx - minx < 0 and nexty - miny == 0:
                rad = 0
        rad += math.pi  # Changing the direction oppositely
        rad = rad % (2 * math.pi)  # Angle Conversion
        radlist.append(rad)
    minrad = min(radlist)
    s = radlist.index(minrad)
    minx = sort[s][1][1]
    miny = sort[s][1][0]
    id2 = sort[s][0]
    idlist.append([id1, id2])
    id1 = sort[s][0]
    del sort[s]
# -------------------------------------------------------------
# Writing to the file and checking the existence...
# It writes the output .txt extension file on the same directory...
# -------------------------------------------------
print(idlist)
prnt = ""
for i in idlist:
    prnt += i[0]+"\t"+i[1]+"\n"
path = input("Enter output file name:")
t = os.path.isfile(path)
while t:
    path = input("""This Name Used Before
Enter file name again: """)
    t = os.path.isfile(path)
f = open(path+".txt", "w")
f.write(prnt)
f.close()
# -------------------------------------------------
