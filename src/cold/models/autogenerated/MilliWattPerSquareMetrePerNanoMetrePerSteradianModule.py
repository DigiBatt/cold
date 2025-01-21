
from pydantic import BaseModel, Field, validator, root_validator
from typing import Optional, List, Union



from .SINonCoherentUnitModule import SINonCoherentUnit



from .MilliPrefixedUnitModule import MilliPrefixedUnit



from .PrefixedUnitModule import PrefixedUnit



from .PressurePerTimeUnitModule import PressurePerTimeUnit





from .WattPerSquareMetrePerNanoMetrePerSteradianModule import WattPerSquareMetrePerNanoMetrePerSteradian






class MilliWattPerSquareMetrePerNanoMetrePerSteradian(SINonCoherentUnit, MilliPrefixedUnit, PrefixedUnit, PressurePerTimeUnit):
    """
    Class representing the `MilliWattPerSquareMetrePerNanoMetrePerSteradian` entity, which inherits from:
    - SINonCoherentUnit, MilliPrefixedUnit, PrefixedUnit, PressurePerTimeUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#MilliWattPerSquareMetrePerNanoMetrePerSteradian'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MilliWattPerSquareMetrePerNanoMetrePerSteradian'`
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
    
    - `hasUnitNonPrefixPart` (`Optional[WattPerSquareMetrePerNanoMetrePerSteradian]`): 
        - **Default Value**: `None`
        - **Alias**: `hasUnitNonPrefixPart`
    
    - `ucumCode` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `ucumCode`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = MilliWattPerSquareMetrePerNanoMetrePerSteradian(
    
    class_iri='https://w3id.org/emmo#MilliWattPerSquareMetrePerNanoMetrePerSteradian',
    
    class_name='MilliWattPerSquareMetrePerNanoMetrePerSteradian',
    
    qudtReference="example_value",
    
    hasSIConversionMultiplier="example_value",
    
    unitSymbol="example_value",
    
    hasSIConversionOffset="example_value",
    
    hasUnitNonPrefixPart="example_value",
    
    ucumCode="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        
            'https://w3id.org/emmo#MilliWattPerSquareMetrePerNanoMetrePerSteradian',
        
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        
            'MilliWattPerSquareMetrePerNanoMetrePerSteradian',
        
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
    
    hasUnitNonPrefixPart: Optional[WattPerSquareMetrePerNanoMetrePerSteradian] = Field(
        
            None,
        
        alias="hasUnitNonPrefixPart"
    )
    
    ucumCode: Optional[str] = Field(
        
            None,
        
        alias="ucumCode"
    )
    


    
    @validator("hasUnitNonPrefixPart", pre=True, always=True)
    def validate_hasUnitNonPrefixPart(cls, value):
        if value is not None and not isinstance(value, WattPerSquareMetrePerNanoMetrePerSteradian):
            raise ValueError(f"Field 'hasUnitNonPrefixPart' must be an instance of 'WattPerSquareMetrePerNanoMetrePerSteradian' or its subclass.")
        return value
    
    

    

    