
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .HolisticModule import Holistic





from .RoleModule import Role





class Whole(Holistic):
    """
    Class representing the `Whole` entity, which inherits from:
    - Holistic

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_1efe8b96_e006_4a33_bc9a_421406cbb9f0'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Whole'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    - `hasHolisticPart` (`Optional[Role]`): 
        - **Default Value**: `None`
        - **Alias**: `hasHolisticPart`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Whole(
    
    class_iri='https://w3id.org/emmo#EMMO_1efe8b96_e006_4a33_bc9a_421406cbb9f0',
    
    class_name='Whole',
    
    elucidation="example_value",
    
    comment="example_value",
    
    hasHolisticPart="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_1efe8b96_e006_4a33_bc9a_421406cbb9f0',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Whole',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    comment: Optional[str] = Field(
        None,
        alias="comment"
    )
    
    hasHolisticPart: Optional[Role] = Field(
        None,
        alias="hasHolisticPart"
    )
    

    
    @validator("hasHolisticPart", pre=True, always=True)
    def validate_hasHolisticPart(cls, value):
        if value is not None and not isinstance(value, Role):
            raise ValueError(f"Field 'hasHolisticPart' must be an instance of 'Role' or its subclass.")
        return value
    
    

    

    