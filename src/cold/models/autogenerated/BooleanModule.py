
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .NumberModule import Number







class Boolean(Number):
    """
    Class representing the `Boolean` entity, which inherits from:
    - Number

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_54dc83cb_06e1_4739_9e45_bc09cead7f48'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Boolean'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `hasNumericalValue` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasNumericalValue`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Boolean(
    
    class_iri='https://w3id.org/emmo#EMMO_54dc83cb_06e1_4739_9e45_bc09cead7f48',
    
    class_name='Boolean',
    
    elucidation="example_value",
    
    hasNumericalValue="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_54dc83cb_06e1_4739_9e45_bc09cead7f48',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Boolean',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    hasNumericalValue: Optional[str] = Field(
        None,
        alias="hasNumericalValue"
    )
    

    
    

    

    