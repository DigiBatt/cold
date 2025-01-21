
from pydantic import BaseModel, Field, validator, root_validator
from typing import Optional, List, Union



from .NonSIUnitModule import NonSIUnit



from .TemperaturePerTimeUnitModule import TemperaturePerTimeUnit



from .NonPrefixedUnitModule import NonPrefixedUnit



from .MeasurementUnitModule import MeasurementUnit








class DegreeFahrenheitPerHour(NonSIUnit, TemperaturePerTimeUnit, NonPrefixedUnit, MeasurementUnit):
    """
    Class representing the `DegreeFahrenheitPerHour` entity, which inherits from:
    - NonSIUnit, TemperaturePerTimeUnit, NonPrefixedUnit, MeasurementUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#DegreeFahrenheitPerHour'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'DegreeFahrenheitPerHour'`
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
    
    - `ucumCode` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `ucumCode`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = DegreeFahrenheitPerHour(
    
    class_iri='https://w3id.org/emmo#DegreeFahrenheitPerHour',
    
    class_name='DegreeFahrenheitPerHour',
    
    elucidation="example_value",
    
    qudtReference="example_value",
    
    unitSymbol="example_value",
    
    ucumCode="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        
            'https://w3id.org/emmo#DegreeFahrenheitPerHour',
        
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        
            'DegreeFahrenheitPerHour',
        
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
    
    ucumCode: Optional[str] = Field(
        
            None,
        
        alias="ucumCode"
    )
    


    
    

    

    