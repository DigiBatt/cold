
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MeasuringSystemModule import MeasuringSystem







class BatteryCyclerSystem(MeasuringSystem):
    """
    Class representing the `BatteryCyclerSystem` entity, which inherits from:
    - MeasuringSystem

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/battery#battery_bc033b97_a5b7_455c_94ce_e95676cb816b'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'BatteryCyclerSystem'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = BatteryCyclerSystem(
    
    class_iri='https://w3id.org/emmo/domain/battery#battery_bc033b97_a5b7_455c_94ce_e95676cb816b',
    
    class_name='BatteryCyclerSystem',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/battery#battery_bc033b97_a5b7_455c_94ce_e95676cb816b',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'BatteryCyclerSystem',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    