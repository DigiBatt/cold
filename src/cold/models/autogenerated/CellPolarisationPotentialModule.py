
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CellVoltageModule import CellVoltage







class CellPolarisationPotential(CellVoltage):
    """
    Class representing the `CellPolarisationPotential` entity, which inherits from:
    - CellVoltage

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_265bb4d6_5eec_40f6_a3fa_59b3bd08e9af'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CellPolarisationPotential'`
        - **Alias**: `class_name`
    
    - `IEVReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `IEVReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = CellPolarisationPotential(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_265bb4d6_5eec_40f6_a3fa_59b3bd08e9af',
    
    class_name='CellPolarisationPotential',
    
    IEVReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_265bb4d6_5eec_40f6_a3fa_59b3bd08e9af',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CellPolarisationPotential',
        alias="class_name"
    )
    
    IEVReference: Optional[str] = Field(
        None,
        alias="IEVReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    