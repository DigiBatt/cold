
from pydantic import BaseModel, Field, validator, root_validator
from typing import Optional, List, Union



from .SpeedUnitModule import SpeedUnit



from .SINonCoherentUnitModule import SINonCoherentUnit



from .MilliPrefixedUnitModule import MilliPrefixedUnit



from .PrefixedUnitModule import PrefixedUnit








class MilliMetrePerYear(SpeedUnit, SINonCoherentUnit, MilliPrefixedUnit, PrefixedUnit):
    """
    Class representing the `MilliMetrePerYear` entity, which inherits from:
    - SpeedUnit, SINonCoherentUnit, MilliPrefixedUnit, PrefixedUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#MilliMetrePerYear'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MilliMetrePerYear'`
        - **Alias**: `class_name`
    
    - `hasSIConversionMultiplier` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSIConversionMultiplier`
    
    - `ucumCode` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `ucumCode`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `hasUnitSymbol` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasUnitSymbol`
    
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
    obj = MilliMetrePerYear(
    
    class_iri='https://w3id.org/emmo#MilliMetrePerYear',
    
    class_name='MilliMetrePerYear',
    
    hasSIConversionMultiplier="example_value",
    
    ucumCode="example_value",
    
    elucidation="example_value",
    
    hasUnitSymbol="example_value",
    
    unitSymbol="example_value",
    
    qudtReference="example_value",
    
    hasSIConversionOffset="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        
            'https://w3id.org/emmo#MilliMetrePerYear',
        
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        
            'MilliMetrePerYear',
        
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
    
    elucidation: Optional[str] = Field(
        
            None,
        
        alias="elucidation"
    )
    
    hasUnitSymbol: Optional[str] = Field(
        
            None,
        
        alias="hasUnitSymbol"
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
    


    
    

    

    