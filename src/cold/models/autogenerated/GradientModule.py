
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .DifferentialOperatorModule import DifferentialOperator







class Gradient(DifferentialOperator):
    """
    Class representing the `Gradient` entity, which inherits from:
    - DifferentialOperator

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_b5c58790_fb2d_42eb_b184_2a3f6ca60acb'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Gradient'`
        - **Alias**: `class_name`
    
    - `hasSymbolValue` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSymbolValue`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Gradient(
    
    class_iri='https://w3id.org/emmo#EMMO_b5c58790_fb2d_42eb_b184_2a3f6ca60acb',
    
    class_name='Gradient',
    
    hasSymbolValue="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_b5c58790_fb2d_42eb_b184_2a3f6ca60acb',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Gradient',
        alias="class_name"
    )
    
    hasSymbolValue: Optional[str] = Field(
        None,
        alias="hasSymbolValue"
    )
    

    
    

    

    