#! /usr/bin/env python3
"""Advent of Code: Day 12
Author: Benjamin Jung
"""

import numpy as np


class ship():
    """A ship in a storm"""
    def __init__(self, EW=0, NS=0, direction='E', waypoint=[10, 1]):
        # corrd[0] is east(+)/west() and coord[1] is north(+)/south(-)
        self.coord = [EW, NS]
        self.direction = direction
        self.degrees = self.direction_to_degree()
        self.waypoint = np.array(waypoint)

    def direction_to_degree(self):
        """Translate direction to a degree number"""
        directions = {'N': 0,
                      'S': 180,
                      'E': 90,
                      'W': 270,
                      }
        try:
            degree = directions[self.direction]
            return degree
        except:
            print('Invalid direction')

    def degree_to_direction(self):
        """Translate degree value to direction"""
        degree_dict = {0: 'N',
                       90: 'E',
                       180: 'S',
                       270: 'W',
                       }

        deg = self.degrees % 360
        #if self.degrees >= 360:
        #    deg = self.degrees % 360
        #else: 
        #    deg = self.degrees
        try:
            direction = degree_dict[deg]
            return direction
        except:
            print('Invalid degree number')

    def move_ship(self, command):
        """Update the position of the ship"""
        c = command[0]
        amount = int(command[1:])
        
        if c == 'F':
            c = self.direction
        else:
            pass

        if c == 'E':
            self.coord[0] += amount
        elif c == 'W':
            self.coord[0] -= amount
        elif c == 'N':
            self.coord[1] += amount
        elif c == 'S':
            self.coord[1] -= amount
        elif c == 'R':
            self.degrees += amount
            self.direction = self.degree_to_direction()
        elif c == 'L':
            self.degrees -= amount
            self.direction = self.degree_to_direction()
        else:
            print('Invalid Command')

    def move_waypoint(self, command):
        """Update the position of the waypoint and the ship"""
        c = command[0]
        amount = int(command[1:])
        print(c, amount) 
        if c == 'F':
            self.coord[0] += (self.waypoint[0] * amount)
            self.coord[1] += (self.waypoint[1] * amount)
        elif c == 'E':
            self.waypoint[0] += amount
        elif c == 'W':
            self.waypoint[0] -= amount
        elif c == 'N':
            self.waypoint[1] += amount
        elif c == 'S':
            self.waypoint[1] -= amount
        elif c == 'R':
            deg = amount % 360
            way = self.waypoint.copy()
            if amount == 0:
                pass
            elif amount == 90:
                self.waypoint[0] = way[1]
                self.waypoint[1] = way[0] * -1
            elif amount == 180:
                self.waypoint *= -1
            elif amount == 270:
                self.waypoint[0] = way[1] * -1
                self.waypoint[1] = way[0]
            else:
                print('Invalid waypoint shift')
        elif c == 'L':
            deg = amount % 360
            way = self.waypoint.copy()
            if amount == 0:
                pass
            elif amount == 270:
                self.waypoint[0] = way[1]
                self.waypoint[1] = way[0] * -1
            elif amount == 180:
                self.waypoint *= -1
            elif amount == 90:
                self.waypoint[0] = way[1] * -1
                self.waypoint[1] = way[0]
            else:
                print('Invalid waypoint shift')
        else:
            print('Invalid Command')


    def manhattan_coords(self):
        """Calculate the manhattan coordinates"""
        return np.abs(self.coord[0]) + np.abs(self.coord[1])

if __name__ == '__main__':
    instructions = np.genfromtxt('navigation.txt', dtype = str)
    test =np.genfromtxt('test.txt', dtype = str)

    """Part 1"""
    our_ship = ship(0, 0, 'E')
    for inst in instructions:
        our_ship.move_ship(inst)
    print('Part 1:', our_ship.manhattan_coords())

    """Part 2"""
    new_ship = ship()
    for inst in instructions:
        print(new_ship.coord, new_ship.waypoint)
        new_ship.move_waypoint(inst)
    print(new_ship.coord)
    print('Part 2:', new_ship.manhattan_coords())
