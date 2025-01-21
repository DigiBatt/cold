
from pydantic import BaseModel, Field, validator, root_validator
from typing import Optional, List, Union



from .AmountPerMassTimeUnitModule import AmountPerMassTimeUnit



from .SINonCoherentUnitModule import SINonCoherentUnit



from .MicroPrefixedUnitModule import MicroPrefixedUnit



from .PrefixedUnitModule import PrefixedUnit





from .MolePerGramPerHourModule import MolePerGramPerHour






class MicroMolePerGramPerHour(AmountPerMassTimeUnit, SINonCoherentUnit, MicroPrefixedUnit, PrefixedUnit):
    """
    Class representing the `MicroMolePerGramPerHour` entity, which inherits from:
    - AmountPerMassTimeUnit, SINonCoherentUnit, MicroPrefixedUnit, PrefixedUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#MicroMolePerGramPerHour'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MicroMolePerGramPerHour'`
        - **Alias**: `class_name`
    
    - `hasSIConversionMultiplier` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSIConversionMultiplier`
    
    - `ucumCode` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `ucumCode`
    
    - `hasUnitSymbol` (`Optional[MolePerGramPerHour]`): 
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
    obj = MicroMolePerGramPerHour(
    
    class_iri='https://w3id.org/emmo#MicroMolePerGramPerHour',
    
    class_name='MicroMolePerGramPerHour',
    
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
        
            'https://w3id.org/emmo#MicroMolePerGramPerHour',
        
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        
            'MicroMolePerGramPerHour',
        
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
    
    hasUnitSymbol: Optional[MolePerGramPerHour] = Field(
        
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
        if value is not None and not isinstance(value, MolePerGramPerHour):
            raise ValueError(f"Field 'hasUnitSymbol' must be an instance of 'MolePerGramPerHour' or its subclass.")
        return value
    
    

    

    