
from pydantic import BaseModel, Field, validator, root_validator
from typing import Optional, List, Union



from .PressurePerTemperatureUnitModule import PressurePerTemperatureUnit



from .SINonCoherentUnitModule import SINonCoherentUnit



from .MilliPrefixedUnitModule import MilliPrefixedUnit



from .PrefixedUnitModule import PrefixedUnit





from .BarPerKelvinModule import BarPerKelvin






class MilliBarPerKelvin(PressurePerTemperatureUnit, SINonCoherentUnit, MilliPrefixedUnit, PrefixedUnit):
    """
    Class representing the `MilliBarPerKelvin` entity, which inherits from:
    - PressurePerTemperatureUnit, SINonCoherentUnit, MilliPrefixedUnit, PrefixedUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#MilliBarPerKelvin'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MilliBarPerKelvin'`
        - **Alias**: `class_name`
    
    - `hasUnitSymbol` (`Optional[BarPerKelvin]`): 
        - **Default Value**: `None`
        - **Alias**: `hasUnitSymbol`
    
    - `hasSIConversionOffset` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSIConversionOffset`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `qudtReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `qudtReference`
    
    - `unitSymbol` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `unitSymbol`
    
    - `ucumCode` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `ucumCode`
    
    - `hasSIConversionMultiplier` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSIConversionMultiplier`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = MilliBarPerKelvin(
    
    class_iri='https://w3id.org/emmo#MilliBarPerKelvin',
    
    class_name='MilliBarPerKelvin',
    
    hasUnitSymbol="example_value",
    
    hasSIConversionOffset="example_value",
    
    elucidation="example_value",
    
    qudtReference="example_value",
    
    unitSymbol="example_value",
    
    ucumCode="example_value",
    
    hasSIConversionMultiplier="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        
            'https://w3id.org/emmo#MilliBarPerKelvin',
        
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        
            'MilliBarPerKelvin',
        
        alias="class_name"
    )
    
    hasUnitSymbol: Optional[BarPerKelvin] = Field(
        
            None,
        
        alias="hasUnitSymbol"
    )
    
    hasSIConversionOffset: Optional[str] = Field(
        
            None,
        
        alias="hasSIConversionOffset"
    )
    
    elucidation: Optional[str] = Field(
        
            None,
        
        alias="elucidation"
    )
    
    qudtReference: Optional[str] = Field(
        
            None,
        
        alias="qudtReference"
    )
    
    unitSymbol: Optional[str] = Field(
        
            None,
        
        alias="unitSymbol"
    )
    
    ucumCode: Optional[str] = Field(
        
            None,
        
        alias="ucumCode"
    )
    
    hasSIConversionMultiplier: Optional[str] = Field(
        
            None,
        
        alias="hasSIConversionMultiplier"
    )
    


    
    @validator("hasUnitSymbol", pre=True, always=True)
    def validate_hasUnitSymbol(cls, value):
        if value is not None and not isinstance(value, BarPerKelvin):
            raise ValueError(f"Field 'hasUnitSymbol' must be an instance of 'BarPerKelvin' or its subclass.")
        return value
    
    

    

    