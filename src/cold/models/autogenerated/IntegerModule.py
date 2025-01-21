
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .NumberModule import Number







class Integer(Number):
    """
    Class representing the `Integer` entity, which inherits from:
    - Number

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_f8bd64d5_5d3e_4ad4_a46e_c30714fecb7f'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Integer'`
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
    obj = Integer(
    
    class_iri='https://w3id.org/emmo#EMMO_f8bd64d5_5d3e_4ad4_a46e_c30714fecb7f',
    
    class_name='Integer',
    
    elucidation="example_value",
    
    hasNumericalValue="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_f8bd64d5_5d3e_4ad4_a46e_c30714fecb7f',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Integer',
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
    

    
    

    

    