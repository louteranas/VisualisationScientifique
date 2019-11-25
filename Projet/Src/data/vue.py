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
renderView1.ViewSize = [936, 772]
renderView1.InteractionMode = '2D'
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.CenterOfRotation = [2.1498055458068848, 45.58517837524414, 0.0]
renderView1.StereoType = 0
renderView1.CameraPosition = [2.1498055458068848, 45.58517837524414, 58.17670546302336]
renderView1.CameraFocalPoint = [2.1498055458068848, 45.58517837524414, 0.0]
renderView1.CameraParallelScale = 15.057239355150308
renderView1.Background = [0.32, 0.34, 0.43]

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'NetCDF Reader'
dataSP1nc = NetCDFReader(FileName=['resultat.nc'])
dataSP1nc.Dimensions = '(latitude, longitude)'
dataSP1nc.SphericalCoordinates = 0
dataSP1nc.ReplaceFillValueWithNan = 1

# create a new 'Calculator'
calculator1 = Calculator(Input=dataSP1nc)
calculator1.ResultArrayName = 'windVector'
calculator1.Function = 'UGUST_10maboveground*iHat+VGRD_10maboveground*jHat'

# create a new 'Glyph'
glyph1 = Glyph(Input=calculator1,
    GlyphType='Arrow')
glyph1.Scalars = ['POINTS', 'DSWRF_surface']
glyph1.Vectors = ['POINTS', 'windVector']
glyph1.ScaleFactor = 1.999999999998181
glyph1.GlyphTransform = 'Transform2'

# create a new 'Extract Subset'
extractSubset1 = ExtractSubset(Input=dataSP1nc)
extractSubset1.VOI = [0, 800, 0, 600, 0, 0]

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get color transfer function/color map for 'TMP2maboveground'
tMP2mabovegroundLUT = GetColorTransferFunction('TMP2maboveground')
tMP2mabovegroundLUT.RGBPoints = [256.9379882812499, 0.0, 1.0, 1.0, 263.1525999627097, 0.0, 0.0, 1.0, 265.8920581451648, 0.0, 0.0, 0.501960784314, 270.3777335680224, 1.0, 0.0, 0.0, 293.0317382812499, 1.0, 1.0, 0.0]
tMP2mabovegroundLUT.UseLogScale = 1
tMP2mabovegroundLUT.ColorSpace = 'RGB'
tMP2mabovegroundLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'TMP2maboveground'
tMP2mabovegroundPWF = GetOpacityTransferFunction('TMP2maboveground')
tMP2mabovegroundPWF.Points = [256.93798828125, 0.0, 0.5, 0.0, 266.12547372017895, 0.30263158679008484, 0.5, 0.0, 288.10985163239314, 0.42105263471603394, 0.5, 0.0, 293.03173828125, 1.0, 0.5, 0.0]
tMP2mabovegroundPWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from dataSP1nc
dataSP1ncDisplay = Show(dataSP1nc, renderView1)
# trace defaults for the display properties.
dataSP1ncDisplay.Representation = 'Slice'
dataSP1ncDisplay.ColorArrayName = ['POINTS', 'TMP_2maboveground']
dataSP1ncDisplay.LookupTable = tMP2mabovegroundLUT
dataSP1ncDisplay.ScalarOpacityUnitDistance = 0.3192955968304613

# show color legend
dataSP1ncDisplay.SetScalarBarVisibility(renderView1, True)

# setup the color legend parameters for each legend in this view

# get color legend/bar for tMP2mabovegroundLUT in view renderView1
tMP2mabovegroundLUTColorBar = GetScalarBar(tMP2mabovegroundLUT, renderView1)
tMP2mabovegroundLUTColorBar.Position = [0.9655080213903743, 0.040920881971465664]
tMP2mabovegroundLUTColorBar.Title = 'TMP_2maboveground'
tMP2mabovegroundLUTColorBar.ComponentTitle = ''


WriteImage('../out.png')
