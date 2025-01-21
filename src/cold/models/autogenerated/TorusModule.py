
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .TwoManifoldModule import TwoManifold







class Torus(TwoManifold):
    """
    Class representing the `Torus` entity, which inherits from:
    - TwoManifold

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_86060335_31c2_4820_b433_27c64aea0366'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Torus'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Torus(
    
    class_iri='https://w3id.org/emmo#EMMO_86060335_31c2_4820_b433_27c64aea0366',
    
    class_name='Torus',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_86060335_31c2_4820_b433_27c64aea0366',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Torus',
        alias="class_name"
    )
    

    
    

    

    