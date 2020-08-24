
# Problem S3: RoboThieves

## Problem Description

A robot has stolen treasure from a factory and needs to escape without getting caught. The factory
can be modelled by an N by M grid, where the robot can move up, down, left, or right.
Each cell of the grid is either empty, a wall, a camera, a conveyor, or the robot’s initial position.
The robot can only walk on empty cells (denoted by .) or conveyors. The first row, last row, first
column and last column of the grid consists of walls (denoted by W), and there may be walls in
other cells.

Conveyors cause the robot to move in a specific direction, denoted by L, R, U, D for left, right, up,
down respectively. The robot is unable to move on its own while on a conveyor. It is possible that
the robot can become stuck forever on conveyors.

Cameras (denoted by C) can see in all four directions up, down, left, and right, but cannot see
through walls. The robot will be caught if it is in the same cell as a camera or is seen by a camera
while on an empty cell. Conveyors are slightly elevated, so the robot cannot be caught while on a
conveyor, but cameras can see empty cells on the other side of conveyors.

The robot is initially at the cell denoted by S. The exit could be at any of the empty cells. For each
empty cell, determine the minimum number of steps needed for the robot to move there without
being caught, or determine that it is impossible to move there. A step consists of moving once up,
down, left or right. Being moved by a conveyor does not count as a step.
Input Specification

There will be exactly one S character and at least one . character. The first and last character of
every row and column will be W.
For 5 of the 15 marks available, there are no cameras or conveyors.
For an additional 5 of the 15 marks available, there are no conveyors.

## Output Specification
For each empty cell, print one line with one integer, the minimum number of steps for the robot to
move to this empty cell without being caught or −1 if it is impossible to move to this empty cell.
The output should be in row major order; the order of empty cells seen if the input is scanned line
by line top-to-bottom and then left-to-right on each line. See the sample outputs for examples of
row major order output.

*** For sample inputs and outputs, see page 8 of the [following document](https://www.cemc.uwaterloo.ca/contests/computing/2018/stage%201/seniorEF.pdf) (signin may be required)
