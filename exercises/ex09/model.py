"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
import math
from random import random
import constants
from math import sin, cos, pi
from math import sqrt


__author__ = "7305 54167"  


class Point:
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)

    def distance(self, second_cell: Point) -> int:
        x1: float = self.x 
        x2: float = second_cell.x
        y1: float = self.y 
        y2: float = second_cell.y
        """Takes two points and returns the distance between them."""
        d = math.sqrt(math.pow(x2-x1, 2) + math.pow(y2-y1, 2))
        return d


class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = constants.VULNERABLE

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction

    def tick(self) -> None:
        """Tick method."""
        self.location = self.location.add(self.direction)
        print(self.is_infected())
        if self.is_infected():
            self.sickness += 1
            if self.sickness > constants.RECOVERY_PERIOD:
                self.immunize()
        

    def contract_disease(self) -> None:
        """Assigns the infected constant to sickness."""
        self.sickness = constants.INFECTED
    
    def is_vulnerable(self) -> None:
        """Returns True if a cell is Vulnerable."""
        return self.sickness == constants.VULNERABLE
    
    def is_infected(self) -> None:
        """Returns True is a cell is infected."""
        return self.sickness >= constants.INFECTED
    
    def color(self) -> str:
        """Returns 'Gray' if a cell is Vulnerable."""
        vulnerable = self.is_vulnerable()
        infected = self.is_infected()
        immune = self.is_immune()
        if vulnerable:
            return "Gray"
        if infected:
            return "Red"
        if immune:
            return "Purple"

    def contact_with(self, cell_contact: Cell) -> None:
        """Changes vulnerable cell to infected if it contacts an infected cell."""
        if self.location.distance(cell_contact.location) <= constants.CELL_RADIUS:
            if self.is_infected() and cell_contact.is_vulnerable():
                cell_contact.contract_disease()
            elif cell_contact.is_infected() and self.is_vulnerable():
                self.contract_disease()

    def immunize(self) -> None:
        """Assigns Immune to the sickness attribute."""
        self.sickness = constants.IMMUNE 

    def is_immune(self) -> None:
        """Checks when a cell is Immune."""
        return self.sickness == constants.IMMUNE



class Model:
    """The state of the simulation."""

    population: list[Cell]
    time: int = 0

    def __init__(self, cells: int, speed: float, infected_cells: int, immune_cells: int = 0):
        """Initialize the cells with random locations and directions."""
        self.population = []

        if infected_cells >= cells or infected_cells <= 0:
            print("There must be atleast one cell infected.")
            raise ValueError 

        if immune_cells >= cells or immune_cells <= 0:
            print("There must be atleast one cell immune.")
            raise ValueError 

        for i in range(cells):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            
            if i < infected_cells:
                cell.contract_disease()
            else:
                if i < immune_cells + infected_cells:
                    cell.immunize()
    
            self.population.append(cell)
    
    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population:
            cell.tick()
            self.enforce_bounds(cell)
            print(cell.is_immune())
        Model.check_contacts(self)
        
    def random_location(self) -> Point:
        """Generate a random location."""
        start_x: float = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        start_y: float = random() * constants.BOUNDS_HEIGHT - constants.MAX_Y
        return Point(start_x, start_y)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle: float = 2.0 * pi * random()
        direction_x: float = cos(random_angle) * speed
        direction_y: float = sin(random_angle) * speed
        return Point(direction_x, direction_y)

    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if cell.location.x > constants.MAX_X:
            cell.location.x = constants.MAX_X
            cell.direction.x *= -1.0
        if cell.location.x < constants.MIN_X:
            cell.location.x = constants.MIN_X
            cell.direction.x *= -1.0
        if cell.location.y > constants.MAX_Y:
            cell.location.y = constants.MAX_Y
            cell.direction.y *= -1.0
        if cell.location.y < constants.MIN_Y:
            cell.location.y = constants.MIN_Y
            cell.direction.y *= -1.0

    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        return False

    def check_contacts(self) -> None:
        """Checks the distance between cells and infects them if they come in contact. """
        for i in range(len(self.population)):
            for j in range(i + 1, len(self.population)):
                self.population[i].contact_with(self.population[j])

