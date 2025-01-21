
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ChemicalCompoundModule import ChemicalCompound







class InorganicCompound(ChemicalCompound):
    """
    Class representing the `InorganicCompound` entity, which inherits from:
    - ChemicalCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_4e659c69_ca2d_4569_8a96_f99857a1fa32'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'InorganicCompound'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = InorganicCompound(
    
    class_iri='https://w3id.org/emmo#EMMO_4e659c69_ca2d_4569_8a96_f99857a1fa32',
    
    class_name='InorganicCompound',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_4e659c69_ca2d_4569_8a96_f99857a1fa32',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'InorganicCompound',
        alias="class_name"
    )
    

    
    

    

    