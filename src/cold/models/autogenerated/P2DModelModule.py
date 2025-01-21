
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .BatteryContinuumModelModule import BatteryContinuumModel







class P2DModel(BatteryContinuumModel):
    """
    Class representing the `P2DModel` entity, which inherits from:
    - BatteryContinuumModel

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/battery#battery_52ed5408_da62_483d_97d5_a45755022582'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'P2DModel'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = P2DModel(
    
    class_iri='https://w3id.org/emmo/domain/battery#battery_52ed5408_da62_483d_97d5_a45755022582',
    
    class_name='P2DModel',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/battery#battery_52ed5408_da62_483d_97d5_a45755022582',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'P2DModel',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    