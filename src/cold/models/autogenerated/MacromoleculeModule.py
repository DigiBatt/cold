
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .PolyatomicEntityModule import PolyatomicEntity







class Macromolecule(PolyatomicEntity):
    """
    Class representing the `Macromolecule` entity, which inherits from:
    - PolyatomicEntity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_a14dd591_8b7a_4847_8c91_3a2f421a45b4'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Macromolecule'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Macromolecule(
    
    class_iri='https://w3id.org/emmo#EMMO_a14dd591_8b7a_4847_8c91_3a2f421a45b4',
    
    class_name='Macromolecule',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_a14dd591_8b7a_4847_8c91_3a2f421a45b4',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Macromolecule',
        alias="class_name"
    )
    

    
    

    

    