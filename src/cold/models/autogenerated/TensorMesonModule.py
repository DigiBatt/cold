
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MesonModule import Meson







class TensorMeson(Meson):
    """
    Class representing the `TensorMeson` entity, which inherits from:
    - Meson

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_f895cb83_2280_42e9_9f4c_047273e70d3c'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'TensorMeson'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = TensorMeson(
    
    class_iri='https://w3id.org/emmo#EMMO_f895cb83_2280_42e9_9f4c_047273e70d3c',
    
    class_name='TensorMeson',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_f895cb83_2280_42e9_9f4c_047273e70d3c',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'TensorMeson',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    