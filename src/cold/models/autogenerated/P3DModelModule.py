
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .BatteryContinuumModelModule import BatteryContinuumModel







class P3DModel(BatteryContinuumModel):
    """
    Class representing the `P3DModel` entity, which inherits from:
    - BatteryContinuumModel

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/battery#battery_0e9e80a1_1fb6_45d9_a1dd_d18ebfc48ae2'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'P3DModel'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = P3DModel(
    
    class_iri='https://w3id.org/emmo/domain/battery#battery_0e9e80a1_1fb6_45d9_a1dd_d18ebfc48ae2',
    
    class_name='P3DModel',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/battery#battery_0e9e80a1_1fb6_45d9_a1dd_d18ebfc48ae2',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'P3DModel',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    