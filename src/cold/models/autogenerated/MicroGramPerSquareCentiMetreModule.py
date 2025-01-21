
from pydantic import BaseModel, Field, validator, root_validator
from typing import Optional, List, Union



from .SINonCoherentUnitModule import SINonCoherentUnit



from .AreaDensityUnitModule import AreaDensityUnit



from .MicroPrefixedUnitModule import MicroPrefixedUnit



from .PrefixedUnitModule import PrefixedUnit





from .GramPerSquareCentiMetreModule import GramPerSquareCentiMetre






class MicroGramPerSquareCentiMetre(SINonCoherentUnit, AreaDensityUnit, MicroPrefixedUnit, PrefixedUnit):
    """
    Class representing the `MicroGramPerSquareCentiMetre` entity, which inherits from:
    - SINonCoherentUnit, AreaDensityUnit, MicroPrefixedUnit, PrefixedUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#MicroGramPerSquareCentiMetre'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MicroGramPerSquareCentiMetre'`
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
    
    - `hasUnitNonPrefixPart` (`Optional[GramPerSquareCentiMetre]`): 
        - **Default Value**: `None`
        - **Alias**: `hasUnitNonPrefixPart`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = MicroGramPerSquareCentiMetre(
    
    class_iri='https://w3id.org/emmo#MicroGramPerSquareCentiMetre',
    
    class_name='MicroGramPerSquareCentiMetre',
    
    qudtReference="example_value",
    
    hasSIConversionMultiplier="example_value",
    
    unitSymbol="example_value",
    
    hasSIConversionOffset="example_value",
    
    hasUnitNonPrefixPart="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        
            'https://w3id.org/emmo#MicroGramPerSquareCentiMetre',
        
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        
            'MicroGramPerSquareCentiMetre',
        
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
    
    hasUnitNonPrefixPart: Optional[GramPerSquareCentiMetre] = Field(
        
            None,
        
        alias="hasUnitNonPrefixPart"
    )
    
    elucidation: Optional[str] = Field(
        
            None,
        
        alias="elucidation"
    )
    


    
    @validator("hasUnitNonPrefixPart", pre=True, always=True)
    def validate_hasUnitNonPrefixPart(cls, value):
        if value is not None and not isinstance(value, GramPerSquareCentiMetre):
            raise ValueError(f"Field 'hasUnitNonPrefixPart' must be an instance of 'GramPerSquareCentiMetre' or its subclass.")
        return value
    
    

    

    