
from pydantic import BaseModel, Field, validator, root_validator
from typing import Optional, List, Union



from .SpeedUnitModule import SpeedUnit



from .SINonCoherentUnitModule import SINonCoherentUnit



from .NonPrefixedUnitModule import NonPrefixedUnit



from .MeasurementUnitModule import MeasurementUnit








class Knot(SpeedUnit, SINonCoherentUnit, NonPrefixedUnit, MeasurementUnit):
    """
    Class representing the `Knot` entity, which inherits from:
    - SpeedUnit, SINonCoherentUnit, NonPrefixedUnit, MeasurementUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#Knot'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Knot'`
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
    
    - `ucumCode` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `ucumCode`
    
    - `hasSIConversionMultiplier` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSIConversionMultiplier`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Knot(
    
    class_iri='https://w3id.org/emmo#Knot',
    
    class_name='Knot',
    
    unitSymbol="example_value",
    
    elucidation="example_value",
    
    qudtReference="example_value",
    
    wikipediaReference="example_value",
    
    hasSIConversionOffset="example_value",
    
    ucumCode="example_value",
    
    hasSIConversionMultiplier="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        
            'https://w3id.org/emmo#Knot',
        
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        
            'Knot',
        
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
    
    ucumCode: Optional[str] = Field(
        
            None,
        
        alias="ucumCode"
    )
    
    hasSIConversionMultiplier: Optional[str] = Field(
        
            None,
        
        alias="hasSIConversionMultiplier"
    )
    


    
    

    

    