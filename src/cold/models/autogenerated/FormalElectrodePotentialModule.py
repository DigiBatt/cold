
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .EquilibriumElectrodePotentialModule import EquilibriumElectrodePotential







class FormalElectrodePotential(EquilibriumElectrodePotential):
    """
    Class representing the `FormalElectrodePotential` entity, which inherits from:
    - EquilibriumElectrodePotential

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_b21de1ef_6c15_4d63_b320_c9b96fbf186f'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'FormalElectrodePotential'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = FormalElectrodePotential(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_b21de1ef_6c15_4d63_b320_c9b96fbf186f',
    
    class_name='FormalElectrodePotential',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_b21de1ef_6c15_4d63_b320_c9b96fbf186f',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'FormalElectrodePotential',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    