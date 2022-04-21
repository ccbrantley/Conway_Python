## Conway_Python
My attempt at Conway's Game of Life in Python. The application initializes a n * m array with randomly generated 0s and 1s, where 0 is an inactive cell and 1 is an active cell. It then iteratively applies the following rules to each cell based on the count of its active neighbours:
<ol>
  <li> If the cell has three active neighbours, the cell's state is active.</li>
  <li> If the cell is active and has two active neighbours, the cell's state remains active.</li>
  <li> Otherwise the cell's state is inactive.
</ol>
## Motivation
The motivation behind this project was to utilize Pygame's double buffer.

## Requirements
The requirements are Pygame, numpy, and Python.

## Screenshots

