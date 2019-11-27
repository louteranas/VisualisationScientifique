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

# get the material library
materialLibrary1 = GetMaterialLibrary()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [1550, 1166]
renderView1.InteractionMode = '2D'
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.CenterOfRotation = [2.0, 45.5, 0.0]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [2.1072948488550365, 45.483791927357395, 48.29629131445342]
renderView1.CameraFocalPoint = [2.1072948488550365, 45.483791927357395, 0.0]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 7.474011374955047
renderView1.Background = [0.32, 0.34, 0.43]
renderView1.BackEnd = 'OSPRay raycaster'
renderView1.OSPRayMaterialLibrary = materialLibrary1

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
dataIP2nc = NetCDFReader(FileName=['/home/ananas/Documents/ProjetImag/3A/VisualisationScientifique/Projet/Demo/dataIP2.nc'])
dataIP2nc.Dimensions = '(latitude, longitude)'
dataIP2nc.SphericalCoordinates = 0
dataIP2nc.ReplaceFillValueWithNan = 1

# create a new 'Threshold'
cLD250MB = Threshold(Input=dataIP2nc)
cLD250MB.Scalars = ['POINTS', 'TCDC_250mb']
cLD250MB.ThresholdRange = [0.59, 1.0]

# create a new 'Threshold'
cLD400MB = Threshold(Input=dataIP2nc)
cLD400MB.Scalars = ['POINTS', 'TCDC_400mb']
cLD400MB.ThresholdRange = [0.61, 1.0]

# create a new 'Threshold'
cLD450MB = Threshold(Input=dataIP2nc)
cLD450MB.Scalars = ['POINTS', 'TCDC_450mb']
cLD450MB.ThresholdRange = [0.59, 1.0]

# create a new 'Threshold'
cLD500MB = Threshold(Input=dataIP2nc)
cLD500MB.Scalars = ['POINTS', 'TCDC_500mb']
cLD500MB.ThresholdRange = [0.59, 1.0]

# create a new 'Threshold'
cLD550MB = Threshold(Input=dataIP2nc)
cLD550MB.Scalars = ['POINTS', 'TCDC_550mb']
cLD550MB.ThresholdRange = [0.62, 1.0]

# create a new 'Threshold'
cLD200MB = Threshold(Input=dataIP2nc)
cLD200MB.Scalars = ['POINTS', 'TCDC_200mb']
cLD200MB.ThresholdRange = [0.51, 1.0]

# create a new 'Threshold'
cLD300MB = Threshold(Input=dataIP2nc)
cLD300MB.Scalars = ['POINTS', 'TCDC_300mb']
cLD300MB.ThresholdRange = [0.58, 1.0]

# create a new 'Threshold'
cLD600MB = Threshold(Input=dataIP2nc)
cLD600MB.Scalars = ['POINTS', 'TCDC_600mb']
cLD600MB.ThresholdRange = [0.63, 1.0]

# create a new 'Threshold'
cLD350MB = Threshold(Input=dataIP2nc)
cLD350MB.Scalars = ['POINTS', 'TCDC_350mb']
cLD350MB.ThresholdRange = [0.6, 1.0]

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from cLD200MB
cLD200MBDisplay = Show(cLD200MB, renderView1)

# get color transfer function/color map for 'TCDC_200mb'
tCDC_200mbLUT = GetColorTransferFunction('TCDC_200mb')
tCDC_200mbLUT.AnnotationsInitialized = 1
tCDC_200mbLUT.RGBPoints = [0.0, 0.8627450980392157, 0.8627450980392157, 0.8627450980392157, 1.0, 1.0, 1.0, 1.0]
tCDC_200mbLUT.ColorSpace = 'RGB'
tCDC_200mbLUT.NanColor = [1.0, 0.0, 0.0]
tCDC_200mbLUT.ScalarRangeInitialized = 1.0
tCDC_200mbLUT.Annotations = ['0.53125', '0.53125', '0.5625', '0.5625', '0.59375', '0.59375', '0.625', '0.625', '0.65625', '0.65625', '0.6875', '0.6875', '0.71875', '0.71875', '0.75', '0.75', '0.78125', '0.78125', '0.8125', '0.8125', '0.84375', '0.84375', '0.875', '0.875', '0.90625', '0.90625', '0.9375', '0.9375', '0.96875', '0.96875', '1', '1']
tCDC_200mbLUT.IndexedColors = [1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.6299992370489051, 0.6299992370489051, 1.0, 0.6699931334401464, 0.5000076295109483, 0.3300068665598535, 1.0, 0.5000076295109483, 0.7499961852445258, 0.5300068665598535, 0.3499961852445258, 0.7000076295109483, 1.0, 0.7499961852445258, 0.5000076295109483, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0]
tCDC_200mbLUT.IndexedOpacities = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]

# get opacity transfer function/opacity map for 'TCDC_200mb'
tCDC_200mbPWF = GetOpacityTransferFunction('TCDC_200mb')
tCDC_200mbPWF.Points = [0.0, 0.0, 0.5, 0.0, 0.17469878494739532, 0.16911764442920685, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
tCDC_200mbPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
cLD200MBDisplay.Representation = 'Surface'
cLD200MBDisplay.ColorArrayName = ['POINTS', 'TCDC_200mb']
cLD200MBDisplay.LookupTable = tCDC_200mbLUT
cLD200MBDisplay.OSPRayScaleArray = 'SCLIWC_1000mb'
cLD200MBDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
cLD200MBDisplay.SelectOrientationVectors = 'None'
cLD200MBDisplay.ScaleFactor = 1.475
cLD200MBDisplay.SelectScaleArray = 'None'
cLD200MBDisplay.GlyphType = 'Arrow'
cLD200MBDisplay.GlyphTableIndexArray = 'None'
cLD200MBDisplay.GaussianRadius = 0.07375
cLD200MBDisplay.SetScaleArray = ['POINTS', 'SCLIWC_1000mb']
cLD200MBDisplay.ScaleTransferFunction = 'PiecewiseFunction'
cLD200MBDisplay.OpacityArray = ['POINTS', 'SCLIWC_1000mb']
cLD200MBDisplay.OpacityTransferFunction = 'PiecewiseFunction'
cLD200MBDisplay.DataAxesGrid = 'GridAxesRepresentation'
cLD200MBDisplay.PolarAxes = 'PolarAxesRepresentation'
cLD200MBDisplay.ScalarOpacityFunction = tCDC_200mbPWF
cLD200MBDisplay.ScalarOpacityUnitDistance = 1.5589959643603553

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
cLD200MBDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
cLD200MBDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# show data from cLD250MB
cLD250MBDisplay = Show(cLD250MB, renderView1)

# trace defaults for the display properties.
cLD250MBDisplay.Representation = 'Surface'
cLD250MBDisplay.ColorArrayName = ['POINTS', 'TCDC_200mb']
cLD250MBDisplay.LookupTable = tCDC_200mbLUT
cLD250MBDisplay.Opacity = 0.9
cLD250MBDisplay.OSPRayScaleArray = 'SCLIWC_1000mb'
cLD250MBDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
cLD250MBDisplay.SelectOrientationVectors = 'None'
cLD250MBDisplay.ScaleFactor = 2.0
cLD250MBDisplay.SelectScaleArray = 'None'
cLD250MBDisplay.GlyphType = 'Arrow'
cLD250MBDisplay.GlyphTableIndexArray = 'None'
cLD250MBDisplay.GaussianRadius = 0.1
cLD250MBDisplay.SetScaleArray = ['POINTS', 'SCLIWC_1000mb']
cLD250MBDisplay.ScaleTransferFunction = 'PiecewiseFunction'
cLD250MBDisplay.OpacityArray = ['POINTS', 'SCLIWC_1000mb']
cLD250MBDisplay.OpacityTransferFunction = 'PiecewiseFunction'
cLD250MBDisplay.DataAxesGrid = 'GridAxesRepresentation'
cLD250MBDisplay.PolarAxes = 'PolarAxesRepresentation'
cLD250MBDisplay.ScalarOpacityFunction = tCDC_200mbPWF
cLD250MBDisplay.ScalarOpacityUnitDistance = 0.31929559683064707

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
cLD250MBDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 0.0007276535034179688, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
cLD250MBDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 0.0007276535034179688, 1.0, 0.5, 0.0]

# show data from cLD300MB
cLD300MBDisplay = Show(cLD300MB, renderView1)

# trace defaults for the display properties.
cLD300MBDisplay.Representation = 'Surface'
cLD300MBDisplay.ColorArrayName = ['POINTS', 'TCDC_200mb']
cLD300MBDisplay.LookupTable = tCDC_200mbLUT
cLD300MBDisplay.Opacity = 0.8
cLD300MBDisplay.OSPRayScaleArray = 'SCLIWC_1000mb'
cLD300MBDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
cLD300MBDisplay.SelectOrientationVectors = 'None'
cLD300MBDisplay.ScaleFactor = 2.0
cLD300MBDisplay.SelectScaleArray = 'None'
cLD300MBDisplay.GlyphType = 'Arrow'
cLD300MBDisplay.GlyphTableIndexArray = 'None'
cLD300MBDisplay.GaussianRadius = 0.1
cLD300MBDisplay.SetScaleArray = ['POINTS', 'SCLIWC_1000mb']
cLD300MBDisplay.ScaleTransferFunction = 'PiecewiseFunction'
cLD300MBDisplay.OpacityArray = ['POINTS', 'SCLIWC_1000mb']
cLD300MBDisplay.OpacityTransferFunction = 'PiecewiseFunction'
cLD300MBDisplay.DataAxesGrid = 'GridAxesRepresentation'
cLD300MBDisplay.PolarAxes = 'PolarAxesRepresentation'
cLD300MBDisplay.ScalarOpacityFunction = tCDC_200mbPWF
cLD300MBDisplay.ScalarOpacityUnitDistance = 0.7823018678554056

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
cLD300MBDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 0.00041900575160980225, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
cLD300MBDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 0.00041900575160980225, 1.0, 0.5, 0.0]

# show data from cLD450MB
cLD450MBDisplay = Show(cLD450MB, renderView1)

# trace defaults for the display properties.
cLD450MBDisplay.Representation = 'Surface'
cLD450MBDisplay.ColorArrayName = ['POINTS', 'TCDC_200mb']
cLD450MBDisplay.LookupTable = tCDC_200mbLUT
cLD450MBDisplay.Opacity = 0.5
cLD450MBDisplay.OSPRayScaleArray = 'SCLIWC_1000mb'
cLD450MBDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
cLD450MBDisplay.SelectOrientationVectors = 'None'
cLD450MBDisplay.ScaleFactor = 2.0
cLD450MBDisplay.SelectScaleArray = 'None'
cLD450MBDisplay.GlyphType = 'Arrow'
cLD450MBDisplay.GlyphTableIndexArray = 'None'
cLD450MBDisplay.GaussianRadius = 0.1
cLD450MBDisplay.SetScaleArray = ['POINTS', 'SCLIWC_1000mb']
cLD450MBDisplay.ScaleTransferFunction = 'PiecewiseFunction'
cLD450MBDisplay.OpacityArray = ['POINTS', 'SCLIWC_1000mb']
cLD450MBDisplay.OpacityTransferFunction = 'PiecewiseFunction'
cLD450MBDisplay.DataAxesGrid = 'GridAxesRepresentation'
cLD450MBDisplay.PolarAxes = 'PolarAxesRepresentation'
cLD450MBDisplay.ScalarOpacityFunction = tCDC_200mbPWF
cLD450MBDisplay.ScalarOpacityUnitDistance = 0.31929559683064707

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
cLD450MBDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 0.0006726980209350586, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
cLD450MBDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 0.0006726980209350586, 1.0, 0.5, 0.0]

# show data from cLD600MB
cLD600MBDisplay = Show(cLD600MB, renderView1)

# trace defaults for the display properties.
cLD600MBDisplay.Representation = 'Surface'
cLD600MBDisplay.ColorArrayName = ['POINTS', 'TCDC_200mb']
cLD600MBDisplay.LookupTable = tCDC_200mbLUT
cLD600MBDisplay.Opacity = 0.2
cLD600MBDisplay.OSPRayScaleArray = 'SCLIWC_1000mb'
cLD600MBDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
cLD600MBDisplay.SelectOrientationVectors = 'None'
cLD600MBDisplay.ScaleFactor = 2.0
cLD600MBDisplay.SelectScaleArray = 'None'
cLD600MBDisplay.GlyphType = 'Arrow'
cLD600MBDisplay.GlyphTableIndexArray = 'None'
cLD600MBDisplay.GaussianRadius = 0.1
cLD600MBDisplay.SetScaleArray = ['POINTS', 'SCLIWC_1000mb']
cLD600MBDisplay.ScaleTransferFunction = 'PiecewiseFunction'
cLD600MBDisplay.OpacityArray = ['POINTS', 'SCLIWC_1000mb']
cLD600MBDisplay.OpacityTransferFunction = 'PiecewiseFunction'
cLD600MBDisplay.DataAxesGrid = 'GridAxesRepresentation'
cLD600MBDisplay.PolarAxes = 'PolarAxesRepresentation'
cLD600MBDisplay.ScalarOpacityFunction = tCDC_200mbPWF
cLD600MBDisplay.ScalarOpacityUnitDistance = 0.31929559683064707

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
cLD600MBDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 0.0006726980209350586, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
cLD600MBDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 0.0006726980209350586, 1.0, 0.5, 0.0]

# show data from cLD350MB
cLD350MBDisplay = Show(cLD350MB, renderView1)

# trace defaults for the display properties.
cLD350MBDisplay.Representation = 'Surface'
cLD350MBDisplay.ColorArrayName = ['POINTS', 'TCDC_200mb']
cLD350MBDisplay.LookupTable = tCDC_200mbLUT
cLD350MBDisplay.Opacity = 0.7
cLD350MBDisplay.OSPRayScaleArray = 'SCLIWC_1000mb'
cLD350MBDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
cLD350MBDisplay.SelectOrientationVectors = 'None'
cLD350MBDisplay.ScaleFactor = 2.0
cLD350MBDisplay.SelectScaleArray = 'None'
cLD350MBDisplay.GlyphType = 'Arrow'
cLD350MBDisplay.GlyphTableIndexArray = 'None'
cLD350MBDisplay.GaussianRadius = 0.1
cLD350MBDisplay.SetScaleArray = ['POINTS', 'SCLIWC_1000mb']
cLD350MBDisplay.ScaleTransferFunction = 'PiecewiseFunction'
cLD350MBDisplay.OpacityArray = ['POINTS', 'SCLIWC_1000mb']
cLD350MBDisplay.OpacityTransferFunction = 'PiecewiseFunction'
cLD350MBDisplay.DataAxesGrid = 'GridAxesRepresentation'
cLD350MBDisplay.PolarAxes = 'PolarAxesRepresentation'
cLD350MBDisplay.ScalarOpacityFunction = tCDC_200mbPWF
cLD350MBDisplay.ScalarOpacityUnitDistance = 0.31929559683064707

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
cLD350MBDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 0.0006726980209350586, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
cLD350MBDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 0.0006726980209350586, 1.0, 0.5, 0.0]

# show data from cLD400MB
cLD400MBDisplay = Show(cLD400MB, renderView1)

# trace defaults for the display properties.
cLD400MBDisplay.Representation = 'Surface'
cLD400MBDisplay.ColorArrayName = ['POINTS', 'TCDC_200mb']
cLD400MBDisplay.LookupTable = tCDC_200mbLUT
cLD400MBDisplay.Opacity = 0.6
cLD400MBDisplay.OSPRayScaleArray = 'SCLIWC_1000mb'
cLD400MBDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
cLD400MBDisplay.SelectOrientationVectors = 'None'
cLD400MBDisplay.ScaleFactor = 2.0
cLD400MBDisplay.SelectScaleArray = 'None'
cLD400MBDisplay.GlyphType = 'Arrow'
cLD400MBDisplay.GlyphTableIndexArray = 'None'
cLD400MBDisplay.GaussianRadius = 0.1
cLD400MBDisplay.SetScaleArray = ['POINTS', 'SCLIWC_1000mb']
cLD400MBDisplay.ScaleTransferFunction = 'PiecewiseFunction'
cLD400MBDisplay.OpacityArray = ['POINTS', 'SCLIWC_1000mb']
cLD400MBDisplay.OpacityTransferFunction = 'PiecewiseFunction'
cLD400MBDisplay.DataAxesGrid = 'GridAxesRepresentation'
cLD400MBDisplay.PolarAxes = 'PolarAxesRepresentation'
cLD400MBDisplay.ScalarOpacityFunction = tCDC_200mbPWF
cLD400MBDisplay.ScalarOpacityUnitDistance = 0.31929559683064707

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
cLD400MBDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 0.0006726980209350586, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
cLD400MBDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 0.0006726980209350586, 1.0, 0.5, 0.0]

# show data from cLD500MB
cLD500MBDisplay = Show(cLD500MB, renderView1)

# trace defaults for the display properties.
cLD500MBDisplay.Representation = 'Surface'
cLD500MBDisplay.ColorArrayName = ['POINTS', 'TCDC_200mb']
cLD500MBDisplay.LookupTable = tCDC_200mbLUT
cLD500MBDisplay.Opacity = 0.4
cLD500MBDisplay.OSPRayScaleArray = 'SCLIWC_1000mb'
cLD500MBDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
cLD500MBDisplay.SelectOrientationVectors = 'None'
cLD500MBDisplay.ScaleFactor = 2.0
cLD500MBDisplay.SelectScaleArray = 'None'
cLD500MBDisplay.GlyphType = 'Arrow'
cLD500MBDisplay.GlyphTableIndexArray = 'None'
cLD500MBDisplay.GaussianRadius = 0.1
cLD500MBDisplay.SetScaleArray = ['POINTS', 'SCLIWC_1000mb']
cLD500MBDisplay.ScaleTransferFunction = 'PiecewiseFunction'
cLD500MBDisplay.OpacityArray = ['POINTS', 'SCLIWC_1000mb']
cLD500MBDisplay.OpacityTransferFunction = 'PiecewiseFunction'
cLD500MBDisplay.DataAxesGrid = 'GridAxesRepresentation'
cLD500MBDisplay.PolarAxes = 'PolarAxesRepresentation'
cLD500MBDisplay.ScalarOpacityFunction = tCDC_200mbPWF
cLD500MBDisplay.ScalarOpacityUnitDistance = 0.31929559683064707

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
cLD500MBDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 0.0006726980209350586, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
cLD500MBDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 0.0006726980209350586, 1.0, 0.5, 0.0]

# show data from cLD550MB
cLD550MBDisplay = Show(cLD550MB, renderView1)

# trace defaults for the display properties.
cLD550MBDisplay.Representation = 'Surface'
cLD550MBDisplay.ColorArrayName = ['POINTS', 'TCDC_200mb']
cLD550MBDisplay.LookupTable = tCDC_200mbLUT
cLD550MBDisplay.Opacity = 0.3
cLD550MBDisplay.OSPRayScaleArray = 'SCLIWC_1000mb'
cLD550MBDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
cLD550MBDisplay.SelectOrientationVectors = 'None'
cLD550MBDisplay.ScaleFactor = 2.0
cLD550MBDisplay.SelectScaleArray = 'None'
cLD550MBDisplay.GlyphType = 'Arrow'
cLD550MBDisplay.GlyphTableIndexArray = 'None'
cLD550MBDisplay.GaussianRadius = 0.1
cLD550MBDisplay.SetScaleArray = ['POINTS', 'SCLIWC_1000mb']
cLD550MBDisplay.ScaleTransferFunction = 'PiecewiseFunction'
cLD550MBDisplay.OpacityArray = ['POINTS', 'SCLIWC_1000mb']
cLD550MBDisplay.OpacityTransferFunction = 'PiecewiseFunction'
cLD550MBDisplay.DataAxesGrid = 'GridAxesRepresentation'
cLD550MBDisplay.PolarAxes = 'PolarAxesRepresentation'
cLD550MBDisplay.ScalarOpacityFunction = tCDC_200mbPWF
cLD550MBDisplay.ScalarOpacityUnitDistance = 0.31929559683064707

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
cLD550MBDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 0.0006726980209350586, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
cLD550MBDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 0.0006726980209350586, 1.0, 0.5, 0.0]

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# finally, restore active source
SetActiveSource(cLD200MB)
# ----------------------------------------------------------------