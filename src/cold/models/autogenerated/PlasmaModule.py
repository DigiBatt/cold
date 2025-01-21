
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .FluidModule import Fluid







class Plasma(Fluid):
    """
    Class representing the `Plasma` entity, which inherits from:
    - Fluid

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_4c21fb86_fdcf_444e_b498_86fe656295af'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Plasma'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Plasma(
    
    class_iri='https://w3id.org/emmo#EMMO_4c21fb86_fdcf_444e_b498_86fe656295af',
    
    class_name='Plasma',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_4c21fb86_fdcf_444e_b498_86fe656295af',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Plasma',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    