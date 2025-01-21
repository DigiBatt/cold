
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ChemicalMaterialModule import ChemicalMaterial







class ElementalMaterial(ChemicalMaterial):
    """
    Class representing the `ElementalMaterial` entity, which inherits from:
    - ChemicalMaterial

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_a086af15_a7c3_404c_b4ce_c8e4466f1b4b'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ElementalMaterial'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ElementalMaterial(
    
    class_iri='https://w3id.org/emmo#EMMO_a086af15_a7c3_404c_b4ce_c8e4466f1b4b',
    
    class_name='ElementalMaterial',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_a086af15_a7c3_404c_b4ce_c8e4466f1b4b',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ElementalMaterial',
        alias="class_name"
    )
    

    
    

    

    