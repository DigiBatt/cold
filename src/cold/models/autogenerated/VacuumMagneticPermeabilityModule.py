
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .PermeabilityModule import Permeability



from .MeasuredConstantModule import MeasuredConstant







class VacuumMagneticPermeability(Permeability, MeasuredConstant):
    """
    Class representing the `VacuumMagneticPermeability` entity, which inherits from:
    - Permeability, MeasuredConstant

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_de021e4f_918f_47ef_a67b_11120f56b9d7'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'VacuumMagneticPermeability'`
        - **Alias**: `class_name`
    
    - `qudtReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `qudtReference`
    
    - `ISO80000Reference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `ISO80000Reference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = VacuumMagneticPermeability(
    
    class_iri='https://w3id.org/emmo#EMMO_de021e4f_918f_47ef_a67b_11120f56b9d7',
    
    class_name='VacuumMagneticPermeability',
    
    qudtReference="example_value",
    
    ISO80000Reference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_de021e4f_918f_47ef_a67b_11120f56b9d7',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'VacuumMagneticPermeability',
        alias="class_name"
    )
    
    qudtReference: Optional[str] = Field(
        None,
        alias="qudtReference"
    )
    
    ISO80000Reference: Optional[str] = Field(
        None,
        alias="ISO80000Reference"
    )
    

    
    

    

    