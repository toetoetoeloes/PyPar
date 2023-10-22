# PyPar
PyPar is a paragraph reformatter.

# Synopsis
    pypar.py [-h] [-i INDENT] [-j] [-m MARGIN] [-w WIDTH] [FILE ...]

# Description
    Reformat paragraphs in FILE(s) and send to standard output.
    
    With no FILE, or when FILE is -, read standard input.

    -h, --help
          display help and exit
          
    -i, --indent
          first line paragraph indentation, default = 10
    
    -j, --justify
          justify text
          
    -m, --margin
          left margin of text, default = 0
          
    -w, --width
          maximum number of characters on a line, default = 75

# Example

If we have a file _test.txt_ with the following text:

```
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Tortor condimentum lacinia quis vel eros donec. Non sodales neque sodales ut etiam. Sem nulla pharetra diam sit amet nisl suscipit. Semper feugiat nibh sed pulvinar proin gravida hendrerit lectus. Aliquam vestibulum morbi blandit cursus risus. Est lorem ipsum dolor sit amet consectetur adipiscing elit. Congue quisque egestas diam in arcu. Vitae elementum curabitur vitae nunc sed velit dignissim sodales ut. Laoreet sit amet cursus sit. Scelerisque eu ultrices vitae auctor eu augue. Amet purus gravida quis blandit turpis cursus. Metus dictum at tempor commodo ullamcorper a lacus. Odio morbi quis commodo odio aenean sed adipiscing diam.

Nulla aliquet enim tortor at. Tellus at urna condimentum mattis pellentesque id nibh tortor. Vitae semper quis lectus nulla at volutpat diam. Varius vel pharetra vel turpis nunc. Id porta nibh venenatis cras sed felis eget velit. Diam phasellus vestibulum lorem sed risus ultricies. Diam phasellus vestibulum lorem sed risus ultricies tristique nulla. Faucibus purus in massa tempor nec feugiat nisl pretium fusce. Felis donec et odio pellentesque diam volutpat commodo. Tellus mauris a diam maecenas sed. In nulla posuere sollicitudin aliquam ultrices sagittis. Cursus eget nunc scelerisque viverra mauris.
```

we can use PyPar to restrict each line to 80 characters using the following command:
```
python PyPar.py --justify --width 80 --margin 10 test.txt >out.txt
```

The contents of _out.txt_ will look like this:

```
                    Lorem  ipsum  dolor  sit  amet,  consectetur  adipiscing elit, sed  do
          eiusmod  tempor  incididunt ut labore et dolore magna aliqua. Tortor condimentum
          lacinia quis vel eros donec. Non  sodales  neque  sodales  ut  etiam.  Sem nulla
          pharetra diam sit amet nisl  suscipit.  Semper  feugiat  nibh sed pulvinar proin
          gravida hendrerit lectus. Aliquam vestibulum  morbi  blandit  cursus  risus. Est
          lorem ipsum dolor sit amet consectetur  adipiscing  elit. Congue quisque egestas
          diam in arcu. Vitae elementum curabitur vitae  nunc  sed velit dignissim sodales
          ut. Laoreet sit amet cursus sit. Scelerisque eu ultrices  vitae auctor eu augue.
          Amet purus  gravida  quis  blandit turpis cursus. Metus dictum at tempor commodo
          ullamcorper a lacus. Odio morbi quis commodo odio aenean sed adipiscing diam. 

                    Nulla  aliquet enim tortor  at.  Tellus  at  urna  condimentum  mattis
          pellentesque id  nibh  tortor.  Vitae semper quis lectus nulla at volutpat diam.
          Varius vel pharetra vel turpis nunc. Id porta nibh venenatis cras sed felis eget
          velit.  Diam phasellus vestibulum lorem  sed  risus  ultricies.  Diam  phasellus
          vestibulum  lorem  sed risus ultricies tristique nulla. Faucibus purus in  massa
          tempor nec feugiat nisl pretium fusce.  Felis  donec  et  odio pellentesque diam
          volutpat  commodo.   Tellus  mauris  a  diam  maecenas  sed.  In  nulla  posuere
          sollicitudin  aliquam  ultrices  sagittis.  Cursus eget nunc scelerisque viverra
          mauris.
```
