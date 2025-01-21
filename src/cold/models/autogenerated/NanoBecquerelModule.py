
from pydantic import BaseModel, Field, validator, root_validator
from typing import Optional, List, Union



from .FrequencyUnitModule import FrequencyUnit



from .SINonCoherentUnitModule import SINonCoherentUnit



from .PrefixedUnitModule import PrefixedUnit



from .NanoPrefixedUnitModule import NanoPrefixedUnit





from .BecquerelModule import Becquerel






class NanoBecquerel(FrequencyUnit, SINonCoherentUnit, PrefixedUnit, NanoPrefixedUnit):
    """
    Class representing the `NanoBecquerel` entity, which inherits from:
    - FrequencyUnit, SINonCoherentUnit, PrefixedUnit, NanoPrefixedUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#NanoBecquerel'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'NanoBecquerel'`
        - **Alias**: `class_name`
    
    - `hasSIConversionOffset` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSIConversionOffset`
    
    - `qudtReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `qudtReference`
    
    - `unitSymbol` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `unitSymbol`
    
    - `hasSIConversionMultiplier` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSIConversionMultiplier`
    
    - `hasUnitSymbol` (`Optional[Becquerel]`): 
        - **Default Value**: `None`
        - **Alias**: `hasUnitSymbol`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = NanoBecquerel(
    
    class_iri='https://w3id.org/emmo#NanoBecquerel',
    
    class_name='NanoBecquerel',
    
    hasSIConversionOffset="example_value",
    
    qudtReference="example_value",
    
    unitSymbol="example_value",
    
    hasSIConversionMultiplier="example_value",
    
    hasUnitSymbol="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        
            'https://w3id.org/emmo#NanoBecquerel',
        
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        
            'NanoBecquerel',
        
        alias="class_name"
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
    
    hasSIConversionMultiplier: Optional[str] = Field(
        
            None,
        
        alias="hasSIConversionMultiplier"
    )
    
    hasUnitSymbol: Optional[Becquerel] = Field(
        
            None,
        
        alias="hasUnitSymbol"
    )
    


    
    @validator("hasUnitSymbol", pre=True, always=True)
    def validate_hasUnitSymbol(cls, value):
        if value is not None and not isinstance(value, Becquerel):
            raise ValueError(f"Field 'hasUnitSymbol' must be an instance of 'Becquerel' or its subclass.")
        return value
    
    

    

    