
from pydantic import BaseModel, Field, validator, root_validator
from typing import Optional, List, Union



from .SINonCoherentUnitModule import SINonCoherentUnit



from .MassPerVolumeTimeUnitModule import MassPerVolumeTimeUnit



from .MilliPrefixedUnitModule import MilliPrefixedUnit



from .PrefixedUnitModule import PrefixedUnit








class MilliGramPerCubicMetrePerHour(SINonCoherentUnit, MassPerVolumeTimeUnit, MilliPrefixedUnit, PrefixedUnit):
    """
    Class representing the `MilliGramPerCubicMetrePerHour` entity, which inherits from:
    - SINonCoherentUnit, MassPerVolumeTimeUnit, MilliPrefixedUnit, PrefixedUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#MilliGramPerCubicMetrePerHour'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MilliGramPerCubicMetrePerHour'`
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
    obj = MilliGramPerCubicMetrePerHour(
    
    class_iri='https://w3id.org/emmo#MilliGramPerCubicMetrePerHour',
    
    class_name='MilliGramPerCubicMetrePerHour',
    
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
        
            'https://w3id.org/emmo#MilliGramPerCubicMetrePerHour',
        
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        
            'MilliGramPerCubicMetrePerHour',
        
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
    


    
    

    

    