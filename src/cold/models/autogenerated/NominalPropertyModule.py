
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ObjectiveModule import Objective







class NominalProperty(Objective):
    """
    Class representing the `NominalProperty` entity, which inherits from:
    - Objective

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_909415d1_7c43_4d5e_bbeb_7e1910159f66'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'NominalProperty'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `example` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `example`
    
    - `VIMTerm` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `VIMTerm`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = NominalProperty(
    
    class_iri='https://w3id.org/emmo#EMMO_909415d1_7c43_4d5e_bbeb_7e1910159f66',
    
    class_name='NominalProperty',
    
    elucidation="example_value",
    
    example="example_value",
    
    VIMTerm="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_909415d1_7c43_4d5e_bbeb_7e1910159f66',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'NominalProperty',
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
    
    VIMTerm: Optional[str] = Field(
        None,
        alias="VIMTerm"
    )
    

    
    

    

    