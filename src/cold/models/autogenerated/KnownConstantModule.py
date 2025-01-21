
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .NumericalModule import Numerical



from .ConstantModule import Constant







class KnownConstant(Numerical, Constant):
    """
    Class representing the `KnownConstant` entity, which inherits from:
    - Numerical, Constant

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_ae15fb4f_8e4d_41de_a0f9_3997f89ba6a2'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'KnownConstant'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `example` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `example`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = KnownConstant(
    
    class_iri='https://w3id.org/emmo#EMMO_ae15fb4f_8e4d_41de_a0f9_3997f89ba6a2',
    
    class_name='KnownConstant',
    
    elucidation="example_value",
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_ae15fb4f_8e4d_41de_a0f9_3997f89ba6a2',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'KnownConstant',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    example: Optional[str] = Field(
        None,
        alias="example"
    )
    

    
    

    

    