
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SICoherentDerivedUnitModule import SICoherentDerivedUnit



from .SexticLengthUnitModule import SexticLengthUnit







class SexticMetre(SICoherentDerivedUnit, SexticLengthUnit):
    """
    Class representing the `SexticMetre` entity, which inherits from:
    - SICoherentDerivedUnit, SexticLengthUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#SexticMetre'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SexticMetre'`
        - **Alias**: `class_name`
    
    - `unitSymbol` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `unitSymbol`
    
    - `qudtReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `qudtReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SexticMetre(
    
    class_iri='https://w3id.org/emmo#SexticMetre',
    
    class_name='SexticMetre',
    
    unitSymbol="example_value",
    
    qudtReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#SexticMetre',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SexticMetre',
        alias="class_name"
    )
    
    unitSymbol: Optional[str] = Field(
        None,
        alias="unitSymbol"
    )
    
    qudtReference: Optional[str] = Field(
        None,
        alias="qudtReference"
    )
    

    
    

    

    