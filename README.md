usage: emapVisualizer.py [-h] [-a N] [-g N] [-t NN] [-c code] [-l N] [-b N]
                         inputFile

Creates a bar and/or pie graph for the top X percent of the output of Emap

positional arguments:
  inputFile             Input, output of Emap (which has a file extension of csv but actually is a tsv)

optional arguments:
  -h, --help            show this help message and exit
  -a N, --annot N       Only output the corresponding annotations:
                        1 == Biological process only
                        2 == Cellular component only
                        3 == Molecular function only
                        4 == Biological process and cellular component
                        5 == Biological process and molecular function
                        6 == Cellular component and molecular function
                        7 == All annotations (Default)
  -g N, --graph N       Only output the corresponding graph:
                        1 == Bar graphs
                        2 == Pie graphs
                        3 == Bar and Pie graphs (Default)
  -t NN, --top NN       Top NN of the annotations will be displayed per domain (Default is 20)
  -c code, --cmap code  Color map code for matplotlib for the prettyness of the graphs
                        I suggest the following:
                        RdYlBu
                        Spectral
                        viridis
                        plasma
                        RdYlGn (Default)
  -l N, --level N       Gene onthology level
  -b N, --barall N      Creates the bar  
