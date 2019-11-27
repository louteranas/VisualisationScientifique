# state file generated using paraview version 4.4.0

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------


from datetime import datetime

def writeentete(fichier):
    fichier.write("""<?xml version="1.0" encoding="UTF-8"?>
    <kml xmlns="http://www.opengis.net/kml/2.2">
      <Folder>
        <name>Ground Overlays</name>
        <description>Examples of ground overlays</description>
    """)

def writeoverlay(fichier, dt_object, i):
    fichier.write(""" <GroundOverlay>
  <name>Large-scale overlay on terrain</name>
  <description>Overlay shows Mount Etna erupting
      on July 13th, 2001.</description>
  <TimeSpan>
      <begin>""" + "T".join(str(dt_object).split(" ")) + """</begin>
  </TimeSpan>
  <Icon>
    <href>./SP1out""" + str(i) + """.png</href>
  </Icon>
  <LatLonBox>
    <north>53.4</north>
    <south>38</south>
    <east>12</east>
    <west>-8</west>
    <rotation>0.01</rotation>
  </LatLonBox>
</GroundOverlay>""")

def writefooter(fichier):
    fichier.write("""
      </Folder>
    </kml>
    """)

# state file generated using paraview version 4.4.0

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [1514, 1132]
renderView1.InteractionMode = '2D'
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.OrientationAxesVisibility = 0
renderView1.CenterOfRotation = [1.99999999999091, 45.5, 0.0]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [1.98485023852865, 45.4919636394582, 10000.0]
renderView1.CameraFocalPoint = [1.98485023852865, 45.4919636394582, 0.0]
renderView1.CameraParallelScale = 7.470588710089256
renderView1.Background = [0.32, 0.34, 0.43]

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'NetCDF Reader'
resultatnc = NetCDFReader(FileName=['resultatSP1IP2.nc'])
resultatnc.Dimensions = '(latitude, longitude)'
resultatnc.SphericalCoordinates = 0
resultatnc.ReplaceFillValueWithNan = 1

# create a new 'Calculator'
calcWindspeed = Calculator(Input=resultatnc)
calcWindspeed.ResultArrayName = 'Calc :  Wind speed'
calcWindspeed.Function = 'sqrt((UGRD_10maboveground)^2+(VGRD_10maboveground)^2)'

# create a new 'Calculator'
calcTempsCelcius = Calculator(Input=resultatnc)
calcTempsCelcius.ResultArrayName = 'TempsCelc'
calcTempsCelcius.Function = 'TMP_2maboveground - 273.15'

# create a new 'Calculator'
calcwindVectors = Calculator(Input=resultatnc)
calcwindVectors.ResultArrayName = 'WindSpeed'
calcwindVectors.Function = 'UGRD_10maboveground*iHat+VGRD_10maboveground*jHat'

# create a new 'Extract Subset'
extractSubset1 = ExtractSubset(Input=calcWindspeed)
extractSubset1.VOI = [0, 800, 0, 600, 0, 0]
extractSubset1.SampleRateI = 10
extractSubset1.SampleRateJ = 10

# create a new 'Threshold'
threshold1 = Threshold(Input=extractSubset1)
threshold1.Scalars = ['POINTS', 'Calc :  Wind speed']
threshold1.ThresholdRange = [3.5, 18.9697286834738]

# create a new 'Extract Subset'
extractSubset3030 = ExtractSubset(Input=calcwindVectors)
extractSubset3030.VOI = [0, 800, 0, 600, 0, 0]
extractSubset3030.SampleRateI = 30
extractSubset3030.SampleRateJ = 30

# create a new 'Glyph'
glyphwindvectors = Glyph(Input=extractSubset3030,
    GlyphType='2D Glyph')
glyphwindvectors.Scalars = [None, 'DSWRF_surface']
glyphwindvectors.Vectors = [None, 'WindSpeed']
glyphwindvectors.ScaleFactor = 0.35
glyphwindvectors.GlyphTransform = 'Transform2'

# create a new 'Contour'
contourRafal1 = Contour(Input=threshold1)
contourRafal1.ContourBy = ['POINTS', 'Calc :  Wind speed']
contourRafal1.ComputeScalars = 1
contourRafal1.OutputPointsPrecision = 'Same as input'
contourRafal1.Isosurfaces = [1.0360908187394, 1.42728332949276, 1.96617677311966, 2.70853797790038, 3.73118942204195, 5.13995912804211, 7.08063216567683, 9.75403706852328, 13.4368283661621, 18.5101158908178]
contourRafal1.PointMergeMethod = 'Uniform Binning'

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get color transfer function/color map for 'CalcWindspeed'
calcWindspeedLUT = GetColorTransferFunction('CalcWindspeed')
calcWindspeedLUT.RGBPoints = [1.42728332949276, 0.34902, 0.0, 0.129412, 1.52171270607194, 0.4, 0.00392157, 0.101961, 1.6223895508145, 0.470588, 0.0156863, 0.0901961, 1.72972719757762, 0.54902, 0.027451, 0.0705882, 1.84416632647668, 0.619608, 0.0627451, 0.0431373, 1.96617677311966, 0.690196, 0.12549, 0.0627451, 2.09625945754093, 0.741176, 0.184314, 0.0745098, 2.23494844075364, 0.788235, 0.266667, 0.0941176, 2.38281311736411, 0.811765, 0.345098, 0.113725, 2.54046055325011, 0.831373, 0.411765, 0.133333, 2.70853797790038, 0.85098, 0.47451, 0.145098, 2.88773544164785, 0.870588, 0.54902, 0.156863, 3.07878864870612, 0.878431, 0.619608, 0.168627, 3.28248197764011, 0.890196, 0.658824, 0.196078, 3.49965170167177, 0.909804, 0.717647, 0.235294, 3.73118942204195, 0.929412, 0.776471, 0.278431, 3.932658268266, 0.94902, 0.823529, 0.321569, 4.17550613070437, 0.968627, 0.87451, 0.407843, 4.45601568220732, 0.980392, 0.917647, 0.509804, 4.76144222708407, 0.988235, 0.956863, 0.643137, 4.9281973483567, 0.992157, 0.964706, 0.713725, 5.1268046156572, 0.988235, 0.980392, 0.870588, 5.13995912804211, 1.0, 1.0, 1.0, 5.15314739267798, 0.913725, 0.988235, 0.937255, 5.360820188492, 0.827451, 0.980392, 0.886275, 5.56982124282488, 0.764706, 0.980392, 0.866667, 5.79436031314693, 0.658824, 0.980392, 0.843137, 6.05876917140577, 0.572549, 0.964706, 0.835294, 6.43290774178609, 0.423529, 0.941176, 0.87451, 6.74362740258886, 0.262745, 0.901961, 0.862745, 7.16920017024588, 0.0705882, 0.854902, 0.870588, 7.58284300273754, 0.0509804, 0.8, 0.85098, 8.18565074395533, 0.0235294, 0.709804, 0.831373, 8.87022839370216, 0.0313725, 0.615686, 0.811765, 9.75403706852328, 0.0313725, 0.537255, 0.788235, 10.3993662897636, 0.0392157, 0.466667, 0.768627, 11.0873906331221, 0.0509804, 0.396078, 0.741176, 11.8209348171964, 0.054902, 0.317647, 0.709804, 12.6030104445826, 0.054902, 0.243137, 0.678431, 13.4368283661621, 0.0431373, 0.164706, 0.639216, 14.3258118634114, 0.0313725, 0.0980392, 0.6, 15.2736107028564, 0.0392157, 0.0392157, 0.560784, 16.2841161203732, 0.105882, 0.0509804, 0.509804, 17.3614767968523, 0.113725, 0.0235294, 0.45098, 18.5101158908178, 0.12549, 0.0, 0.380392]
calcWindspeedLUT.UseLogScale = 1
calcWindspeedLUT.ColorSpace = 'Lab'
calcWindspeedLUT.AboveRangeColor = [0.5, 0.5, 0.5]
calcWindspeedLUT.NanColor = [0.250004, 0.0, 0.0]
calcWindspeedLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'CalcWindspeed'
calcWindspeedPWF = GetOpacityTransferFunction('CalcWindspeed')
calcWindspeedPWF.Points = [1.42728332949276, 0.0, 0.5, 0.0, 18.5101158908178, 1.0, 0.5, 0.0]
calcWindspeedPWF.ScalarRangeInitialized = 1

# get color transfer function/color map for 'TempsCelc'
tempsCelcLUT = GetColorTransferFunction('TempsCelc')
tempsCelcLUT.EnableOpacityMapping = 1
tempsCelcLUT.RGBPoints = [-12.3609375, 0.0862745098039216, 0.00392156862745098, 0.298039215686275, -11.3828809030349, 0.113725, 0.0235294, 0.45098, -10.5705986141464, 0.105882, 0.0509804, 0.509804, -10.0069730531882, 0.0392157, 0.0392157, 0.560784, -9.4599241047609, 0.0313725, 0.0980392, 0.6, -8.92945365385593, 0.0431373, 0.164706, 0.639216, -8.1669030875517, 0.054902, 0.243137, 0.678431, -7.15569202333481, 0.054902, 0.317647, 0.709804, -5.91240234375003, 0.0509804, 0.396078, 0.741176, -5.10633544921877, 0.0392157, 0.466667, 0.768627, -4.30026855468752, 0.0313725, 0.537255, 0.788235, -3.45897359453966, 0.0313725, 0.615686, 0.811765, -2.59695958306693, 0.0235294, 0.709804, 0.831373, -1.73494368660284, 0.0509804, 0.8, 0.85098, -1.0221248428829, 0.0705882, 0.854902, 0.870588, -0.359035836756119, 0.262745, 0.901961, 0.862745, 0.22116633673315, 0.423529, 0.941176, 0.87451, 1.1163354582593, 0.572549, 0.964706, 0.835294, 1.71311612927081, 0.658824, 0.980392, 0.843137, 2.14412313500717, 0.764706, 0.980392, 0.866667, 2.60828430830128, 0.827451, 0.980392, 0.886275, 3.52003098485399, 0.913725, 0.988235, 0.937255, 3.80184376533314, 1.0, 1.0, 0.972549019607843, 4.08365654581228, 0.988235, 0.980392, 0.870588, 4.49808693901756, 0.992156862745098, 0.972549019607843, 0.803921568627451, 4.81305388705445, 0.992157, 0.964706, 0.713725, 5.34352433795942, 0.988235, 0.956863, 0.643137, 6.18896173690117, 0.980392, 0.917647, 0.509804, 6.90178246561236, 0.968627, 0.87451, 0.407843, 7.63117980685453, 0.94902, 0.823529, 0.321569, 8.16165025775947, 0.929412, 0.776471, 0.278431, 8.94077932158593, 0.909804, 0.717647, 0.235294, 9.63702155277484, 0.890196, 0.658824, 0.196078, 10.208935546875, 0.878431, 0.619608, 0.168627, 11.0150024414063, 0.870588, 0.54902, 0.156863, 11.8210693359375, 0.85098, 0.47451, 0.145098, 12.6271362304688, 0.831373, 0.411765, 0.133333, 13.433203125, 0.811765, 0.345098, 0.113725, 14.2392700195313, 0.788235, 0.266667, 0.0941176, 15.0453369140625, 0.741176, 0.184314, 0.0745098, 15.8514038085938, 0.690196, 0.12549, 0.0627451, 16.657470703125, 0.619608, 0.0627451, 0.0431373, 17.4117338702351, 0.54902, 0.027451, 0.0705882, 18.0748223167552, 0.470588, 0.0156863, 0.0901961, 18.8207967712292, 0.4, 0.00392157, 0.101961, 19.88173828125, 0.188235294117647, 0.0, 0.0705882352941176]
tempsCelcLUT.ColorSpace = 'Lab'
tempsCelcLUT.AboveRangeColor = [0.5, 0.5, 0.5]
tempsCelcLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'TempsCelc'
tempsCelcPWF = GetOpacityTransferFunction('TempsCelc')
tempsCelcPWF.Points = [-12.3609375, 0.0, 0.5, 0.0, 19.88173828125, 1.0, 0.5, 0.0]
tempsCelcPWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from contourRafal1
contourRafal1Display = Show(contourRafal1, renderView1)
# trace defaults for the display properties.
contourRafal1Display.ColorArrayName = ['POINTS', 'Calc :  Wind speed']
contourRafal1Display.LookupTable = calcWindspeedLUT
contourRafal1Display.Opacity = 0.77

# show data from calcTempsCelcius
calcTempsCelciusDisplay = Show(calcTempsCelcius, renderView1)
# trace defaults for the display properties.
calcTempsCelciusDisplay.Representation = 'Slice'
calcTempsCelciusDisplay.ColorArrayName = ['POINTS', 'TempsCelc']
calcTempsCelciusDisplay.LookupTable = tempsCelcLUT
calcTempsCelciusDisplay.ScalarOpacityUnitDistance = 0.319295596830461

# show data from glyphwindvectors
glyphwindvectorsDisplay = Show(glyphwindvectors, renderView1)
# trace defaults for the display properties.
glyphwindvectorsDisplay.ColorArrayName = ['POINTS', '']
glyphwindvectorsDisplay.Opacity = 0.5

# hello commence ici

tempsAnimation = resultatnc.TimestepValues

mon_fichier = open("fileSP1.kml", "w")
mon_fichier.close()
mon_fichier = open("fileSP1.kml", "a")
writeentete(mon_fichier)
for i, t in enumerate(tempsAnimation):
    renderView1.ViewTime = t
    dt_object = datetime.fromtimestamp(int(t))
    SaveScreenshot("SP1out" + str(i) + ".png")
    writeoverlay(mon_fichier, dt_object, i)
writefooter(mon_fichier)

mon_fichier.close()
