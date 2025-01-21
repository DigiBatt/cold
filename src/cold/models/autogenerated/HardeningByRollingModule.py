
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .HardeningByFormingModule import HardeningByForming







class HardeningByRolling(HardeningByForming):
    """
    Class representing the `HardeningByRolling` entity, which inherits from:
    - HardeningByForming

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_607ccc15_38aa_4a69_a70a_effa8015bf42'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'HardeningByRolling'`
        - **Alias**: `class_name`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = HardeningByRolling(
    
    class_iri='https://w3id.org/emmo#EMMO_607ccc15_38aa_4a69_a70a_effa8015bf42',
    
    class_name='HardeningByRolling',
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_607ccc15_38aa_4a69_a70a_effa8015bf42',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'HardeningByRolling',
        alias="class_name"
    )
    
    comment: Optional[str] = Field(
        None,
        alias="comment"
    )
    

    
    

    

    