
from pydantic import BaseModel, Field, validator, root_validator
from typing import Optional, List, Union



from .SpeedUnitModule import SpeedUnit



from .KiloPrefixedUnitModule import KiloPrefixedUnit



from .SINonCoherentUnitModule import SINonCoherentUnit



from .PrefixedUnitModule import PrefixedUnit





from .MetrePerSecondModule import MetrePerSecond






class KiloMetrePerSecond(SpeedUnit, KiloPrefixedUnit, SINonCoherentUnit, PrefixedUnit):
    """
    Class representing the `KiloMetrePerSecond` entity, which inherits from:
    - SpeedUnit, KiloPrefixedUnit, SINonCoherentUnit, PrefixedUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#KiloMetrePerSecond'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'KiloMetrePerSecond'`
        - **Alias**: `class_name`
    
    - `qudtReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `qudtReference`
    
    - `hasSIConversionMultiplier` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSIConversionMultiplier`
    
    - `unitSymbol` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `unitSymbol`
    
    - `hasSIConversionOffset` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSIConversionOffset`
    
    - `hasUnitNonPrefixPart` (`Optional[MetrePerSecond]`): 
        - **Default Value**: `None`
        - **Alias**: `hasUnitNonPrefixPart`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `ucumCode` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `ucumCode`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = KiloMetrePerSecond(
    
    class_iri='https://w3id.org/emmo#KiloMetrePerSecond',
    
    class_name='KiloMetrePerSecond',
    
    qudtReference="example_value",
    
    hasSIConversionMultiplier="example_value",
    
    unitSymbol="example_value",
    
    hasSIConversionOffset="example_value",
    
    hasUnitNonPrefixPart="example_value",
    
    elucidation="example_value",
    
    ucumCode="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        
            'https://w3id.org/emmo#KiloMetrePerSecond',
        
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        
            'KiloMetrePerSecond',
        
        alias="class_name"
    )
    
    qudtReference: Optional[str] = Field(
        
            None,
        
        alias="qudtReference"
    )
    
    hasSIConversionMultiplier: Optional[str] = Field(
        
            None,
        
        alias="hasSIConversionMultiplier"
    )
    
    unitSymbol: Optional[str] = Field(
        
            None,
        
        alias="unitSymbol"
    )
    
    hasSIConversionOffset: Optional[str] = Field(
        
            None,
        
        alias="hasSIConversionOffset"
    )
    
    hasUnitNonPrefixPart: Optional[MetrePerSecond] = Field(
        
            None,
        
        alias="hasUnitNonPrefixPart"
    )
    
    elucidation: Optional[str] = Field(
        
            None,
        
        alias="elucidation"
    )
    
    ucumCode: Optional[str] = Field(
        
            None,
        
        alias="ucumCode"
    )
    


    
    @validator("hasUnitNonPrefixPart", pre=True, always=True)
    def validate_hasUnitNonPrefixPart(cls, value):
        if value is not None and not isinstance(value, MetrePerSecond):
            raise ValueError(f"Field 'hasUnitNonPrefixPart' must be an instance of 'MetrePerSecond' or its subclass.")
        return value
    
    

    

    