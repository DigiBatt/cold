
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .BariumSaltCompoundModule import BariumSaltCompound







class BariumTrifluoromethanesulfonyloxalatoborate(BariumSaltCompound):
    """
    Class representing the `BariumTrifluoromethanesulfonyloxalatoborate` entity, which inherits from:
    - BariumSaltCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_4d6845ce_47c8_4c7d_b275_1d4494a0799b'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'BariumTrifluoromethanesulfonyloxalatoborate'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = BariumTrifluoromethanesulfonyloxalatoborate(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_4d6845ce_47c8_4c7d_b275_1d4494a0799b',
    
    class_name='BariumTrifluoromethanesulfonyloxalatoborate',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_4d6845ce_47c8_4c7d_b275_1d4494a0799b',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'BariumTrifluoromethanesulfonyloxalatoborate',
        alias="class_name"
    )
    

    
    

    

    