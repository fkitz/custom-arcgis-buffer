import arcpy
def ScriptTool(param0, param1, param2, param3):
    arcpy.AddMessage('Complete') # final completion message
    return

if __name__ == "__main__":
    
    # defines inputs as text strings
    param0 = arcpy.GetParameterAsText(0)
    param1 = arcpy.GetParameterAsText(1)
    param2 = arcpy.GetParameterAsText(2)
    param3 = arcpy.GetParameterAsText(3)

    # get the input field count to ensure an input was made
    pm1 = (arcpy.management.GetCount(param1).getOutput(1))
    pm2 = (arcpy.management.GetCount(param2).getOutput(2))
    pm3 = (arcpy.management.GetCount(param3).getOutput(3))

    if param1!= '':
        arcpy.Buffer_analysis(param0,param0[:-4] + str(param1) + '.shp',param1)
        # renames new buffer layer to the input file ('param0') plus the buffer radius ('param1')
        if pm1 == 0:
            arcpy.AddError("{1} has no features!".format(param1))
            # if field count is zero, the script runs an error message
        else:
            arcpy.AddMessage('Buffering Input and creating BuffDist1') 
            # if the field count is non-zero, the script returns a positive message

    if param2!= '':
        arcpy.Buffer_analysis(param1,param1[:-4] + str(param2) + '.shp',param2)
        if pm2 == 0:
            arcpy.AddError("{2} has no features!".format(param2))
        else:
            arcpy.AddMessage('Buffering BuffDist1 and creating BuffDist2')

    if param3!= '':
        arcpy.Buffer_analysis(param2,param2[:-4] + str(param3) + '.shp',param3)
        if pm3 == 0:
            arcpy.AddError("{3} has no features!".format(param3))
        else:
            arcpy.AddMessage('Buffering BuffDist2 and creating BuffDist3')

    ScriptTool(param0, param1, param2, param3)
