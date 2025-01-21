
from pydantic import BaseModel, Field, validator, root_validator
from typing import Optional, List, Union



from .PerPressureUnitModule import PerPressureUnit



from .SINonCoherentUnitModule import SINonCoherentUnit



from .PrefixedUnitModule import PrefixedUnit



from .NanoPrefixedUnitModule import NanoPrefixedUnit








class NanoMeterPerMilliMeterMegaPascal(PerPressureUnit, SINonCoherentUnit, PrefixedUnit, NanoPrefixedUnit):
    """
    Class representing the `NanoMeterPerMilliMeterMegaPascal` entity, which inherits from:
    - PerPressureUnit, SINonCoherentUnit, PrefixedUnit, NanoPrefixedUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#NanoMeterPerMilliMeterMegaPascal'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'NanoMeterPerMilliMeterMegaPascal'`
        - **Alias**: `class_name`
    
    - `hasSIConversionMultiplier` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSIConversionMultiplier`
    
    - `ucumCode` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `ucumCode`
    
    - `unitSymbol` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `unitSymbol`
    
    - `hasSIConversionOffset` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSIConversionOffset`
    
    - `qudtReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `qudtReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = NanoMeterPerMilliMeterMegaPascal(
    
    class_iri='https://w3id.org/emmo#NanoMeterPerMilliMeterMegaPascal',
    
    class_name='NanoMeterPerMilliMeterMegaPascal',
    
    hasSIConversionMultiplier="example_value",
    
    ucumCode="example_value",
    
    unitSymbol="example_value",
    
    hasSIConversionOffset="example_value",
    
    qudtReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        
            'https://w3id.org/emmo#NanoMeterPerMilliMeterMegaPascal',
        
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        
            'NanoMeterPerMilliMeterMegaPascal',
        
        alias="class_name"
    )
    
    hasSIConversionMultiplier: Optional[str] = Field(
        
            None,
        
        alias="hasSIConversionMultiplier"
    )
    
    ucumCode: Optional[str] = Field(
        
            None,
        
        alias="ucumCode"
    )
    
    unitSymbol: Optional[str] = Field(
        
            None,
        
        alias="unitSymbol"
    )
    
    hasSIConversionOffset: Optional[str] = Field(
        
            None,
        
        alias="hasSIConversionOffset"
    )
    
    qudtReference: Optional[str] = Field(
        
            None,
        
        alias="qudtReference"
    )
    


    
    

    

    