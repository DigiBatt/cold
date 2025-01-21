
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ManganeseSaltCompoundModule import ManganeseSaltCompound







class ManganeseIIChlorate(ManganeseSaltCompound):
    """
    Class representing the `ManganeseIIChlorate` entity, which inherits from:
    - ManganeseSaltCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_09aa1409_b244_4d5e_a6ed_c94bdff60e42'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ManganeseIIChlorate'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ManganeseIIChlorate(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_09aa1409_b244_4d5e_a6ed_c94bdff60e42',
    
    class_name='ManganeseIIChlorate',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_09aa1409_b244_4d5e_a6ed_c94bdff60e42',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ManganeseIIChlorate',
        alias="class_name"
    )
    

    
    

    

    