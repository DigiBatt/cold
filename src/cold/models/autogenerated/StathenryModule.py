
from pydantic import BaseModel, Field, validator, root_validator
from typing import Optional, List, Union



from .InductanceUnitModule import InductanceUnit



from .SINonCoherentUnitModule import SINonCoherentUnit



from .NonPrefixedUnitModule import NonPrefixedUnit



from .MeasurementUnitModule import MeasurementUnit








class Stathenry(InductanceUnit, SINonCoherentUnit, NonPrefixedUnit, MeasurementUnit):
    """
    Class representing the `Stathenry` entity, which inherits from:
    - InductanceUnit, SINonCoherentUnit, NonPrefixedUnit, MeasurementUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#Stathenry'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Stathenry'`
        - **Alias**: `class_name`
    
    - `hasSIConversionMultiplier` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSIConversionMultiplier`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `qudtReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `qudtReference`
    
    - `hasSIConversionOffset` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSIConversionOffset`
    
    - `unitSymbol` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `unitSymbol`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Stathenry(
    
    class_iri='https://w3id.org/emmo#Stathenry',
    
    class_name='Stathenry',
    
    hasSIConversionMultiplier="example_value",
    
    elucidation="example_value",
    
    qudtReference="example_value",
    
    hasSIConversionOffset="example_value",
    
    unitSymbol="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        
            'https://w3id.org/emmo#Stathenry',
        
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        
            'Stathenry',
        
        alias="class_name"
    )
    
    hasSIConversionMultiplier: Optional[str] = Field(
        
            None,
        
        alias="hasSIConversionMultiplier"
    )
    
    elucidation: Optional[str] = Field(
        
            None,
        
        alias="elucidation"
    )
    
    qudtReference: Optional[str] = Field(
        
            None,
        
        alias="qudtReference"
    )
    
    hasSIConversionOffset: Optional[str] = Field(
        
            None,
        
        alias="hasSIConversionOffset"
    )
    
    unitSymbol: Optional[str] = Field(
        
            None,
        
        alias="unitSymbol"
    )
    


    
    

    

    