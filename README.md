# Converter between Maanmittauslaitos data and Cities: Skylines

![](http://i.imgur.com/64kXLc0.jpg)

Simple tool for converting Maanmittauslaitos data to height map files understood by Cities: Skylines.

First, head to https://tiedostopalvelu.maanmittauslaitos.fi/tp/kartta and download grid cells you want. Map is divided into grids so you might have to download multiple grid cells to get the whole area you want.

Unzip the downloaded grid cells and convert them to 16-bit grayscale images using the converter, for example like this:

```
./convert.py N4324D.asc N4324D.png 3.4
```

Last argument is an optional scale factor which can be used to increase contrast between the lowest and highest points.

If you want to join multiple grid areas together, use your favorite image manipulation tools such as Photoshop, GIMP or ImageMagick.

Finally use these instructions to import height maps into Cities: Skylines map editor: http://www.skylineswiki.com/Map_Editor#Import_Heightmap
