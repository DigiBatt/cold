
from pydantic import BaseModel, Field, validator, root_validator
from typing import Optional, List, Union



from .SIAcceptedUnitModule import SIAcceptedUnit



from .NonPrefixedUnitModule import NonPrefixedUnit



from .LengthFractionUnitModule import LengthFractionUnit








class Arcsecond(SIAcceptedUnit, NonPrefixedUnit, LengthFractionUnit):
    """
    Class representing the `Arcsecond` entity, which inherits from:
    - SIAcceptedUnit, NonPrefixedUnit, LengthFractionUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#Arcsecond'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Arcsecond'`
        - **Alias**: `class_name`
    
    - `hasSIConversionOffset` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSIConversionOffset`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    - `qudtReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `qudtReference`
    
    - `ucumCode` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `ucumCode`
    
    - `uneceCommonCode` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `uneceCommonCode`
    
    - `unitSymbol` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `unitSymbol`
    
    - `hasSIConversionMultiplier` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSIConversionMultiplier`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `hasSymbolValue` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSymbolValue`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Arcsecond(
    
    class_iri='https://w3id.org/emmo#Arcsecond',
    
    class_name='Arcsecond',
    
    hasSIConversionOffset="example_value",
    
    wikipediaReference="example_value",
    
    qudtReference="example_value",
    
    ucumCode="example_value",
    
    uneceCommonCode="example_value",
    
    unitSymbol="example_value",
    
    hasSIConversionMultiplier="example_value",
    
    elucidation="example_value",
    
    hasSymbolValue="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        
            'https://w3id.org/emmo#Arcsecond',
        
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        
            'Arcsecond',
        
        alias="class_name"
    )
    
    hasSIConversionOffset: Optional[str] = Field(
        
            None,
        
        alias="hasSIConversionOffset"
    )
    
    wikipediaReference: Optional[str] = Field(
        
            None,
        
        alias="wikipediaReference"
    )
    
    qudtReference: Optional[str] = Field(
        
            None,
        
        alias="qudtReference"
    )
    
    ucumCode: Optional[str] = Field(
        
            None,
        
        alias="ucumCode"
    )
    
    uneceCommonCode: Optional[str] = Field(
        
            None,
        
        alias="uneceCommonCode"
    )
    
    unitSymbol: Optional[str] = Field(
        
            None,
        
        alias="unitSymbol"
    )
    
    hasSIConversionMultiplier: Optional[str] = Field(
        
            None,
        
        alias="hasSIConversionMultiplier"
    )
    
    elucidation: Optional[str] = Field(
        
            None,
        
        alias="elucidation"
    )
    
    hasSymbolValue: Optional[str] = Field(
        
            None,
        
        alias="hasSymbolValue"
    )
    


    
    

    

    