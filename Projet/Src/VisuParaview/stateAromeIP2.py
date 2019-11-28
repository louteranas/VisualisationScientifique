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
renderView1.ViewSize = [1007, 772]
renderView1.InteractionMode = '2D'
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.OrientationAxesVisibility = 0
renderView1.CenterOfRotation = [2.1769464910180214, 45.47788168862161, 0.0]
renderView1.StereoType = 0
renderView1.CameraPosition = [1.9418164342759912, 45.47788168862161, 10000.0]
renderView1.CameraFocalPoint = [1.9418164342759912, 45.47788168862161, 0.0]
renderView1.CameraParallelScale = 7.563350158535305
renderView1.Background = [0.32, 0.34, 0.43]

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'NetCDF Reader'
resultatIP2nc = NetCDFReader(FileName=['/user/0/.base/loutera/home/Documents/3a/VisualisationScientifique/Projet/Src/data/resultatIP2.nc'])
resultatIP2nc.Dimensions = '(latitude, longitude)'
resultatIP2nc.SphericalCoordinates = 0
resultatIP2nc.ReplaceFillValueWithNan = 1

# create a new 'Threshold'
cLD350MB = Threshold(Input=resultatIP2nc)
cLD350MB.Scalars = ['POINTS', 'TCDC_350mb']
cLD350MB.ThresholdRange = [0.57, 1.0]

# create a new 'Threshold'
cLD200MB = Threshold(Input=resultatIP2nc)
cLD200MB.Scalars = ['POINTS', 'TCDC_200mb']
cLD200MB.ThresholdRange = [0.59, 1.0]

# create a new 'Threshold'
cLD450MB = Threshold(Input=resultatIP2nc)
cLD450MB.Scalars = ['POINTS', 'TCDC_450mb']
cLD450MB.ThresholdRange = [0.59, 1.0]

# create a new 'Threshold'
cLD700MB = Threshold(Input=resultatIP2nc)
cLD700MB.Scalars = ['POINTS', 'TCDC_700mb']
cLD700MB.ThresholdRange = [0.6, 1.0]

# create a new 'Threshold'
cLD500MB = Threshold(Input=resultatIP2nc)
cLD500MB.Scalars = ['POINTS', 'TCDC_500mb']
cLD500MB.ThresholdRange = [0.58, 1.0]

# create a new 'Threshold'
cLD250MB = Threshold(Input=resultatIP2nc)
cLD250MB.Scalars = ['POINTS', 'TCDC_250mb']
cLD250MB.ThresholdRange = [0.57, 1.0]

# create a new 'Threshold'
cLD400MB = Threshold(Input=resultatIP2nc)
cLD400MB.Scalars = ['POINTS', 'TCDC_400mb']
cLD400MB.ThresholdRange = [0.57, 1.0]

# create a new 'Threshold'
cLD300MB = Threshold(Input=resultatIP2nc)
cLD300MB.Scalars = ['POINTS', 'TCDC_300mb']
cLD300MB.ThresholdRange = [0.59, 1.0]

# create a new 'Threshold'
cLD600MB = Threshold(Input=resultatIP2nc)
cLD600MB.Scalars = ['POINTS', 'TCDC_600mb']
cLD600MB.ThresholdRange = [0.6, 1.0]

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get color transfer function/color map for 'SCLIWC1000mb'
sCLIWC1000mbLUT = GetColorTransferFunction('SCLIWC1000mb')
sCLIWC1000mbLUT.RGBPoints = [0.0, 0.9176470588235294, 0.9176470588235294, 0.9176470588235294, 0.0005499422550201416, 1.0, 1.0, 1.0]
sCLIWC1000mbLUT.ColorSpace = 'RGB'
sCLIWC1000mbLUT.NanColor = [1.0, 0.0, 0.0]
sCLIWC1000mbLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'SCLIWC1000mb'
sCLIWC1000mbPWF = GetOpacityTransferFunction('SCLIWC1000mb')
sCLIWC1000mbPWF.Points = [0.0, 0.0, 0.5, 0.0, 0.0005499422550201416, 1.0, 0.5, 0.0]
sCLIWC1000mbPWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from cLD250MB
cLD250MBDisplay = Show(cLD250MB, renderView1)
# trace defaults for the display properties.
cLD250MBDisplay.ColorArrayName = ['POINTS', 'SCLIWC_1000mb']
cLD250MBDisplay.LookupTable = sCLIWC1000mbLUT
cLD250MBDisplay.Opacity = 0.9
cLD250MBDisplay.ScalarOpacityUnitDistance = 0.6954587397345667

# show data from cLD200MB
cLD200MBDisplay = Show(cLD200MB, renderView1)
# trace defaults for the display properties.
cLD200MBDisplay.ColorArrayName = ['POINTS', 'SCLIWC_1000mb']
cLD200MBDisplay.LookupTable = sCLIWC1000mbLUT
cLD200MBDisplay.ScalarOpacityUnitDistance = 0.31929559683064723

# show data from cLD300MB
cLD300MBDisplay = Show(cLD300MB, renderView1)
# trace defaults for the display properties.
cLD300MBDisplay.ColorArrayName = ['POINTS', 'SCLIWC_1000mb']
cLD300MBDisplay.LookupTable = sCLIWC1000mbLUT
cLD300MBDisplay.Opacity = 0.8
cLD300MBDisplay.ScalarOpacityUnitDistance = 0.31929559683064723

# show data from cLD400MB
cLD400MBDisplay = Show(cLD400MB, renderView1)
# trace defaults for the display properties.
cLD400MBDisplay.ColorArrayName = ['POINTS', 'SCLIWC_1000mb']
cLD400MBDisplay.LookupTable = sCLIWC1000mbLUT
cLD400MBDisplay.Opacity = 0.7
cLD400MBDisplay.ScalarOpacityUnitDistance = 0.31929559683064723

# show data from cLD450MB
cLD450MBDisplay = Show(cLD450MB, renderView1)
# trace defaults for the display properties.
cLD450MBDisplay.ColorArrayName = ['POINTS', 'SCLIWC_1000mb']
cLD450MBDisplay.LookupTable = sCLIWC1000mbLUT
cLD450MBDisplay.Opacity = 0.6
cLD450MBDisplay.ScalarOpacityUnitDistance = 0.31929559683064723

# show data from cLD500MB
cLD500MBDisplay = Show(cLD500MB, renderView1)
# trace defaults for the display properties.
cLD500MBDisplay.ColorArrayName = ['POINTS', 'SCLIWC_1000mb']
cLD500MBDisplay.LookupTable = sCLIWC1000mbLUT
cLD500MBDisplay.Opacity = 0.5
cLD500MBDisplay.ScalarOpacityUnitDistance = 0.31929559683064723

# show data from cLD600MB
cLD600MBDisplay = Show(cLD600MB, renderView1)
# trace defaults for the display properties.
cLD600MBDisplay.ColorArrayName = ['POINTS', 'SCLIWC_1000mb']
cLD600MBDisplay.LookupTable = sCLIWC1000mbLUT
cLD600MBDisplay.Opacity = 0.4
cLD600MBDisplay.ScalarOpacityUnitDistance = 0.31929559683064723

# show data from cLD700MB
cLD700MBDisplay = Show(cLD700MB, renderView1)
# trace defaults for the display properties.
cLD700MBDisplay.ColorArrayName = ['POINTS', 'SCLIWC_1000mb']
cLD700MBDisplay.LookupTable = sCLIWC1000mbLUT
cLD700MBDisplay.Opacity = 0.3
cLD700MBDisplay.ScalarOpacityUnitDistance = 0.31929559683064723

# show data from cLD350MB
cLD350MBDisplay = Show(cLD350MB, renderView1)
# trace defaults for the display properties.
cLD350MBDisplay.ColorArrayName = ['POINTS', 'SCLIWC_1000mb']
cLD350MBDisplay.LookupTable = sCLIWC1000mbLUT
cLD350MBDisplay.ScalarOpacityUnitDistance = 0.577815741270431
