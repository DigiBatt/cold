
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .PureNumberQuantityModule import PureNumberQuantity







class NumberOfElements(PureNumberQuantity):
    """
    Class representing the `NumberOfElements` entity, which inherits from:
    - PureNumberQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_f17133c2_bb33_4ffd_89fa_eef2b403d5e6'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'NumberOfElements'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = NumberOfElements(
    
    class_iri='https://w3id.org/emmo#EMMO_f17133c2_bb33_4ffd_89fa_eef2b403d5e6',
    
    class_name='NumberOfElements',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_f17133c2_bb33_4ffd_89fa_eef2b403d5e6',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'NumberOfElements',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    