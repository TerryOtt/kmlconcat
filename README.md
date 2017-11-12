# kmlconcat

## Usage

Assuming you have multiple KML files stored as `/tmp/input_kml/*.kml`, with
one editor per folder, such as:

``` XML
...
<Folder><name>GizmoGuy411</name><Placemark><name>#1</name>
<Polygon><outerBoundaryIs><LinearRing><tessellate>1</tessellate><coordinates>145.213165283203,14.3516682266844,0 145.424652099609,14.1200536153139,0 144.746246337891,13.1324357106785,0 144.463348388672,13.3650282856022,0 145.213165283203,14.3516682266844,0 </coordinates></LinearRing></outerBoundaryIs></Polygon></Placemark>
<Placemark><name>#2</name>
<Polygon><outerBoundaryIs><LinearRing><tessellate>1</tessellate><coordinates>-125.5078125,48.4692793171672,0 -122.783203125,49.3930998935057,0 -93.955078125,49.3358615911041,0 -87.890625,48.4692793171672,0 -82.001953125,45.4716882581046,0 -81.9140625,42.3057530030464,0 -79.541015625,43.0166973716967,0 -79.892578125,44.0994206852865,0 -69.2578125,47.8242201493502,0 -67.587890625,47.8242201493502,0 -65.390625,44.0362698095346,0 -79.892578125,30.5386078788546,0 -78.837890625,25.9728606959239,0 -80.419921875,24.1417409805043,0 -82.880859375,24.7817473378158,0 -84.814453125,29.0129443024249,0 -96.85546875,25.1800878089906,0 -100.107421875,26.3672638601294,0 -101.953125,29.243270277107,0 -103.88671875,28.2414888173017,0 -107.314453125,31.0670507727078,0 -117.24609375,31.816896886747,0 -123.662109375,35.4740916077303,0 -126.123046875,41.1248835992912,0 -125.5078125,48.4692793171672,0 </coordinates></LinearRing></outerBoundaryIs></Polygon></Placemark>
<Placemark><name>#3</name>
<Polygon><outerBoundaryIs><LinearRing><tessellate>1</tessellate><coordinates>-85.319824,42.142906,0 -82.089844,42.256848,0 -81.897583,40.742957,0 -85.437927,40.786711,0 -85.319824,42.142906,0 </coordinates></LinearRing></outerBoundaryIs></Polygon></Placemark>
</Folder>

<Folder><name>burgher_2</name><Placemark><name>#1</name>
<Polygon><outerBoundaryIs><LinearRing><tessellate>1</tessellate><coordinates>-81.12883,34.82508,0 -80.5327,34.81719,0 -80.51605,33.73804,0 -81.11755,33.7449,0 -81.12883,34.82508,0 </coordinates></LinearRing></outerBoundaryIs></Polygon></Placemark>
</Folder>

...
```

Run the program as:

``` Shell
python3 generated.kml /tmp/input_kml/*.kml
```

Output will be in the `generated.kml` file. 

The output KML file contains no folders, and each polygon is stored in its own placemark. 

## Legal

`kmlconcat` is copyrighted by Terry D. Ott, released as open-source software 
under the [MIT License](https://en.wikipedia.org/wiki/MIT_License). 

Refer to the
[LICENSE](https://github.com/TerryOtt/kmlconcat/blob/master/LICENSE) 
file for more information.
