
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .BatteryContinuumModelModule import BatteryContinuumModel







class P4DModel(BatteryContinuumModel):
    """
    Class representing the `P4DModel` entity, which inherits from:
    - BatteryContinuumModel

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/battery#battery_ef791f05_41d4_4bdb_a1fc_fd455ed0ecb2'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'P4DModel'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = P4DModel(
    
    class_iri='https://w3id.org/emmo/domain/battery#battery_ef791f05_41d4_4bdb_a1fc_fd455ed0ecb2',
    
    class_name='P4DModel',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/battery#battery_ef791f05_41d4_4bdb_a1fc_fd455ed0ecb2',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'P4DModel',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    