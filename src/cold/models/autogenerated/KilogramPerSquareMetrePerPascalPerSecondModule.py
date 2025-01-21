
from pydantic import BaseModel, Field, validator, root_validator
from typing import Optional, List, Union



from .SICoherentDerivedUnitModule import SICoherentDerivedUnit



from .NonPrefixedUnitModule import NonPrefixedUnit



from .TimePerLengthUnitModule import TimePerLengthUnit








class KilogramPerSquareMetrePerPascalPerSecond(SICoherentDerivedUnit, NonPrefixedUnit, TimePerLengthUnit):
    """
    Class representing the `KilogramPerSquareMetrePerPascalPerSecond` entity, which inherits from:
    - SICoherentDerivedUnit, NonPrefixedUnit, TimePerLengthUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#KilogramPerSquareMetrePerPascalPerSecond'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'KilogramPerSquareMetrePerPascalPerSecond'`
        - **Alias**: `class_name`
    
    - `hasSIConversionMultiplier` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSIConversionMultiplier`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    - `unitSymbol` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `unitSymbol`
    
    - `hasSIConversionOffset` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSIConversionOffset`
    
    - `qudtReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `qudtReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = KilogramPerSquareMetrePerPascalPerSecond(
    
    class_iri='https://w3id.org/emmo#KilogramPerSquareMetrePerPascalPerSecond',
    
    class_name='KilogramPerSquareMetrePerPascalPerSecond',
    
    hasSIConversionMultiplier="example_value",
    
    wikipediaReference="example_value",
    
    unitSymbol="example_value",
    
    hasSIConversionOffset="example_value",
    
    qudtReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        
            'https://w3id.org/emmo#KilogramPerSquareMetrePerPascalPerSecond',
        
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        
            'KilogramPerSquareMetrePerPascalPerSecond',
        
        alias="class_name"
    )
    
    hasSIConversionMultiplier: Optional[str] = Field(
        
            None,
        
        alias="hasSIConversionMultiplier"
    )
    
    wikipediaReference: Optional[str] = Field(
        
            None,
        
        alias="wikipediaReference"
    )
    
    unitSymbol: Optional[str] = Field(
        
            None,
        
        alias="unitSymbol"
    )
    
    hasSIConversionOffset: Optional[str] = Field(
        
            None,
        
        alias="hasSIConversionOffset"
    )
    
    qudtReference: Optional[str] = Field(
        
            None,
        
        alias="qudtReference"
    )
    


    
    

    

    