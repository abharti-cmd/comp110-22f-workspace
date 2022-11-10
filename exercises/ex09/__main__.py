"""This specially named module makes the package runnable."""

import constants
from model import Model
from view_controller import ViewController


def main() -> None:
    """Entrypoint of simulation."""
    model: Model = Model(constants.CELL_COUNT, constants.CELL_SPEED, constants.NUM_INFECTED_CELLS, constants.NUM_IMMUNE_CELLS)
    view_controller: ViewController = ViewController(model)
    view_controller.start_simulation()



if __name__ == "__main__":
    main()