
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .QuantityModule import Quantity







class PhysicalQuantity(Quantity):
    """
    Class representing the `PhysicalQuantity` entity, which inherits from:
    - Quantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_02c0621e_a527_4790_8a0f_2bb51973c819'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'PhysicalQuantity'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = PhysicalQuantity(
    
    class_iri='https://w3id.org/emmo#EMMO_02c0621e_a527_4790_8a0f_2bb51973c819',
    
    class_name='PhysicalQuantity',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_02c0621e_a527_4790_8a0f_2bb51973c819',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'PhysicalQuantity',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    