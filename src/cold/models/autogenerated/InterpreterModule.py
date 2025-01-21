
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SemioticEntityModule import SemioticEntity



from .CausalSystemModule import CausalSystem







class Interpreter(SemioticEntity, CausalSystem):
    """
    Class representing the `Interpreter` entity, which inherits from:
    - SemioticEntity, CausalSystem

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_0527413c_b286_4e9c_b2d0_03fb2a038dee'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Interpreter'`
        - **Alias**: `class_name`
    
    - `hasSpatialSlice` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSpatialSlice`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `example` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `example`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Interpreter(
    
    class_iri='https://w3id.org/emmo#EMMO_0527413c_b286_4e9c_b2d0_03fb2a038dee',
    
    class_name='Interpreter',
    
    hasSpatialSlice="example_value",
    
    elucidation="example_value",
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_0527413c_b286_4e9c_b2d0_03fb2a038dee',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Interpreter',
        alias="class_name"
    )
    
    hasSpatialSlice: Optional[str] = Field(
        None,
        alias="hasSpatialSlice"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    example: Optional[str] = Field(
        None,
        alias="example"
    )
    

    
    

    

    