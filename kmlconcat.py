from __future__ import print_function
import argparse
import pprint
import datetime
import re


def _parseArgs():
  parser = argparse.ArgumentParser(description="Take KML Placemarks from "
    "multiple KML files, put all Placemarks into one unified KML file" )

  parser.add_argument("unified_kml_file", help="Output KML file with all KML Placemarks from all KML input files")
  parser.add_argument("input_kml_file", help="KML file(s) to read Placemarks from", nargs="+")

  parsedArgs = parser.parse_args()

  return ( parsedArgs.unified_kml_file, parsedArgs.input_kml_file )


def _readAllInputKmlFiles( inputKmlFiles ):

  unifiedKml = ""

  print( "entered read" )

  foldersCompiled = re.compile( r"<Folder>.*?</Folder>", re.MULTILINE | re.DOTALL)
  editorNameCompiled = re.compile( 
    r"<Folder><name>(.*?)</name>", re.MULTILINE | re.DOTALL )

  folderPolygonsCompiled = re.compile( r"(<Polygon>.*?</Polygon>)", re.MULTILINE | re.DOTALL)

  editorPolygons = {}


  for currFile in inputKmlFiles:
    print( "\n\nFile {0}".format(currFile) )
    with open(currFile, "r") as readHandle:
      fileContents = readHandle.read()
    
    # Find all folders in content
    folderMatches = re.findall( foldersCompiled, fileContents )

    for currFolder in folderMatches:
      editorName = re.search( editorNameCompiled, currFolder ).group(1)

      print( "\n\tEditor name: {0}".format(editorName) )

      polygonMatches = re.findall( folderPolygonsCompiled, currFolder )

      for polygonIndex in range(len(polygonMatches)):
        currPolygon = polygonMatches[polygonIndex]
        print( "\t\tPolygon {0}".format(polygonIndex + 1) )

        editorPolygons[ "{0}---{1:02d}".format(editorName.lower(), polygonIndex + 1)] = {
          "label": "{0} AM Area #{1:02d}".format(editorName, polygonIndex + 1),
          "geometry": currPolygon
        }

  return editorPolygons
    


def _createOutputKml( outputKmlFilename, editorPolygons ):
  editorKmlContent = ""

  for currKey in sorted(editorPolygons.keys()):
    currPolygon = editorPolygons[currKey]
    
    # print( "Polygon: {0}".format(editorPolygons[currKey]["label"]) )
    editorKmlContent += \
      "<Placemark><name>{0}</name>{1}</Placemark>\n".format(
        currPolygon["label"], currPolygon["geometry"])


  outputKml = \
    "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n\n" + \
    "<kml xmlns=\"http://www.opengis.net/kml/2.2\">\n" + \
    "  <Document>\n" + \
    "    <name>Area Managers, {0} UTC</name>\n".format(str(datetime.datetime.utcnow())[:19]) + \
    editorKmlContent + \
    "  </Document>\n" + \
    "</kml>\n"

  with open( outputKmlFilename, "w" ) as outputKmlHandle:
    outputKmlHandle.write(outputKml)


if __name__ == "__main__":
  (outputKmlFile, inputKmlFiles) = _parseArgs()
  editorPolygons = _readAllInputKmlFiles(inputKmlFiles)
  _createOutputKml(outputKmlFile, editorPolygons )
