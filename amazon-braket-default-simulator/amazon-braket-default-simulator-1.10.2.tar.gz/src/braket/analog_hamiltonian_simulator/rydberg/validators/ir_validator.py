from braket.ir.ahs.program_v1 import Program

from braket.analog_hamiltonian_simulator.rydberg.validators.atom_arrangement import (
    AtomArrangementValidator,
)
from braket.analog_hamiltonian_simulator.rydberg.validators.capabilities_constants import (
    CapabilitiesConstants,
)
from braket.analog_hamiltonian_simulator.rydberg.validators.driving_field import (
    DrivingFieldValidator,
)
from braket.analog_hamiltonian_simulator.rydberg.validators.hamiltonian import HamiltonianValidator
from braket.analog_hamiltonian_simulator.rydberg.validators.physical_field import (
    PhysicalFieldValidator,
)
from braket.analog_hamiltonian_simulator.rydberg.validators.program import ProgramValidator
from braket.analog_hamiltonian_simulator.rydberg.validators.shifting_field import (
    ShiftingFieldValidator,
)
from braket.analog_hamiltonian_simulator.rydberg.validators.times_series import TimeSeriesValidator


def validate_program(program: Program, device_capabilities: CapabilitiesConstants) -> None:
    """
    Validate the analog Hamiltonian simulation program has only one driving and shifting field,
    and all the sequences have the same last time point.

    Args:
        program (Program): An analog Hamiltonian simulation program
        device_capabilities (CapabilitiesConstants): The capability constants for the simulator
    """

    ProgramValidator(capabilities=device_capabilities, **program.dict())
    AtomArrangementValidator(capabilities=device_capabilities, **program.setup.ahs_register.dict())
    HamiltonianValidator(**program.hamiltonian.dict())
    for d_fields in program.hamiltonian.drivingFields:
        DrivingFieldValidator(capabilities=device_capabilities, **d_fields.dict())
        amplitude = d_fields.amplitude
        phase = d_fields.phase
        detuning = d_fields.detuning
        PhysicalFieldValidator(**amplitude.dict())
        TimeSeriesValidator(capabilities=device_capabilities, **amplitude.time_series.dict())

        PhysicalFieldValidator(**phase.dict())
        TimeSeriesValidator(capabilities=device_capabilities, **phase.time_series.dict())

        PhysicalFieldValidator(**detuning.dict())
        TimeSeriesValidator(capabilities=device_capabilities, **detuning.time_series.dict())
    for s_fields in program.hamiltonian.shiftingFields:
        ShiftingFieldValidator(capabilities=device_capabilities, **s_fields.dict())
        magnitude = s_fields.magnitude
        PhysicalFieldValidator(**magnitude.dict())
        TimeSeriesValidator(capabilities=device_capabilities, **magnitude.time_series.dict())
