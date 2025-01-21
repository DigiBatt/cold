
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .HardeningByFormingModule import HardeningByForming







class Peening(HardeningByForming):
    """
    Class representing the `Peening` entity, which inherits from:
    - HardeningByForming

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_dc0874e8_36e1_44df_947d_0d7c81167a09'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Peening'`
        - **Alias**: `class_name`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Peening(
    
    class_iri='https://w3id.org/emmo#EMMO_dc0874e8_36e1_44df_947d_0d7c81167a09',
    
    class_name='Peening',
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_dc0874e8_36e1_44df_947d_0d7c81167a09',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Peening',
        alias="class_name"
    )
    
    comment: Optional[str] = Field(
        None,
        alias="comment"
    )
    

    
    

    

    