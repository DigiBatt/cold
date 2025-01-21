
from pydantic import BaseModel, Field, validator, root_validator
from typing import Optional, List, Union



from .SINonCoherentUnitModule import SINonCoherentUnit



from .MicroPrefixedUnitModule import MicroPrefixedUnit



from .AmountPerVolumeTimeUnitModule import AmountPerVolumeTimeUnit



from .PrefixedUnitModule import PrefixedUnit








class MicroMolePerLitrePerHour(SINonCoherentUnit, MicroPrefixedUnit, AmountPerVolumeTimeUnit, PrefixedUnit):
    """
    Class representing the `MicroMolePerLitrePerHour` entity, which inherits from:
    - SINonCoherentUnit, MicroPrefixedUnit, AmountPerVolumeTimeUnit, PrefixedUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#MicroMolePerLitrePerHour'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MicroMolePerLitrePerHour'`
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
    
    - `qudtReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `qudtReference`
    
    - `hasSIConversionOffset` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSIConversionOffset`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = MicroMolePerLitrePerHour(
    
    class_iri='https://w3id.org/emmo#MicroMolePerLitrePerHour',
    
    class_name='MicroMolePerLitrePerHour',
    
    hasSIConversionMultiplier="example_value",
    
    ucumCode="example_value",
    
    unitSymbol="example_value",
    
    qudtReference="example_value",
    
    hasSIConversionOffset="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        
            'https://w3id.org/emmo#MicroMolePerLitrePerHour',
        
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        
            'MicroMolePerLitrePerHour',
        
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
    
    qudtReference: Optional[str] = Field(
        
            None,
        
        alias="qudtReference"
    )
    
    hasSIConversionOffset: Optional[str] = Field(
        
            None,
        
        alias="hasSIConversionOffset"
    )
    


    
    

    

    