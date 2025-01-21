
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ChemicalNomenclatureModule import ChemicalNomenclature







class ChemicalName(ChemicalNomenclature):
    """
    Class representing the `ChemicalName` entity, which inherits from:
    - ChemicalNomenclature

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_26586828_3b8c_4d8b_9c6c_0bc2502f26ae'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ChemicalName'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ChemicalName(
    
    class_iri='https://w3id.org/emmo#EMMO_26586828_3b8c_4d8b_9c6c_0bc2502f26ae',
    
    class_name='ChemicalName',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_26586828_3b8c_4d8b_9c6c_0bc2502f26ae',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ChemicalName',
        alias="class_name"
    )
    

    
    

    

    