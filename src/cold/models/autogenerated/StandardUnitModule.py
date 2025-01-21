
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MetrologicalReferenceModule import MetrologicalReference







class StandardUnit(MetrologicalReference):
    """
    Class representing the `StandardUnit` entity, which inherits from:
    - MetrologicalReference

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_acd1a504_ca32_4f30_86ad_0b62cea5bc02'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'StandardUnit'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `example` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `example`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = StandardUnit(
    
    class_iri='https://w3id.org/emmo#EMMO_acd1a504_ca32_4f30_86ad_0b62cea5bc02',
    
    class_name='StandardUnit',
    
    elucidation="example_value",
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_acd1a504_ca32_4f30_86ad_0b62cea5bc02',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'StandardUnit',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    example: Optional[str] = Field(
        None,
        alias="example"
    )
    

    
    

    

    