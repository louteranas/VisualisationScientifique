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
renderView1.ViewSize = [1096, 772]
renderView1.InteractionMode = '2D'
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.CenterOfRotation = [1.99999999999091, 45.5, 0.0]
renderView1.StereoType = 0
renderView1.CameraPosition = [2.309656359288365, 44.526794299350854, 10000.0]
renderView1.CameraFocalPoint = [2.309656359288365, 44.526794299350854, 0.0]
renderView1.CameraParallelScale = 8.53766819205841
renderView1.Background = [0.32, 0.34, 0.43]

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'NetCDF Reader'
dataSP1nc = NetCDFReader(FileName=['/user/0/.base/loutera/home/Documents/3a/VisualisationScientifique/Projet/Demo/dataSP1.nc'])
dataSP1nc.Dimensions = '(latitude, longitude)'
dataSP1nc.SphericalCoordinates = 0
dataSP1nc.ReplaceFillValueWithNan = 1

# create a new 'Calculator'
calcwindSpeed = Calculator(Input=dataSP1nc)
calcwindSpeed.ResultArrayName = 'WindSpeed'
calcwindSpeed.Function = 'UGRD_10maboveground*iHat+VGRD_10maboveground*jHat'

# create a new 'Extract Subset'
extractSubset3030 = ExtractSubset(Input=calcwindSpeed)
extractSubset3030.VOI = [0, 800, 0, 600, 0, 0]
extractSubset3030.SampleRateI = 30
extractSubset3030.SampleRateJ = 30

# create a new 'Stream Tracer'
streamTracer1 = StreamTracer(Input=extractSubset3030,
    SeedType='High Resolution Line Source')
streamTracer1.Vectors = ['POINTS', 'WindSpeed']
streamTracer1.IntegrationStepUnit = 'Length'
streamTracer1.MaximumStreamlineLength = 4.679999999995744

# init the 'High Resolution Line Source' selected for 'SeedType'
streamTracer1.SeedType.Point1 = [-7.9557633772430005, 46.736732994464994, -2.2737367544323206e-13]
streamTracer1.SeedType.Point2 = [-1.9036966953216186, 53.00000000000132, -2.2737367544323206e-13]
streamTracer1.SeedType.Resolution = 20

# create a new 'Stream Tracer'
streamTracer3 = StreamTracer(Input=extractSubset3030,
    SeedType='High Resolution Line Source')
streamTracer3.Vectors = ['POINTS', 'WindSpeed']
streamTracer3.IntegrationStepUnit = 'Length'
streamTracer3.MaximumStreamlineLength = 4.68

# init the 'High Resolution Line Source' selected for 'SeedType'
streamTracer3.SeedType.Point1 = [11.994953486064187, 49.05915568919555, -6.536993168992922e-13]
streamTracer3.SeedType.Point2 = [7.872596933926368, 53.02211831137895, -6.536993168992922e-13]
streamTracer3.SeedType.Resolution = 20

# create a new 'Stream Tracer'
streamTracer2 = StreamTracer(Input=extractSubset3030,
    SeedType='High Resolution Line Source')
streamTracer2.Vectors = ['POINTS', 'WindSpeed']
streamTracer2.IntegrationStepUnit = 'Length'
streamTracer2.MaximumStreamlineLength = 4.68

# init the 'High Resolution Line Source' selected for 'SeedType'
streamTracer2.SeedType.Point1 = [-3.2887996764029666, 37.91152675448726, -8.242295734817162e-13]
streamTracer2.SeedType.Point2 = [-7.919877390243858, 41.67542457426466, 0.0]
streamTracer2.SeedType.Resolution = 20

# create a new 'Stream Tracer'
streamTracer5 = StreamTracer(Input=extractSubset3030,
    SeedType='High Resolution Line Source')
streamTracer5.Vectors = ['POINTS', 'WindSpeed']
streamTracer5.IntegrationStepUnit = 'Length'
streamTracer5.MaximumStreamlineLength = 4.68

# init the 'High Resolution Line Source' selected for 'SeedType'
streamTracer5.SeedType.Point1 = [0.9136794854910424, 49.65635009641183, -4.547473508864641e-13]
streamTracer5.SeedType.Point2 = [4.200957245113677, 52.29221403589218, -4.547473508864641e-13]
streamTracer5.SeedType.Resolution = 20

# create a new 'Glyph'
glyphWindVectors = Glyph(Input=extractSubset3030,
    GlyphType='2D Glyph')
glyphWindVectors.Scalars = ['POINTS', 'DSWRF_surface']
glyphWindVectors.Vectors = ['POINTS', 'WindSpeed']
glyphWindVectors.ScaleFactor = 0.359999999999673
glyphWindVectors.GlyphTransform = 'Transform2'

# create a new 'Stream Tracer'
streamTracer4 = StreamTracer(Input=extractSubset3030,
    SeedType='High Resolution Line Source')
streamTracer4.Vectors = ['POINTS', 'WindSpeed']
streamTracer4.IntegrationStepUnit = 'Length'
streamTracer4.MaximumStreamlineLength = 4.68

# init the 'High Resolution Line Source' selected for 'SeedType'
streamTracer4.SeedType.Point1 = [12.083426731577848, 43.330513042193076, -2.1458390619955026e-12]
streamTracer4.SeedType.Point2 = [6.94362785603402, 38.003784885452596, -9.947598300641403e-13]
streamTracer4.SeedType.Resolution = 20

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get color transfer function/color map for 'TMP2maboveground'
tMP2mabovegroundLUT = GetColorTransferFunction('TMP2maboveground')
tMP2mabovegroundLUT.RGBPoints = [256.93798828125, 1.0, 0.988235, 0.968627, 257.65986328125, 1.0, 0.952941, 0.878431, 258.74267578125, 0.968627, 0.905882, 0.776471, 260.54736328125, 0.94902, 0.898039, 0.647059, 262.35205078125, 0.901961, 0.878431, 0.556863, 264.15673828125, 0.847059, 0.858824, 0.482353, 265.96142578125, 0.690196, 0.819608, 0.435294, 267.76611328125, 0.513725, 0.768627, 0.384314, 269.57080078125, 0.337255, 0.721569, 0.337255, 271.37548828125, 0.278431, 0.658824, 0.392157, 273.18017578125, 0.231373, 0.639216, 0.435294, 274.98486328125, 0.203922, 0.6, 0.486275, 276.78955078125, 0.172549, 0.568627, 0.537255, 278.59423828125, 0.141176, 0.517647, 0.54902, 280.39892578125, 0.133333, 0.458824, 0.541176, 282.20361328125, 0.12549, 0.396078, 0.529412, 284.00830078125, 0.117647, 0.321569, 0.521569, 285.81298828125, 0.121569, 0.258824, 0.509804, 287.61767578125, 0.133333, 0.227451, 0.501961, 289.42236328125, 0.145098, 0.192157, 0.490196, 291.22705078125, 0.188235, 0.164706, 0.470588, 293.03173828125, 0.258824, 0.196078, 0.439216]
tMP2mabovegroundLUT.ColorSpace = 'Lab'
tMP2mabovegroundLUT.NanColor = [0.25, 0.0, 0.0]
tMP2mabovegroundLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'TMP2maboveground'
tMP2mabovegroundPWF = GetOpacityTransferFunction('TMP2maboveground')
tMP2mabovegroundPWF.Points = [256.93798828125, 0.0, 0.5, 0.0, 293.03173828125, 1.0, 0.5, 0.0]
tMP2mabovegroundPWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from calcwindSpeed
calcwindSpeedDisplay = Show(calcwindSpeed, renderView1)
# trace defaults for the display properties.
calcwindSpeedDisplay.Representation = 'Slice'
calcwindSpeedDisplay.ColorArrayName = ['POINTS', 'TMP_2maboveground']
calcwindSpeedDisplay.LookupTable = tMP2mabovegroundLUT
calcwindSpeedDisplay.ScalarOpacityUnitDistance = 0.319295596830461

# show color legend
calcwindSpeedDisplay.SetScalarBarVisibility(renderView1, True)

# show data from glyphWindVectors
glyphWindVectorsDisplay = Show(glyphWindVectors, renderView1)
# trace defaults for the display properties.
glyphWindVectorsDisplay.ColorArrayName = ['POINTS', '']
glyphWindVectorsDisplay.DiffuseColor = [1.0, 0.6666666666666666, 0.0]

# show data from streamTracer1
streamTracer1Display = Show(streamTracer1, renderView1)
# trace defaults for the display properties.
streamTracer1Display.ColorArrayName = ['POINTS', '']
streamTracer1Display.DiffuseColor = [1.0, 1.0, 0.4980392156862745]

# show data from streamTracer2
streamTracer2Display = Show(streamTracer2, renderView1)
# trace defaults for the display properties.
streamTracer2Display.ColorArrayName = ['POINTS', '']
streamTracer2Display.DiffuseColor = [1.0, 1.0, 0.4980392156862745]

# show data from streamTracer4
streamTracer4Display = Show(streamTracer4, renderView1)
# trace defaults for the display properties.
streamTracer4Display.ColorArrayName = ['POINTS', '']
streamTracer4Display.DiffuseColor = [1.0, 1.0, 0.4980392156862745]

# show data from streamTracer3
streamTracer3Display = Show(streamTracer3, renderView1)
# trace defaults for the display properties.
streamTracer3Display.ColorArrayName = ['POINTS', '']
streamTracer3Display.DiffuseColor = [1.0, 1.0, 0.4980392156862745]

# show data from streamTracer5
streamTracer5Display = Show(streamTracer5, renderView1)
# trace defaults for the display properties.
streamTracer5Display.ColorArrayName = ['POINTS', '']
streamTracer5Display.DiffuseColor = [1.0, 1.0, 0.4980392156862745]

# setup the color legend parameters for each legend in this view

# get color legend/bar for tMP2mabovegroundLUT in view renderView1
tMP2mabovegroundLUTColorBar = GetScalarBar(tMP2mabovegroundLUT, renderView1)
tMP2mabovegroundLUTColorBar.Position = [0.97, 0.108365758754864]
tMP2mabovegroundLUTColorBar.Title = 'TMP_2maboveground'
tMP2mabovegroundLUTColorBar.ComponentTitle = ''