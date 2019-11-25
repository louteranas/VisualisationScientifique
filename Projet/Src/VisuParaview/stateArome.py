# state file generated using paraview version 5.7.0

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

# trace generated using paraview version 5.7.0
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [1559, 1166]
renderView1.InteractionMode = '2D'
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.CenterOfRotation = [1.99999999999091, 45.5, 0.0]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [1.9848502385286462, 45.4919636394582, 10000.0]
renderView1.CameraFocalPoint = [1.9848502385286462, 45.4919636394582, 0.0]
renderView1.CameraParallelScale = 9.039412339208
renderView1.Background = [0.32, 0.34, 0.43]
renderView1.BackEnd = 'OSPRay raycaster'

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name='Layout #1')
layout1.AssignView(0, renderView1)

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'NetCDF Reader'
dataSP1nc = NetCDFReader(FileName=['/home/ananas/Documents/ProjetImag/3A/VisualisationScientifique/Projet/Demo/dataSP1.nc'])
dataSP1nc.Dimensions = '(latitude, longitude)'
dataSP1nc.SphericalCoordinates = 0
dataSP1nc.ReplaceFillValueWithNan = 1

# create a new 'Calculator'
calcWindspeed = Calculator(Input=dataSP1nc)
calcWindspeed.ResultArrayName = 'Calc :  Wind speed'
calcWindspeed.Function = 'sqrt((UGRD_10maboveground)^2+(VGRD_10maboveground)^2)'

# create a new 'Calculator'
calcwindVectors = Calculator(Input=dataSP1nc)
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
threshold1.ThresholdRange = [3.5, 18.96972868347375]

# create a new 'Calculator'
calcTempsCelcius = Calculator(Input=dataSP1nc)
calcTempsCelcius.ResultArrayName = 'TempsCelc'
calcTempsCelcius.Function = 'TMP_2maboveground - 273.15'

# create a new 'Contour'
contourRafal1 = Contour(Input=threshold1)
contourRafal1.ContourBy = ['POINTS', 'Calc :  Wind speed']
contourRafal1.Isosurfaces = [1.0360908187394047, 1.427283329492765, 1.9661767731196633, 2.7085379779003773, 3.7311894220419517, 5.139959128042107, 7.080632165676826, 9.754037068523276, 13.436828366162102, 18.5101158908178]
contourRafal1.PointMergeMethod = 'Uniform Binning'

# create a new 'Extract Subset'
extractSubset3030 = ExtractSubset(Input=calcwindVectors)
extractSubset3030.VOI = [0, 800, 0, 600, 0, 0]
extractSubset3030.SampleRateI = 30
extractSubset3030.SampleRateJ = 30

# create a new 'GlyphLegacy'
glyphWindVectors = GlyphLegacy(Input=extractSubset3030,
    GlyphType='2D Glyph')
glyphWindVectors.Scalars = ['POINTS', 'DSWRF_surface']
glyphWindVectors.Vectors = ['POINTS', 'WindSpeed']
glyphWindVectors.ScaleFactor = 0.359999999999673
glyphWindVectors.GlyphTransform = 'Transform2'

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from glyphWindVectors
glyphWindVectorsDisplay = Show(glyphWindVectors, renderView1)

# trace defaults for the display properties.
glyphWindVectorsDisplay.Representation = 'Surface'
glyphWindVectorsDisplay.AmbientColor = [0.9372549019607843, 0.9372549019607843, 0.9372549019607843]
glyphWindVectorsDisplay.ColorArrayName = ['POINTS', '']
glyphWindVectorsDisplay.DiffuseColor = [0.9372549019607843, 0.9372549019607843, 0.9372549019607843]
glyphWindVectorsDisplay.Opacity = 0.49
glyphWindVectorsDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
glyphWindVectorsDisplay.ScaleFactor = 2.03443508148193
glyphWindVectorsDisplay.GlyphType = 'Arrow'
glyphWindVectorsDisplay.SetScaleArray = [None, '']
glyphWindVectorsDisplay.ScaleTransferFunction = 'PiecewiseFunction'
glyphWindVectorsDisplay.OpacityArray = [None, '']
glyphWindVectorsDisplay.OpacityTransferFunction = 'PiecewiseFunction'
glyphWindVectorsDisplay.DataAxesGrid = 'GridAxesRepresentation'
glyphWindVectorsDisplay.PolarAxes = 'PolarAxesRepresentation'

# show data from contourRafal1
contourRafal1Display = Show(contourRafal1, renderView1)

# get color transfer function/color map for 'CalcWindspeed'
calcWindspeedLUT = GetColorTransferFunction('CalcWindspeed')
calcWindspeedLUT.RGBPoints = [1.427283329492765, 0.34902, 0.0, 0.129412, 1.521712706071941, 0.4, 0.00392157, 0.101961, 1.622389550814499, 0.470588, 0.0156863, 0.0901961, 1.7297271975776178, 0.54902, 0.027451, 0.0705882, 1.8441663264766763, 0.619608, 0.0627451, 0.0431373, 1.9661767731196633, 0.690196, 0.12549, 0.0627451, 2.0962594575409326, 0.741176, 0.184314, 0.0745098, 2.234948440753635, 0.788235, 0.266667, 0.0941176, 2.3828131173641083, 0.811765, 0.345098, 0.113725, 2.5404605532501146, 0.831373, 0.411765, 0.133333, 2.7085379779003773, 0.85098, 0.47451, 0.145098, 2.8877354416478522, 0.870588, 0.54902, 0.156863, 3.0787886487061225, 0.878431, 0.619608, 0.168627, 3.282481977640107, 0.890196, 0.658824, 0.196078, 3.4996517016717688, 0.909804, 0.717647, 0.235294, 3.731189422041951, 0.929412, 0.776471, 0.278431, 3.9326582682660027, 0.94902, 0.823529, 0.321569, 4.175506130704372, 0.968627, 0.87451, 0.407843, 4.456015682207316, 0.980392, 0.917647, 0.509804, 4.7614422270840695, 0.988235, 0.956863, 0.643137, 4.928197348356701, 0.992157, 0.964706, 0.713725, 5.1268046156572, 0.988235, 0.980392, 0.870588, 5.139959128042105, 1.0, 1.0, 1.0, 5.153147392677985, 0.913725, 0.988235, 0.937255, 5.360820188492004, 0.827451, 0.980392, 0.886275, 5.5698212428248794, 0.764706, 0.980392, 0.866667, 5.794360313146933, 0.658824, 0.980392, 0.843137, 6.058769171405769, 0.572549, 0.964706, 0.835294, 6.43290774178609, 0.423529, 0.941176, 0.87451, 6.743627402588857, 0.262745, 0.901961, 0.862745, 7.169200170245875, 0.0705882, 0.854902, 0.870588, 7.582843002737545, 0.0509804, 0.8, 0.85098, 8.185650743955334, 0.0235294, 0.709804, 0.831373, 8.870228393702163, 0.0313725, 0.615686, 0.811765, 9.754037068523276, 0.0313725, 0.537255, 0.788235, 10.399366289763577, 0.0392157, 0.466667, 0.768627, 11.087390633122133, 0.0509804, 0.396078, 0.741176, 11.820934817196363, 0.054902, 0.317647, 0.709804, 12.603010444582566, 0.054902, 0.243137, 0.678431, 13.436828366162109, 0.0431373, 0.164706, 0.639216, 14.325811863411383, 0.0313725, 0.0980392, 0.6, 15.273610702856438, 0.0392157, 0.0392157, 0.560784, 16.284116120373167, 0.105882, 0.0509804, 0.509804, 17.361476796852315, 0.113725, 0.0235294, 0.45098, 18.5101158908178, 0.12549, 0.0, 0.380392]
calcWindspeedLUT.UseLogScale = 1
calcWindspeedLUT.ColorSpace = 'Lab'
calcWindspeedLUT.NanColor = [0.250004, 0.0, 0.0]
calcWindspeedLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
contourRafal1Display.Representation = 'Surface'
contourRafal1Display.ColorArrayName = ['POINTS', 'Calc :  Wind speed']
contourRafal1Display.LookupTable = calcWindspeedLUT
contourRafal1Display.Opacity = 0.77
contourRafal1Display.OSPRayScaleFunction = 'PiecewiseFunction'
contourRafal1Display.SelectOrientationVectors = 'None'
contourRafal1Display.ScaleFactor = -2.0000000000000002e+298
contourRafal1Display.SelectScaleArray = 'None'
contourRafal1Display.GlyphType = 'Arrow'
contourRafal1Display.GlyphTableIndexArray = 'None'
contourRafal1Display.GaussianRadius = -1e+297
contourRafal1Display.SetScaleArray = [None, '']
contourRafal1Display.ScaleTransferFunction = 'PiecewiseFunction'
contourRafal1Display.OpacityArray = [None, '']
contourRafal1Display.OpacityTransferFunction = 'PiecewiseFunction'
contourRafal1Display.DataAxesGrid = 'GridAxesRepresentation'
contourRafal1Display.PolarAxes = 'PolarAxesRepresentation'

# show data from calcTempsCelcius
calcTempsCelciusDisplay = Show(calcTempsCelcius, renderView1)

# get color transfer function/color map for 'TempsCelc'
tempsCelcLUT = GetColorTransferFunction('TempsCelc')
tempsCelcLUT.AutomaticRescaleRangeMode = 'Never'
tempsCelcLUT.EnableOpacityMapping = 1
tempsCelcLUT.RGBPoints = [0.0019881738281250024, 0.0862745098039216, 0.00392156862745098, 0.298039215686275, 0.6050249959112263, 0.113725, 0.0235294, 0.45098, 1.1058509518382205, 0.105882, 0.0509804, 0.509804, 1.4533635274700516, 0.0392157, 0.0392157, 0.560784, 1.7906555210082233, 0.0313725, 0.0980392, 0.6, 2.1177257702303653, 0.0431373, 0.164706, 0.639216, 2.58788881765389, 0.054902, 0.243137, 0.678431, 3.2113675698169533, 0.054902, 0.317647, 0.709804, 3.9779381953124737, 0.0509804, 0.396078, 0.741176, 4.474931947998025, 0.0392157, 0.466667, 0.768627, 4.971925700683576, 0.0313725, 0.537255, 0.788235, 5.49063989450054, 0.0313725, 0.615686, 0.811765, 6.022128758930943, 0.0235294, 0.709804, 0.831373, 6.553618785583658, 0.0509804, 0.8, 0.85098, 6.993118924503713, 0.0705882, 0.854902, 0.870588, 7.401957317142483, 0.262745, 0.901961, 0.862745, 7.759690474868096, 0.423529, 0.941176, 0.87451, 8.31162166570831, 0.572549, 0.964706, 0.835294, 8.67957656774989, 0.658824, 0.980392, 0.843137, 8.945320999965093, 0.764706, 0.980392, 0.866667, 9.231507177478951, 0.827451, 0.980392, 0.886275, 9.793659531523982, 0.913725, 0.988235, 0.937255, 9.967415819339926, 1.0, 1.0, 0.972549019607843, 10.141172107155874, 0.988235, 0.980392, 0.870588, 10.396695957277293, 0.992156862745098, 0.972549019607843, 0.803921568627451, 10.590893990391896, 0.992157, 0.964706, 0.713725, 10.91796423961404, 0.988235, 0.956863, 0.643137, 11.439232521950721, 0.980392, 0.917647, 0.509804, 11.878733823093025, 0.968627, 0.87451, 0.407843, 12.32845570632905, 0.94902, 0.823529, 0.321569, 12.655525955551177, 0.929412, 0.776471, 0.278431, 13.135910747290666, 0.909804, 0.717647, 0.235294, 13.565190304116975, 0.890196, 0.658824, 0.196078, 13.91781324902345, 0.878431, 0.619608, 0.168627, 14.414807001708995, 0.870588, 0.54902, 0.156863, 14.911800754394546, 0.85098, 0.47451, 0.145098, 15.408794507080092, 0.831373, 0.411765, 0.133333, 15.905788259765643, 0.811765, 0.345098, 0.113725, 16.40278201245119, 0.788235, 0.266667, 0.0941176, 16.899775765136738, 0.741176, 0.184314, 0.0745098, 17.396769517822285, 0.690196, 0.12549, 0.0627451, 17.893763270507833, 0.619608, 0.0627451, 0.0431373, 18.358816586154216, 0.54902, 0.027451, 0.0705882, 18.7676546337583, 0.470588, 0.0156863, 0.0901961, 19.227597407803348, 0.4, 0.00392157, 0.101961, 19.881738281250023, 0.188235294117647, 0.0, 0.0705882352941176]
tempsCelcLUT.ColorSpace = 'Lab'
tempsCelcLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'TempsCelc'
tempsCelcPWF = GetOpacityTransferFunction('TempsCelc')
tempsCelcPWF.Points = [0.0019881738281250024, 0.0, 0.5, 0.0, 19.881738281250023, 1.0, 0.5, 0.0]
tempsCelcPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
calcTempsCelciusDisplay.Representation = 'Slice'
calcTempsCelciusDisplay.ColorArrayName = ['POINTS', 'TempsCelc']
calcTempsCelciusDisplay.LookupTable = tempsCelcLUT
calcTempsCelciusDisplay.OSPRayScaleArray = 'TempsCelc'
calcTempsCelciusDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
calcTempsCelciusDisplay.SelectOrientationVectors = 'DSWRF_surface'
calcTempsCelciusDisplay.ScaleFactor = 1.999999999998181
calcTempsCelciusDisplay.SelectScaleArray = 'TempsCelc'
calcTempsCelciusDisplay.GlyphType = 'Arrow'
calcTempsCelciusDisplay.GlyphTableIndexArray = 'TempsCelc'
calcTempsCelciusDisplay.GaussianRadius = 0.09999999999990905
calcTempsCelciusDisplay.SetScaleArray = ['POINTS', 'TempsCelc']
calcTempsCelciusDisplay.ScaleTransferFunction = 'PiecewiseFunction'
calcTempsCelciusDisplay.OpacityArray = ['POINTS', 'TempsCelc']
calcTempsCelciusDisplay.OpacityTransferFunction = 'PiecewiseFunction'
calcTempsCelciusDisplay.DataAxesGrid = 'GridAxesRepresentation'
calcTempsCelciusDisplay.PolarAxes = 'PolarAxesRepresentation'
calcTempsCelciusDisplay.ScalarOpacityUnitDistance = 0.3192955968304612
calcTempsCelciusDisplay.ScalarOpacityFunction = tempsCelcPWF
calcTempsCelciusDisplay.IsosurfaceValues = [1.8348632812500227]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
calcTempsCelciusDisplay.ScaleTransferFunction.Points = [-16.212011718749977, 0.0, 0.5, 0.0, 19.881738281250023, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
calcTempsCelciusDisplay.OpacityTransferFunction.Points = [-16.212011718749977, 0.0, 0.5, 0.0, 19.881738281250023, 1.0, 0.5, 0.0]

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get opacity transfer function/opacity map for 'CalcWindspeed'
calcWindspeedPWF = GetOpacityTransferFunction('CalcWindspeed')
calcWindspeedPWF.Points = [1.427283329492765, 0.0, 0.5, 0.0, 18.5101158908178, 1.0, 0.5, 0.0]
calcWindspeedPWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# finally, restore active source
SetActiveSource(glyphWindVectors)
# ----------------------------------------------------------------