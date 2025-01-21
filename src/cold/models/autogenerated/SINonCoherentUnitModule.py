
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SIUnitModule import SIUnit







class SINonCoherentUnit(SIUnit):
    """
    Class representing the `SINonCoherentUnit` entity, which inherits from:
    - SIUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_8246541a_f1f6_4d03_8bd7_fc6b76d17375'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SINonCoherentUnit'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SINonCoherentUnit(
    
    class_iri='https://w3id.org/emmo#EMMO_8246541a_f1f6_4d03_8bd7_fc6b76d17375',
    
    class_name='SINonCoherentUnit',
    
    elucidation="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_8246541a_f1f6_4d03_8bd7_fc6b76d17375',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SINonCoherentUnit',
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
    

    
    

    

    