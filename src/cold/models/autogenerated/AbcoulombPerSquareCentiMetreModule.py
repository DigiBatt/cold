
from pydantic import BaseModel, Field, validator, root_validator
from typing import Optional, List, Union



from .ElectricDisplacementFieldUnitModule import ElectricDisplacementFieldUnit



from .SINonCoherentUnitModule import SINonCoherentUnit



from .MeasurementUnitModule import MeasurementUnit



from .PrefixedUnitModule import PrefixedUnit








class AbcoulombPerSquareCentiMetre(ElectricDisplacementFieldUnit, SINonCoherentUnit, MeasurementUnit, PrefixedUnit):
    """
    Class representing the `AbcoulombPerSquareCentiMetre` entity, which inherits from:
    - ElectricDisplacementFieldUnit, SINonCoherentUnit, MeasurementUnit, PrefixedUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#AbcoulombPerSquareCentiMetre'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'AbcoulombPerSquareCentiMetre'`
        - **Alias**: `class_name`
    
    - `hasSIConversionOffset` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSIConversionOffset`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `qudtReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `qudtReference`
    
    - `unitSymbol` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `unitSymbol`
    
    - `ucumCode` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `ucumCode`
    
    - `hasSIConversionMultiplier` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSIConversionMultiplier`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = AbcoulombPerSquareCentiMetre(
    
    class_iri='https://w3id.org/emmo#AbcoulombPerSquareCentiMetre',
    
    class_name='AbcoulombPerSquareCentiMetre',
    
    hasSIConversionOffset="example_value",
    
    elucidation="example_value",
    
    qudtReference="example_value",
    
    unitSymbol="example_value",
    
    ucumCode="example_value",
    
    hasSIConversionMultiplier="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        
            'https://w3id.org/emmo#AbcoulombPerSquareCentiMetre',
        
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        
            'AbcoulombPerSquareCentiMetre',
        
        alias="class_name"
    )
    
    hasSIConversionOffset: Optional[str] = Field(
        
            None,
        
        alias="hasSIConversionOffset"
    )
    
    elucidation: Optional[str] = Field(
        
            None,
        
        alias="elucidation"
    )
    
    qudtReference: Optional[str] = Field(
        
            None,
        
        alias="qudtReference"
    )
    
    unitSymbol: Optional[str] = Field(
        
            None,
        
        alias="unitSymbol"
    )
    
    ucumCode: Optional[str] = Field(
        
            None,
        
        alias="ucumCode"
    )
    
    hasSIConversionMultiplier: Optional[str] = Field(
        
            None,
        
        alias="hasSIConversionMultiplier"
    )
    


    
    

    

    