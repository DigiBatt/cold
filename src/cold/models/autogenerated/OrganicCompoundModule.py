
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ChemicalCompoundModule import ChemicalCompound







class OrganicCompound(ChemicalCompound):
    """
    Class representing the `OrganicCompound` entity, which inherits from:
    - ChemicalCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_704630b8_fee3_49b9_baca_40e2dd276370'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'OrganicCompound'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = OrganicCompound(
    
    class_iri='https://w3id.org/emmo#EMMO_704630b8_fee3_49b9_baca_40e2dd276370',
    
    class_name='OrganicCompound',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_704630b8_fee3_49b9_baca_40e2dd276370',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'OrganicCompound',
        alias="class_name"
    )
    

    
    

    

    