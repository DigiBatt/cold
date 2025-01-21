
from pydantic import BaseModel, Field, validator, root_validator
from typing import Optional, List, Union



from .SICoherentDerivedUnitModule import SICoherentDerivedUnit



from .NonPrefixedUnitModule import NonPrefixedUnit



from .MassPerSquareLengthSquareTimeUnitModule import MassPerSquareLengthSquareTimeUnit








class KilogramPerSquareMetreSquareSecond(SICoherentDerivedUnit, NonPrefixedUnit, MassPerSquareLengthSquareTimeUnit):
    """
    Class representing the `KilogramPerSquareMetreSquareSecond` entity, which inherits from:
    - SICoherentDerivedUnit, NonPrefixedUnit, MassPerSquareLengthSquareTimeUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#KilogramPerSquareMetreSquareSecond'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'KilogramPerSquareMetreSquareSecond'`
        - **Alias**: `class_name`
    
    - `hasSIConversionMultiplier` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSIConversionMultiplier`
    
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
    obj = KilogramPerSquareMetreSquareSecond(
    
    class_iri='https://w3id.org/emmo#KilogramPerSquareMetreSquareSecond',
    
    class_name='KilogramPerSquareMetreSquareSecond',
    
    hasSIConversionMultiplier="example_value",
    
    unitSymbol="example_value",
    
    hasSIConversionOffset="example_value",
    
    qudtReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        
            'https://w3id.org/emmo#KilogramPerSquareMetreSquareSecond',
        
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        
            'KilogramPerSquareMetreSquareSecond',
        
        alias="class_name"
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
    
    qudtReference: Optional[str] = Field(
        
            None,
        
        alias="qudtReference"
    )
    


    
    

    

    