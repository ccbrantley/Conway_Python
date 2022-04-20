'''
BSD 3-Clause License

Copyright (c) 2022, ccbrantley
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its
   contributors may be used to endorse or promote products derived from
   this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
'''

import pygame
import random
import numpy

class Grid:

    rows = 0
    cols = 0
    grid = numpy.zeros((0, 0))

    def __init__(_self, _rows, _cols):
        _self.rows = _rows
        _self.cols = _cols
        _self.grid = numpy.zeros((_self.rows, _self.cols))

    # Getters.

    def getRows(_self):
        return _self.rows

    def getCols(_self):
        return _self.cols

    def getGrid(_self):
        return _self.grid
    # Setters.

    # Methods.

class GridOfLife(Grid):

    seed = 1
    activeNeighbours = numpy.zeros((0, 0))

    def __init__(_self, _rows, _cols, _seed):
        super().__init__(_rows, _cols)
        _self.seed = _seed
        _self.generateActiveCells()
        _self.initializeActiveNeighbours();

    # Getters.

    # Setters.

    # Methods.

    def generateActiveCells(_self):
        for x in range(_self.grid.shape[0]):
            for y in range(_self.grid.shape[1]):
                if (not numpy.random.randint(0, _self.seed + 1)):
                    _self.grid[x][y] = 1

    def initializeActiveNeighbours(_self):
        _self.activeNeighbours = numpy.zeros((_self.rows, _self.cols))

    def countActiveNeighbours(_self):

        # Count topleft active neighbours.

        _self.activeNeighbours[0][0] += _self.grid[0][1]
        _self.activeNeighbours[0][0] += _self.grid[1][1]
        _self.activeNeighbours[0][0] += _self.grid[1][0]

        # Count topright active neighbours.

        _self.activeNeighbours[0][_self.cols - 1] += _self.grid[1][_self.cols - 1]
        _self.activeNeighbours[0][_self.cols - 1] += _self.grid[1][_self.cols - 2]
        _self.activeNeighbours[0][_self.cols - 1] += _self.grid[0][_self.cols - 2]

        # Count bottomright active neighbours.

        _self.activeNeighbours[_self.rows - 1][_self.cols - 1] = _self.grid[_self.rows - 2][_self.cols - 1]
        _self.activeNeighbours[_self.rows - 1][_self.cols - 1] = _self.grid[_self.rows - 1][_self.cols - 2]
        _self.activeNeighbours[_self.rows - 1][_self.cols - 1] = _self.grid[_self.rows - 2][_self.cols - 2]

        # Count bottomleft active neighbours.

        _self.activeNeighbours[_self.rows - 1][0] = _self.grid[_self.rows - 2][0]
        _self.activeNeighbours[_self.rows - 1][0] = _self.grid[_self.rows - 2][1]
        _self.activeNeighbours[_self.rows - 1][0] = _self.grid[_self.rows - 1][1]

        # Count leftmost middle active neighbours.

        for row in range(1, _self.rows - 1):
            _self.activeNeighbours[row][0] += _self.grid[row - 1][0]
            _self.activeNeighbours[row][0] += _self.grid[row - 1][1]
            _self.activeNeighbours[row][0] += _self.grid[row][1]
            _self.activeNeighbours[row][0] += _self.grid[row + 1][1]
            _self.activeNeighbours[row][0] += _self.grid[row + 1][0]

        # Count rightmost middle active neighbours.

        for row  in range(1, _self.rows - 1):
            _self.activeNeighbours[row][_self.cols - 1] += _self.grid[row - 1][_self.cols - 1]
            _self.activeNeighbours[row][_self.cols - 1] += _self.grid[row + 1][_self.cols - 1]
            _self.activeNeighbours[row][_self.cols - 1] += _self.grid[row + 1][_self.cols - 2]
            _self.activeNeighbours[row][_self.cols - 1] += _self.grid[row][_self.cols - 2]
            _self.activeNeighbours[row][_self.cols - 1] += _self.grid[row - 1][_self.cols - 2]

        # Count topmost middle active neighbours.

        for col in range(1, _self.cols - 1):
            _self.activeNeighbours[0][col] += _self.grid[0][col + 1]
            _self.activeNeighbours[0][col] += _self.grid[1][col + 1]
            _self.activeNeighbours[0][col] += _self.grid[1][col]
            _self.activeNeighbours[0][col] += _self.grid[1][col - 1]
            _self.activeNeighbours[0][col] += _self.grid[0][col - 1]

        # Count bottommost middle active neighbours.

        for col in range(1, _self.cols - 1):
            _self.activeNeighbours[_self.rows - 1][col] += _self.grid[_self.rows - 2][col]
            _self.activeNeighbours[_self.rows - 1][col] += _self.grid[_self.rows - 2][col + 1]
            _self.activeNeighbours[_self.rows - 1][col] += _self.grid[_self.rows - 1][col + 1]
            _self.activeNeighbours[_self.rows - 1][col] += _self.grid[_self.rows - 1][col - 1]
            _self.activeNeighbours[_self.rows - 1][col] += _self.grid[_self.rows - 2][col - 1]

        # Count middlemost active neighbours.
        for row in range (1, _self.rows - 1):
            for col in range(1, _self.cols - 1):
                _self.activeNeighbours[row][col] += _self.grid[row - 1][col]
                _self.activeNeighbours[row][col] += _self.grid[row - 1][col + 1]
                _self.activeNeighbours[row][col] += _self.grid[row][col + 1]
                _self.activeNeighbours[row][col] += _self.grid[row + 1][col + 1]
                _self.activeNeighbours[row][col] += _self.grid[row + 1][col]
                _self.activeNeighbours[row][col] += _self.grid[row + 1][col - 1]
                _self.activeNeighbours[row][col] += _self.grid[row][col - 1]
                _self.activeNeighbours[row][col] += _self.grid[row - 1][col - 1]

    def applyRules(_self):
        for row in range(_self.getRows()):
            for col in range(_self.getCols()):
                if (_self.activeNeighbours[row][col] == 3):
                    _self.getGrid()[row][col] = 1
                elif ((_self.activeNeighbours[row][col] == 2) and
                         (_self.getGrid()[row][col])):
                    _self.getGrid()[row][col] = 1
                else:
                    _self.getGrid()[row][col] = 0

    def nextGeneration(_self):
        _self.countActiveNeighbours()
        _self.applyRules()
        _self.initializeActiveNeighbours()

def main():
    grid = GridOfLife(80, 80, 1)
    pygame.init()
    width = 800
    height = 800
    width = width - (width % grid.getRows())
    height = height - (height % grid.getCols())
    screenSize = (width, height)
    screen = pygame.display.set_mode(screenSize)
    colorWhite = (255, 255, 255)
    colorBlack = (0, 0, 0)
    clock = pygame.time.Clock()
    while True:
        screen.fill(colorWhite)
        for row in range(grid.getRows()):
            for col in range(grid.getCols()):
                if (grid.getGrid()[row][col]):
                    rect = pygame.Rect(
                        row * (width / grid.getRows()),
                        col * (height / grid.getCols()),
                        width / grid.getRows(),
                        height / grid.getCols(),
                        )
                    pygame.draw.rect(
                        screen,
                        colorBlack,
                        rect,
                        )
        pygame.display.flip()
        grid.nextGeneration()
        clock.tick(15)
main()
