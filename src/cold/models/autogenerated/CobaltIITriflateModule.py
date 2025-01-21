
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CobaltSaltCompoundModule import CobaltSaltCompound







class CobaltIITriflate(CobaltSaltCompound):
    """
    Class representing the `CobaltIITriflate` entity, which inherits from:
    - CobaltSaltCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_48108f36_d856_46d4_b293_e174aeff9970'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CobaltIITriflate'`
        - **Alias**: `class_name`
    
    - `pubChemReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `pubChemReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = CobaltIITriflate(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_48108f36_d856_46d4_b293_e174aeff9970',
    
    class_name='CobaltIITriflate',
    
    pubChemReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_48108f36_d856_46d4_b293_e174aeff9970',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CobaltIITriflate',
        alias="class_name"
    )
    
    pubChemReference: Optional[str] = Field(
        None,
        alias="pubChemReference"
    )
    

    
    

    

    