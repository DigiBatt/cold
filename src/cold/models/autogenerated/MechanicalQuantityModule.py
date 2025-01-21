
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ISO80000CategorisedModule import ISO80000Categorised







class MechanicalQuantity(ISO80000Categorised):
    """
    Class representing the `MechanicalQuantity` entity, which inherits from:
    - ISO80000Categorised

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_be76ad52_2e29_4202_be6f_0a15eb9c1817'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MechanicalQuantity'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = MechanicalQuantity(
    
    class_iri='https://w3id.org/emmo#EMMO_be76ad52_2e29_4202_be6f_0a15eb9c1817',
    
    class_name='MechanicalQuantity',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_be76ad52_2e29_4202_be6f_0a15eb9c1817',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MechanicalQuantity',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    