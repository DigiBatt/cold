
from pydantic import BaseModel, Field, validator, root_validator
from typing import Optional, List, Union



from .AmountSquareTimePerMassVolumeUnitModule import AmountSquareTimePerMassVolumeUnit



from .PicoPrefixedUnitModule import PicoPrefixedUnit



from .SINonCoherentUnitModule import SINonCoherentUnit



from .PrefixedUnitModule import PrefixedUnit








class PicoMolePerMetrePerWattPerSecond(AmountSquareTimePerMassVolumeUnit, PicoPrefixedUnit, SINonCoherentUnit, PrefixedUnit):
    """
    Class representing the `PicoMolePerMetrePerWattPerSecond` entity, which inherits from:
    - AmountSquareTimePerMassVolumeUnit, PicoPrefixedUnit, SINonCoherentUnit, PrefixedUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#PicoMolePerMetrePerWattPerSecond'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'PicoMolePerMetrePerWattPerSecond'`
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
    
    - `ucumCode` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `ucumCode`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = PicoMolePerMetrePerWattPerSecond(
    
    class_iri='https://w3id.org/emmo#PicoMolePerMetrePerWattPerSecond',
    
    class_name='PicoMolePerMetrePerWattPerSecond',
    
    qudtReference="example_value",
    
    hasSIConversionMultiplier="example_value",
    
    unitSymbol="example_value",
    
    hasSIConversionOffset="example_value",
    
    ucumCode="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        
            'https://w3id.org/emmo#PicoMolePerMetrePerWattPerSecond',
        
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        
            'PicoMolePerMetrePerWattPerSecond',
        
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
    
    ucumCode: Optional[str] = Field(
        
            None,
        
        alias="ucumCode"
    )
    


    
    

    

    