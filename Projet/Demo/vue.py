# state file generated using paraview version 4.4.0

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

#### import the simple module from the paraview
from paraview.simple import *
import sys
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [1335, 1132]
renderView1.InteractionMode = '2D'
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.CenterOfRotation = [1.999999999987267, 46.45, 0.0]
renderView1.StereoType = 0
renderView1.CameraPosition = [1.999999999987267, 46.45, 10000.0]
renderView1.CameraFocalPoint = [1.999999999987267, 46.45, 0.0]
renderView1.CameraParallelScale = 19.15062186170783
renderView1.Background = [0.32, 0.34, 0.43]

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'NetCDF Reader'
donneesnc = NetCDFReader(FileName=['/user/0/.base/loutera/home/Documents/3a/Visu/donnees.nc'])
donneesnc.Dimensions = '(latitude, longitude)'
donneesnc.SphericalCoordinates = 0
donneesnc.ReplaceFillValueWithNan = 1

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get color transfer function/color map for 'RH100maboveground'
rH100mabovegroundLUT = GetColorTransferFunction('RH100maboveground')
rH100mabovegroundLUT.RGBPoints = [11.599690437316895, 0.231373, 0.298039, 0.752941, 55.80281686782837, 0.865003, 0.865003, 0.865003, 100.00594329833984, 0.705882, 0.0156863, 0.14902]
rH100mabovegroundLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'RH100maboveground'
rH100mabovegroundPWF = GetOpacityTransferFunction('RH100maboveground')
rH100mabovegroundPWF.Points = [11.599690437316895, 0.0, 0.5, 0.0, 100.00594329833984, 1.0, 0.5, 0.0]
rH100mabovegroundPWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from donneesnc
donneesncDisplay = Show(donneesnc, renderView1)
# trace defaults for the display properties.
donneesncDisplay.Representation = 'Slice'
donneesncDisplay.ColorArrayName = ['POINTS', 'RH_100maboveground']
donneesncDisplay.LookupTable = rH100mabovegroundLUT
donneesncDisplay.ScalarOpacityUnitDistance = 0.1941905735298652

# show color legend
donneesncDisplay.SetScalarBarVisibility(renderView1, True)

# setup the color legend parameters for each legend in this view

# get color legend/bar for rH100mabovegroundLUT in view renderView1
rH100mabovegroundLUTColorBar = GetScalarBar(rH100mabovegroundLUT, renderView1)
rH100mabovegroundLUTColorBar.Position = [0.8493103448275863, 0.2763483642793988]
rH100mabovegroundLUTColorBar.Position2 = [0.11999999999999933, 0.4299999999999997]
rH100mabovegroundLUTColorBar.Title = 'RH_100maboveground'
rH100mabovegroundLUTColorBar.ComponentTitle = ''

WriteImage(sys.argv[1] + '.png')
