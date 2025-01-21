
from pydantic import BaseModel, Field, validator, root_validator
from typing import Optional, List, Union



from .KiloPrefixedUnitModule import KiloPrefixedUnit



from .SINonCoherentUnitModule import SINonCoherentUnit



from .LengthUnitModule import LengthUnit



from .PrefixedUnitModule import PrefixedUnit





from .MetreModule import Metre






class KiloMetre(KiloPrefixedUnit, SINonCoherentUnit, LengthUnit, PrefixedUnit):
    """
    Class representing the `KiloMetre` entity, which inherits from:
    - KiloPrefixedUnit, SINonCoherentUnit, LengthUnit, PrefixedUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#KiloMetre'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'KiloMetre'`
        - **Alias**: `class_name`
    
    - `hasSIConversionOffset` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSIConversionOffset`
    
    - `ucumCode` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `ucumCode`
    
    - `qudtReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `qudtReference`
    
    - `unitSymbol` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `unitSymbol`
    
    - `hasSIConversionMultiplier` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSIConversionMultiplier`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    - `hasUnitSymbol` (`Optional[Metre]`): 
        - **Default Value**: `None`
        - **Alias**: `hasUnitSymbol`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = KiloMetre(
    
    class_iri='https://w3id.org/emmo#KiloMetre',
    
    class_name='KiloMetre',
    
    hasSIConversionOffset="example_value",
    
    ucumCode="example_value",
    
    qudtReference="example_value",
    
    unitSymbol="example_value",
    
    hasSIConversionMultiplier="example_value",
    
    wikipediaReference="example_value",
    
    hasUnitSymbol="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        
            'https://w3id.org/emmo#KiloMetre',
        
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        
            'KiloMetre',
        
        alias="class_name"
    )
    
    hasSIConversionOffset: Optional[str] = Field(
        
            None,
        
        alias="hasSIConversionOffset"
    )
    
    ucumCode: Optional[str] = Field(
        
            None,
        
        alias="ucumCode"
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
    
    wikipediaReference: Optional[str] = Field(
        
            None,
        
        alias="wikipediaReference"
    )
    
    hasUnitSymbol: Optional[Metre] = Field(
        
            None,
        
        alias="hasUnitSymbol"
    )
    
    elucidation: Optional[str] = Field(
        
            None,
        
        alias="elucidation"
    )
    


    
    @validator("hasUnitSymbol", pre=True, always=True)
    def validate_hasUnitSymbol(cls, value):
        if value is not None and not isinstance(value, Metre):
            raise ValueError(f"Field 'hasUnitSymbol' must be an instance of 'Metre' or its subclass.")
        return value
    
    

    

    