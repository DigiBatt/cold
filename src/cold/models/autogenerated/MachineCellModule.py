
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ManufacturingSystemModule import ManufacturingSystem







class MachineCell(ManufacturingSystem):
    """
    Class representing the `MachineCell` entity, which inherits from:
    - ManufacturingSystem

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_4d2ca841_6cb1_4710_a756_5b989746bca2'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MachineCell'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = MachineCell(
    
    class_iri='https://w3id.org/emmo#EMMO_4d2ca841_6cb1_4710_a756_5b989746bca2',
    
    class_name='MachineCell',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_4d2ca841_6cb1_4710_a756_5b989746bca2',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MachineCell',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    