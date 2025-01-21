
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .NonPrefixedUnitModule import NonPrefixedUnit







class DerivedUnit(NonPrefixedUnit):
    """
    Class representing the `DerivedUnit` entity, which inherits from:
    - NonPrefixedUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_08b308d4_31cd_4779_a784_aa92fc730f39'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'DerivedUnit'`
        - **Alias**: `class_name`
    
    - `VIMTerm` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `VIMTerm`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = DerivedUnit(
    
    class_iri='https://w3id.org/emmo#EMMO_08b308d4_31cd_4779_a784_aa92fc730f39',
    
    class_name='DerivedUnit',
    
    VIMTerm="example_value",
    
    elucidation="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_08b308d4_31cd_4779_a784_aa92fc730f39',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'DerivedUnit',
        alias="class_name"
    )
    
    VIMTerm: Optional[str] = Field(
        None,
        alias="VIMTerm"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    comment: Optional[str] = Field(
        None,
        alias="comment"
    )
    

    
    

    

    