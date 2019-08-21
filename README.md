## EMAP Visualizer ##

EMAP Visualizer creates bar and pie graphs for reporting purposes from the CSV output of EMAP - A project of Philippine Genome Center's 2018 Internship.

**Input**

It can take the following as input:
* EMAP's cellular component annotations
* EMAP's mollecular function annotations
* EMAP's biological processes annotations
* EMAP's combined cellular component, mollecular function, and biological processes annotations

**Output**

It can output the following graphs:

* Bar graphs of the top 20 annotations with the most number of gene count hits per annotation domain
* Pie graphs of the top 20 annotations with the most number of gene count hits per annotation domain
* A combined bar graph of the top 20 annotations of the three domains

Sample Bar Graph:
![alt text](https://github.com/edmorado/emapvisualizer/raw/master/Cellular_Component_Bar.png)

Sample Pie Graph:
![alt text](https://github.com/edmorado/emapvisualizer/raw/master/Molecular_Function_Pie.png)

Sample Combined Bar Graph:
![alt text](https://github.com/edmorado/emapvisualizer/raw/master/BarAll.png)

**Optional Arguments / Customizations**

'''bash
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
'''
