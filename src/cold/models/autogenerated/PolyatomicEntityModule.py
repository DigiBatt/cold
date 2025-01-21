
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MolecularEntityModule import MolecularEntity







class PolyatomicEntity(MolecularEntity):
    """
    Class representing the `PolyatomicEntity` entity, which inherits from:
    - MolecularEntity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_9fa966c7_5231_409e_841f_b4c5fd33732a'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'PolyatomicEntity'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = PolyatomicEntity(
    
    class_iri='https://w3id.org/emmo#EMMO_9fa966c7_5231_409e_841f_b4c5fd33732a',
    
    class_name='PolyatomicEntity',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_9fa966c7_5231_409e_841f_b4c5fd33732a',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'PolyatomicEntity',
        alias="class_name"
    )
    

    
    

    

    