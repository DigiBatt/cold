
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .PropertyModule import Property







class Hazard(Property):
    """
    Class representing the `Hazard` entity, which inherits from:
    - Property

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/characterisation-methodology/chameo#Hazard'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Hazard'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Hazard(
    
    class_iri='https://w3id.org/emmo/domain/characterisation-methodology/chameo#Hazard',
    
    class_name='Hazard',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/characterisation-methodology/chameo#Hazard',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Hazard',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    