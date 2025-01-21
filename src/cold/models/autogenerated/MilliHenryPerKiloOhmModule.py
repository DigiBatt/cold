
from pydantic import BaseModel, Field, validator, root_validator
from typing import Optional, List, Union



from .TimeUnitModule import TimeUnit



from .SINonCoherentUnitModule import SINonCoherentUnit



from .MilliPrefixedUnitModule import MilliPrefixedUnit



from .PrefixedUnitModule import PrefixedUnit





from .HenryPerKiloOhmModule import HenryPerKiloOhm






class MilliHenryPerKiloOhm(TimeUnit, SINonCoherentUnit, MilliPrefixedUnit, PrefixedUnit):
    """
    Class representing the `MilliHenryPerKiloOhm` entity, which inherits from:
    - TimeUnit, SINonCoherentUnit, MilliPrefixedUnit, PrefixedUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#MilliHenryPerKiloOhm'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MilliHenryPerKiloOhm'`
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
    
    - `hasUnitNonPrefixPart` (`Optional[HenryPerKiloOhm]`): 
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
    obj = MilliHenryPerKiloOhm(
    
    class_iri='https://w3id.org/emmo#MilliHenryPerKiloOhm',
    
    class_name='MilliHenryPerKiloOhm',
    
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
        
            'https://w3id.org/emmo#MilliHenryPerKiloOhm',
        
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        
            'MilliHenryPerKiloOhm',
        
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
    
    hasUnitNonPrefixPart: Optional[HenryPerKiloOhm] = Field(
        
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
        if value is not None and not isinstance(value, HenryPerKiloOhm):
            raise ValueError(f"Field 'hasUnitNonPrefixPart' must be an instance of 'HenryPerKiloOhm' or its subclass.")
        return value
    
    

    

    