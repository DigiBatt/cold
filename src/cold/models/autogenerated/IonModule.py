
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MolecularEntityModule import MolecularEntity







class Ion(MolecularEntity):
    """
    Class representing the `Ion` entity, which inherits from:
    - MolecularEntity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_f07ae87e_b56e_4835_8a28_04c6c7dfbaa2'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Ion'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Ion(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_f07ae87e_b56e_4835_8a28_04c6c7dfbaa2',
    
    class_name='Ion',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_f07ae87e_b56e_4835_8a28_04c6c7dfbaa2',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Ion',
        alias="class_name"
    )
    

    
    

    

    