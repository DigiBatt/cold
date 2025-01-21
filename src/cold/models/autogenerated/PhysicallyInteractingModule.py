
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CausalSystemModule import CausalSystem







class PhysicallyInteracting(CausalSystem):
    """
    Class representing the `PhysicallyInteracting` entity, which inherits from:
    - CausalSystem

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_09f0ac34_c349_46b5_acf0_0edeae52cca1'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'PhysicallyInteracting'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = PhysicallyInteracting(
    
    class_iri='https://w3id.org/emmo#EMMO_09f0ac34_c349_46b5_acf0_0edeae52cca1',
    
    class_name='PhysicallyInteracting',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_09f0ac34_c349_46b5_acf0_0edeae52cca1',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'PhysicallyInteracting',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    