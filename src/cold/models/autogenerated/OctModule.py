
from pydantic import BaseModel, Field, validator, root_validator
from typing import Optional, List, Union



from .SINonCoherentUnitModule import SINonCoherentUnit



from .NonPrefixedUnitModule import NonPrefixedUnit



from .LogarithmicUnitModule import LogarithmicUnit








class Oct(SINonCoherentUnit, NonPrefixedUnit, LogarithmicUnit):
    """
    Class representing the `Oct` entity, which inherits from:
    - SINonCoherentUnit, NonPrefixedUnit, LogarithmicUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#Oct'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Oct'`
        - **Alias**: `class_name`
    
    - `unitSymbol` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `unitSymbol`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `qudtReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `qudtReference`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    - `hasSIConversionOffset` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSIConversionOffset`
    
    - `hasSIConversionMultiplier` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSIConversionMultiplier`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Oct(
    
    class_iri='https://w3id.org/emmo#Oct',
    
    class_name='Oct',
    
    unitSymbol="example_value",
    
    elucidation="example_value",
    
    qudtReference="example_value",
    
    wikipediaReference="example_value",
    
    hasSIConversionOffset="example_value",
    
    hasSIConversionMultiplier="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        
            'https://w3id.org/emmo#Oct',
        
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        
            'Oct',
        
        alias="class_name"
    )
    
    unitSymbol: Optional[str] = Field(
        
            None,
        
        alias="unitSymbol"
    )
    
    elucidation: Optional[str] = Field(
        
            None,
        
        alias="elucidation"
    )
    
    qudtReference: Optional[str] = Field(
        
            None,
        
        alias="qudtReference"
    )
    
    wikipediaReference: Optional[str] = Field(
        
            None,
        
        alias="wikipediaReference"
    )
    
    hasSIConversionOffset: Optional[str] = Field(
        
            None,
        
        alias="hasSIConversionOffset"
    )
    
    hasSIConversionMultiplier: Optional[str] = Field(
        
            None,
        
        alias="hasSIConversionMultiplier"
    )
    


    
    

    

    