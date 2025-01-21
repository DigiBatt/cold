
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ObjectivePropertyModule import ObjectiveProperty







class MeasuredProperty(ObjectiveProperty):
    """
    Class representing the `MeasuredProperty` entity, which inherits from:
    - ObjectiveProperty

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_873b0ab3_88e6_4054_b901_5531e01f14a4'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MeasuredProperty'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = MeasuredProperty(
    
    class_iri='https://w3id.org/emmo#EMMO_873b0ab3_88e6_4054_b901_5531e01f14a4',
    
    class_name='MeasuredProperty',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_873b0ab3_88e6_4054_b901_5531e01f14a4',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MeasuredProperty',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    