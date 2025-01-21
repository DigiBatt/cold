
from pydantic import BaseModel, Field, validator, root_validator
from typing import Optional, List, Union



from .NonSIUnitModule import NonSIUnit



from .DimensionlessUnitModule import DimensionlessUnit



from .NonPrefixedUnitModule import NonPrefixedUnit



from .MeasurementUnitModule import MeasurementUnit








class PracticalSalinityUnit(NonSIUnit, DimensionlessUnit, NonPrefixedUnit, MeasurementUnit):
    """
    Class representing the `PracticalSalinityUnit` entity, which inherits from:
    - NonSIUnit, DimensionlessUnit, NonPrefixedUnit, MeasurementUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#PracticalSalinityUnit'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'PracticalSalinityUnit'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `qudtReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `qudtReference`
    
    - `unitSymbol` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `unitSymbol`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = PracticalSalinityUnit(
    
    class_iri='https://w3id.org/emmo#PracticalSalinityUnit',
    
    class_name='PracticalSalinityUnit',
    
    elucidation="example_value",
    
    qudtReference="example_value",
    
    unitSymbol="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        
            'https://w3id.org/emmo#PracticalSalinityUnit',
        
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        
            'PracticalSalinityUnit',
        
        alias="class_name"
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
    


    
    

    

    