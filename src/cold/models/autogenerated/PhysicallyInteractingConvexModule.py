
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .PhysicallyInteractingModule import PhysicallyInteracting







class PhysicallyInteractingConvex(PhysicallyInteracting):
    """
    Class representing the `PhysicallyInteractingConvex` entity, which inherits from:
    - PhysicallyInteracting

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_b56c3aa6_28e5_4f9b_a4a5_93d8c68e1570'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'PhysicallyInteractingConvex'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = PhysicallyInteractingConvex(
    
    class_iri='https://w3id.org/emmo#EMMO_b56c3aa6_28e5_4f9b_a4a5_93d8c68e1570',
    
    class_name='PhysicallyInteractingConvex',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_b56c3aa6_28e5_4f9b_a4a5_93d8c68e1570',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'PhysicallyInteractingConvex',
        alias="class_name"
    )
    

    
    

    

    