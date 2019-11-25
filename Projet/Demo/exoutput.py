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
renderView1.ViewSize = [814, 539]
renderView1.InteractionMode = '2D'
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.CenterOfRotation = [1.999999999987267, 46.45, 0.0]
renderView1.StereoType = 0
renderView1.CameraPosition = [1.999999999987267, 46.45, 10000.0]
renderView1.CameraFocalPoint = [1.999999999987267, 46.45, 0.0]
renderView1.CameraParallelScale = 16.616332326949994
renderView1.Background = [0.32, 0.34, 0.43]

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'NetCDF Reader'
resultatnc = NetCDFReader(FileName=['/user/8/.base/desobryd/home/Desktop/3A/visualisationscientifique/VisualisationScientifique/VisualisationScientifique/Projet/Src/data/resultat.nc'])
resultatnc.Dimensions = '(latitude, longitude)'
resultatnc.SphericalCoordinates = 0
resultatnc.ReplaceFillValueWithNan = 1

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get color transfer function/color map for 'RH2maboveground'
rH2mabovegroundLUT = GetColorTransferFunction('RH2maboveground')
rH2mabovegroundLUT.RGBPoints = [19.5076904296875, 0.231373, 0.298039, 0.752941, 59.7576904296875, 0.865003, 0.865003, 0.865003, 100.0076904296875, 0.705882, 0.0156863, 0.14902]
rH2mabovegroundLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'RH2maboveground'
rH2mabovegroundPWF = GetOpacityTransferFunction('RH2maboveground')
rH2mabovegroundPWF.Points = [19.5076904296875, 0.0, 0.5, 0.0, 100.0076904296875, 1.0, 0.5, 0.0]
rH2mabovegroundPWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from resultatnc
resultatncDisplay = Show(resultatnc, renderView1)
# trace defaults for the display properties.
resultatncDisplay.Representation = 'Slice'
resultatncDisplay.ColorArrayName = ['POINTS', 'RH_2maboveground']
resultatncDisplay.LookupTable = rH2mabovegroundLUT
resultatncDisplay.ScalarOpacityUnitDistance = 0.1941905735298652

# show color legend
resultatncDisplay.SetScalarBarVisibility(renderView1, True)

# setup the color legend parameters for each legend in this view

# get color legend/bar for rH2mabovegroundLUT in view renderView1
rH2mabovegroundLUTColorBar = GetScalarBar(rH2mabovegroundLUT, renderView1)
rH2mabovegroundLUTColorBar.Title = 'RH_2maboveground'
rH2mabovegroundLUTColorBar.ComponentTitle = ''

Interact()
WriteImage('exemple.png')
