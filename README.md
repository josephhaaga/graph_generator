# Graph Generator

A very basic CLI to generate CSV's of undirected graphs.
For use in Genetic Algorithms project, particularly evaluating genetic algorithm performance on k-colorable graph problems.

Maybe i'll add undirected graphs and weighted edges when school winds down for the semester.


## Dependencies

Pandas and NumPy are required. You may be able to `pypi install pandas`, but I would recommend installing Continuum.io's Anaconda distribution

## Usage

`python graph_generator.py NUMBER_OF_NODES TARGET_FILE_NAME`

in other words

`python graph_generator.py 10 targetFile.csv` will yeild

![sample output from command line](sample_output.png)

and a csv file with your designated name will be generated inside the working directory.

![output file ](screen.png)

Joseph Haaga
April 22 2016
