"""branchpro is a Branching Processes modelling library.
It contains functionality for modelling, simulating, and visualising the
number of cases of infections by day during an outbreak of the influenza virus.
"""

# Import version info
from .version_info import VERSION_INT, VERSION  # noqa

# Import main classes
from .models import ForwardModel, BranchProModel    # noqa
from .simulation import SimulationController    # noqa
from .visualisation import Visualisation     # noqa