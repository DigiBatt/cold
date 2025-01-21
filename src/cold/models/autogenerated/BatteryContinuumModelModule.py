
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ContinuumModelModule import ContinuumModel







class BatteryContinuumModel(ContinuumModel):
    """
    Class representing the `BatteryContinuumModel` entity, which inherits from:
    - ContinuumModel

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/battery#battery_b1921f7b_afac_465a_a275_26f929f7f936'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'BatteryContinuumModel'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = BatteryContinuumModel(
    
    class_iri='https://w3id.org/emmo/domain/battery#battery_b1921f7b_afac_465a_a275_26f929f7f936',
    
    class_name='BatteryContinuumModel',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/battery#battery_b1921f7b_afac_465a_a275_26f929f7f936',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'BatteryContinuumModel',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    