
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SICoherentDerivedUnitModule import SICoherentDerivedUnit



from .AreaPerQuarticTimeUnitModule import AreaPerQuarticTimeUnit







class SquareMetreQuarticHertz(SICoherentDerivedUnit, AreaPerQuarticTimeUnit):
    """
    Class representing the `SquareMetreQuarticHertz` entity, which inherits from:
    - SICoherentDerivedUnit, AreaPerQuarticTimeUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#SquareMetreQuarticHertz'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SquareMetreQuarticHertz'`
        - **Alias**: `class_name`
    
    - `unitSymbol` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `unitSymbol`
    
    - `qudtReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `qudtReference`
    
    - `ucumCode` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `ucumCode`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SquareMetreQuarticHertz(
    
    class_iri='https://w3id.org/emmo#SquareMetreQuarticHertz',
    
    class_name='SquareMetreQuarticHertz',
    
    unitSymbol="example_value",
    
    qudtReference="example_value",
    
    ucumCode="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#SquareMetreQuarticHertz',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SquareMetreQuarticHertz',
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
    
    ucumCode: Optional[str] = Field(
        None,
        alias="ucumCode"
    )
    

    
    

    

    