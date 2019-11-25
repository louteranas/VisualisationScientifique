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
    <href>./out""" + str(i) + """.png</href>
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


#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [1096, 772]
renderView1.InteractionMode = '2D'
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.CenterOfRotation = [1.999999999990905, 45.5, 0.0]
renderView1.StereoType = 0
renderView1.CameraPosition = [1.999999999990905, 45.5, 10000.0]
renderView1.CameraFocalPoint = [1.999999999990905, 45.5, 0.0]
renderView1.CameraParallelScale = 7.055924125668108
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
calculator1.ResultArrayName = 'WindSpeed'
calculator1.Function = 'UGRD_10maboveground*iHat+VGRD_10maboveground*jHat'

# create a new 'Stream Tracer'
streamTracer2 = StreamTracer(Input=calculator1,
    SeedType='High Resolution Line Source')
streamTracer2.Vectors = ['POINTS', 'WindSpeed']
streamTracer2.MaximumStreamlineLength = 19.99999999998181

# init the 'High Resolution Line Source' selected for 'SeedType'
streamTracer2.SeedType.Point1 = [2.571446923301356, 38.776131546267436, 0.0]
streamTracer2.SeedType.Point2 = [10.55478953451784, 38.73523744273476, 9.094947017729282e-13]
streamTracer2.SeedType.Resolution = 10

# create a new 'Stream Tracer'
streamTracer3 = StreamTracer(Input=calculator1,
    SeedType='High Resolution Line Source')
streamTracer3.Vectors = ['POINTS', 'WindSpeed']
streamTracer3.MaximumStreamlineLength = 19.99999999998181

# init the 'High Resolution Line Source' selected for 'SeedType'
streamTracer3.SeedType.Point1 = [7.0676572603004235, 46.430394381872674, 1.3216094885137863e-12]
streamTracer3.SeedType.Point2 = [11.99999999998181, 53.0, 0.0]
streamTracer3.SeedType.Resolution = 20

# create a new 'Stream Tracer'
streamTracer1 = StreamTracer(Input=calculator1,
    SeedType='High Resolution Line Source')
streamTracer1.Vectors = ['POINTS', 'WindSpeed']
streamTracer1.MaximumStreamlineLength = 19.99999999998181

# init the 'High Resolution Line Source' selected for 'SeedType'
streamTracer1.SeedType.Point1 = [-7.411210551107297, 45.57397336530166, 6.821210263296962e-13]
streamTracer1.SeedType.Point2 = [-5.958078191246562, 50.40397379351833, 5.968558980384842e-13]
streamTracer1.SeedType.Resolution = 10

# create a new 'Extract Subset'
extractSubset1 = ExtractSubset(Input=calculator1)
extractSubset1.VOI = [0, 800, 0, 600, 0, 0]
extractSubset1.SampleRateI = 30
extractSubset1.SampleRateJ = 30

# create a new 'Glyph'
glyph1 = Glyph(Input=extractSubset1,
    GlyphType='2D Glyph')
glyph1.Scalars = ['POINTS', 'DSWRF_surface']
glyph1.Vectors = ['POINTS', 'WindSpeed']
glyph1.ScaleFactor = 0.3599999999996726
glyph1.GlyphTransform = 'Transform2'

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

# show data from calculator1
calculator1Display = Show(calculator1, renderView1)
# trace defaults for the display properties.
calculator1Display.Representation = 'Slice'
calculator1Display.ColorArrayName = ['POINTS', 'TMP_2maboveground']
calculator1Display.LookupTable = tMP2mabovegroundLUT
calculator1Display.ScalarOpacityUnitDistance = 0.3192955968304613

# show color legend
calculator1Display.SetScalarBarVisibility(renderView1, True)

# show data from glyph1
glyph1Display = Show(glyph1, renderView1)
# trace defaults for the display properties.
glyph1Display.ColorArrayName = ['POINTS', '']
glyph1Display.DiffuseColor = [1.0, 1.0, 0.4980392156862745]

# show data from streamTracer1
streamTracer1Display = Show(streamTracer1, renderView1)
# trace defaults for the display properties.
streamTracer1Display.ColorArrayName = ['POINTS', '']

# show data from streamTracer2
streamTracer2Display = Show(streamTracer2, renderView1)
# trace defaults for the display properties.
streamTracer2Display.ColorArrayName = ['POINTS', '']

# show data from streamTracer3
streamTracer3Display = Show(streamTracer3, renderView1)
# trace defaults for the display properties.
streamTracer3Display.ColorArrayName = ['POINTS', '']

# setup the color legend parameters for each legend in this view

# get color legend/bar for tMP2mabovegroundLUT in view renderView1
tMP2mabovegroundLUTColorBar = GetScalarBar(tMP2mabovegroundLUT, renderView1)
tMP2mabovegroundLUTColorBar.Position = [0.8619786096256684, 0.0629701686121919]
tMP2mabovegroundLUTColorBar.Position2 = [0.11999999999999988, 0.42999999999999994]
tMP2mabovegroundLUTColorBar.Title = 'TMP_2maboveground'
tMP2mabovegroundLUTColorBar.ComponentTitle = ''


# hello commence ici

tempsAnimation = dataSP1nc.TimestepValues

mon_fichier = open("file.kml", "w")
mon_fichier.close()
mon_fichier = open("file.kml", "a")
writeentete(mon_fichier)
for i, t in enumerate(tempsAnimation):
    renderView1.ViewTime = t
    dt_object = datetime.fromtimestamp(int(t))
    SaveScreenshot("out" + str(i) + ".png")
    writeoverlay(mon_fichier, dt_object, i)
writefooter(mon_fichier)

mon_fichier.close()
