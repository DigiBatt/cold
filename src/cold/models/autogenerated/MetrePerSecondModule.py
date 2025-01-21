
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SICoherentDerivedUnitModule import SICoherentDerivedUnit



from .SpeedUnitModule import SpeedUnit







class MetrePerSecond(SICoherentDerivedUnit, SpeedUnit):
    """
    Class representing the `MetrePerSecond` entity, which inherits from:
    - SICoherentDerivedUnit, SpeedUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#MetrePerSecond'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MetrePerSecond'`
        - **Alias**: `class_name`
    
    - `unitSymbol` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `unitSymbol`
    
    - `qudtReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `qudtReference`
    
    - `omReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `omReference`
    
    - `ucumCode` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `ucumCode`
    
    - `uneceCommonCode` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `uneceCommonCode`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `hasSIConversionOffset` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSIConversionOffset`
    
    - `hasSIConversionMultiplier` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSIConversionMultiplier`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = MetrePerSecond(
    
    class_iri='https://w3id.org/emmo#MetrePerSecond',
    
    class_name='MetrePerSecond',
    
    unitSymbol="example_value",
    
    qudtReference="example_value",
    
    omReference="example_value",
    
    ucumCode="example_value",
    
    uneceCommonCode="example_value",
    
    elucidation="example_value",
    
    hasSIConversionOffset="example_value",
    
    hasSIConversionMultiplier="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#MetrePerSecond',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MetrePerSecond',
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
    
    omReference: Optional[str] = Field(
        None,
        alias="omReference"
    )
    
    ucumCode: Optional[str] = Field(
        None,
        alias="ucumCode"
    )
    
    uneceCommonCode: Optional[str] = Field(
        None,
        alias="uneceCommonCode"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    hasSIConversionOffset: Optional[str] = Field(
        None,
        alias="hasSIConversionOffset"
    )
    
    hasSIConversionMultiplier: Optional[str] = Field(
        None,
        alias="hasSIConversionMultiplier"
    )
    

    
    

    

    