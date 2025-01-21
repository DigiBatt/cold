
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SourceVoltageModule import SourceVoltage



from .OpenCircuitVoltageModule import OpenCircuitVoltage



from .ElectrodePotentialModule import ElectrodePotential







class EquilibriumElectrodePotential(SourceVoltage, OpenCircuitVoltage, ElectrodePotential):
    """
    Class representing the `EquilibriumElectrodePotential` entity, which inherits from:
    - SourceVoltage, OpenCircuitVoltage, ElectrodePotential

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_d91940f0_c8b6_4505_9b68_6bf6cfc5c544'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'EquilibriumElectrodePotential'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `IEVReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `IEVReference`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = EquilibriumElectrodePotential(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_d91940f0_c8b6_4505_9b68_6bf6cfc5c544',
    
    class_name='EquilibriumElectrodePotential',
    
    elucidation="example_value",
    
    IEVReference="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_d91940f0_c8b6_4505_9b68_6bf6cfc5c544',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'EquilibriumElectrodePotential',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    IEVReference: Optional[str] = Field(
        None,
        alias="IEVReference"
    )
    
    wikipediaReference: Optional[str] = Field(
        None,
        alias="wikipediaReference"
    )
    

    
    

    

    