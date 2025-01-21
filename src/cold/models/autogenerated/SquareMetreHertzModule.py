
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .AreaPerTimeUnitModule import AreaPerTimeUnit



from .SICoherentDerivedUnitModule import SICoherentDerivedUnit



from .AreicSpeedUnitModule import AreicSpeedUnit







class SquareMetreHertz(AreaPerTimeUnit, SICoherentDerivedUnit, AreicSpeedUnit):
    """
    Class representing the `SquareMetreHertz` entity, which inherits from:
    - AreaPerTimeUnit, SICoherentDerivedUnit, AreicSpeedUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#SquareMetreHertz'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SquareMetreHertz'`
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
    
    - `hasSIConversionOffset` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSIConversionOffset`
    
    - `hasSIConversionMultiplier` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSIConversionMultiplier`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SquareMetreHertz(
    
    class_iri='https://w3id.org/emmo#SquareMetreHertz',
    
    class_name='SquareMetreHertz',
    
    unitSymbol="example_value",
    
    qudtReference="example_value",
    
    ucumCode="example_value",
    
    hasSIConversionOffset="example_value",
    
    hasSIConversionMultiplier="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#SquareMetreHertz',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SquareMetreHertz',
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
    
    hasSIConversionOffset: Optional[str] = Field(
        None,
        alias="hasSIConversionOffset"
    )
    
    hasSIConversionMultiplier: Optional[str] = Field(
        None,
        alias="hasSIConversionMultiplier"
    )
    

    
    

    

    