
from pydantic import BaseModel, Field, validator, root_validator
from typing import Optional, List, Union



from .TimeUnitModule import TimeUnit



from .NonSIUnitModule import NonSIUnit



from .NonPrefixedUnitModule import NonPrefixedUnit



from .MeasurementUnitModule import MeasurementUnit








class SynodicMonth(TimeUnit, NonSIUnit, NonPrefixedUnit, MeasurementUnit):
    """
    Class representing the `SynodicMonth` entity, which inherits from:
    - TimeUnit, NonSIUnit, NonPrefixedUnit, MeasurementUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#SynodicMonth'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SynodicMonth'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `qudtReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `qudtReference`
    
    - `ucumCode` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `ucumCode`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SynodicMonth(
    
    class_iri='https://w3id.org/emmo#SynodicMonth',
    
    class_name='SynodicMonth',
    
    elucidation="example_value",
    
    qudtReference="example_value",
    
    ucumCode="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        
            'https://w3id.org/emmo#SynodicMonth',
        
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        
            'SynodicMonth',
        
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
    
    ucumCode: Optional[str] = Field(
        
            None,
        
        alias="ucumCode"
    )
    


    
    

    

    