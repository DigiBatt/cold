
from pydantic import BaseModel, Field, validator, root_validator
from typing import Optional, List, Union



from .SINonCoherentUnitModule import SINonCoherentUnit



from .MicroPrefixedUnitModule import MicroPrefixedUnit



from .AmountPerAreaTimeUnitModule import AmountPerAreaTimeUnit



from .PrefixedUnitModule import PrefixedUnit





from .MolePerSquareMetrePerDayModule import MolePerSquareMetrePerDay






class MicroMolePerSquareMetrePerDay(SINonCoherentUnit, MicroPrefixedUnit, AmountPerAreaTimeUnit, PrefixedUnit):
    """
    Class representing the `MicroMolePerSquareMetrePerDay` entity, which inherits from:
    - SINonCoherentUnit, MicroPrefixedUnit, AmountPerAreaTimeUnit, PrefixedUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#MicroMolePerSquareMetrePerDay'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MicroMolePerSquareMetrePerDay'`
        - **Alias**: `class_name`
    
    - `hasSIConversionMultiplier` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSIConversionMultiplier`
    
    - `ucumCode` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `ucumCode`
    
    - `hasUnitSymbol` (`Optional[MolePerSquareMetrePerDay]`): 
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
    obj = MicroMolePerSquareMetrePerDay(
    
    class_iri='https://w3id.org/emmo#MicroMolePerSquareMetrePerDay',
    
    class_name='MicroMolePerSquareMetrePerDay',
    
    hasSIConversionMultiplier="example_value",
    
    ucumCode="example_value",
    
    hasUnitSymbol="example_value",
    
    unitSymbol="example_value",
    
    qudtReference="example_value",
    
    hasSIConversionOffset="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        
            'https://w3id.org/emmo#MicroMolePerSquareMetrePerDay',
        
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        
            'MicroMolePerSquareMetrePerDay',
        
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
    
    hasUnitSymbol: Optional[MolePerSquareMetrePerDay] = Field(
        
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
    


    
    @validator("hasUnitSymbol", pre=True, always=True)
    def validate_hasUnitSymbol(cls, value):
        if value is not None and not isinstance(value, MolePerSquareMetrePerDay):
            raise ValueError(f"Field 'hasUnitSymbol' must be an instance of 'MolePerSquareMetrePerDay' or its subclass.")
        return value
    
    

    

    