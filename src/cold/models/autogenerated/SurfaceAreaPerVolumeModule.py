
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ISQDerivedQuantityModule import ISQDerivedQuantity







class SurfaceAreaPerVolume(ISQDerivedQuantity):
    """
    Class representing the `SurfaceAreaPerVolume` entity, which inherits from:
    - ISQDerivedQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_7f381c19_cf07_47a8_ab10_0b14d46901e8'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SurfaceAreaPerVolume'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SurfaceAreaPerVolume(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_7f381c19_cf07_47a8_ab10_0b14d46901e8',
    
    class_name='SurfaceAreaPerVolume',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_7f381c19_cf07_47a8_ab10_0b14d46901e8',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SurfaceAreaPerVolume',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    