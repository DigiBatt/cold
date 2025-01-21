
from pydantic import BaseModel, Field, validator, root_validator
from typing import Optional, List, Union



from .SpeedUnitModule import SpeedUnit



from .SINonCoherentUnitModule import SINonCoherentUnit



from .CentiPrefixedUnitModule import CentiPrefixedUnit



from .PrefixedUnitModule import PrefixedUnit





from .MetrePerYearModule import MetrePerYear






class CentiMetrePerYear(SpeedUnit, SINonCoherentUnit, CentiPrefixedUnit, PrefixedUnit):
    """
    Class representing the `CentiMetrePerYear` entity, which inherits from:
    - SpeedUnit, SINonCoherentUnit, CentiPrefixedUnit, PrefixedUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#CentiMetrePerYear'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CentiMetrePerYear'`
        - **Alias**: `class_name`
    
    - `hasUnitSymbol` (`Optional[MetrePerYear]`): 
        - **Default Value**: `None`
        - **Alias**: `hasUnitSymbol`
    
    - `hasSIConversionOffset` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSIConversionOffset`
    
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
    obj = CentiMetrePerYear(
    
    class_iri='https://w3id.org/emmo#CentiMetrePerYear',
    
    class_name='CentiMetrePerYear',
    
    hasUnitSymbol="example_value",
    
    hasSIConversionOffset="example_value",
    
    qudtReference="example_value",
    
    unitSymbol="example_value",
    
    ucumCode="example_value",
    
    hasSIConversionMultiplier="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        
            'https://w3id.org/emmo#CentiMetrePerYear',
        
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        
            'CentiMetrePerYear',
        
        alias="class_name"
    )
    
    hasUnitSymbol: Optional[MetrePerYear] = Field(
        
            None,
        
        alias="hasUnitSymbol"
    )
    
    hasSIConversionOffset: Optional[str] = Field(
        
            None,
        
        alias="hasSIConversionOffset"
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
        if value is not None and not isinstance(value, MetrePerYear):
            raise ValueError(f"Field 'hasUnitSymbol' must be an instance of 'MetrePerYear' or its subclass.")
        return value
    
    

    

    