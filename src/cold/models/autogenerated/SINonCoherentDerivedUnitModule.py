
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SIDerivedUnitModule import SIDerivedUnit



from .SINonCoherentUnitModule import SINonCoherentUnit



from .DerivedUnitModule import DerivedUnit







class SINonCoherentDerivedUnit(SIDerivedUnit, SINonCoherentUnit, DerivedUnit):
    """
    Class representing the `SINonCoherentDerivedUnit` entity, which inherits from:
    - SIDerivedUnit, SINonCoherentUnit, DerivedUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_60b78cc3_6011_4134_95ab_956f56d4bdc1'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SINonCoherentDerivedUnit'`
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
    obj = SINonCoherentDerivedUnit(
    
    class_iri='https://w3id.org/emmo#EMMO_60b78cc3_6011_4134_95ab_956f56d4bdc1',
    
    class_name='SINonCoherentDerivedUnit',
    
    elucidation="example_value",
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_60b78cc3_6011_4134_95ab_956f56d4bdc1',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SINonCoherentDerivedUnit',
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
    

    
    

    

    