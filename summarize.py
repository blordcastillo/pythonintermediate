import arcpy
shp = u'C:\\Assignment3\\PublicSchools.shp'
d = arcpy.da.FeatureClassToNumPyArray(shp,['txt_Respon'])
districts = {x[0] for x in d}
centers = []
for district in districts:
    schools = arcpy.da.FeatureClassToNumPyArray(shp,["SHAPE@X","SHAPE@Y"],"\"txt_Respon\" = '{}'".format(district))
    print "{} schools have a mean location of {},{}".format(district,schools['SHAPE@X'].mean(),schools['SHAPE@Y'].mean())
    centers.append((district,schools['SHAPE@X'].mean(),schools['SHAPE@Y'].mean()))

