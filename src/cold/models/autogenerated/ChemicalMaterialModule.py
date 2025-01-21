
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MaterialModule import Material







class ChemicalMaterial(Material):
    """
    Class representing the `ChemicalMaterial` entity, which inherits from:
    - Material

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_8a41ed1b_64f9_4be7_9b60_01fcece45075'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ChemicalMaterial'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ChemicalMaterial(
    
    class_iri='https://w3id.org/emmo#EMMO_8a41ed1b_64f9_4be7_9b60_01fcece45075',
    
    class_name='ChemicalMaterial',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_8a41ed1b_64f9_4be7_9b60_01fcece45075',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ChemicalMaterial',
        alias="class_name"
    )
    

    
    

    

    