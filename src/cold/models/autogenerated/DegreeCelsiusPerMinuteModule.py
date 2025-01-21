
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .TemperaturePerTimeUnitModule import TemperaturePerTimeUnit



from .SIAcceptedDerivedUnitModule import SIAcceptedDerivedUnit







class DegreeCelsiusPerMinute(TemperaturePerTimeUnit, SIAcceptedDerivedUnit):
    """
    Class representing the `DegreeCelsiusPerMinute` entity, which inherits from:
    - TemperaturePerTimeUnit, SIAcceptedDerivedUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#DegreeCelsiusPerMinute'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'DegreeCelsiusPerMinute'`
        - **Alias**: `class_name`
    
    - `unitSymbol` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `unitSymbol`
    
    - `qudtReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `qudtReference`
    
    - `ucumCode` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `ucumCode`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = DegreeCelsiusPerMinute(
    
    class_iri='https://w3id.org/emmo#DegreeCelsiusPerMinute',
    
    class_name='DegreeCelsiusPerMinute',
    
    unitSymbol="example_value",
    
    qudtReference="example_value",
    
    ucumCode="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#DegreeCelsiusPerMinute',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'DegreeCelsiusPerMinute',
        alias="class_name"
    )
    
    unitSymbol: Optional[str] = Field(
        None,
        alias="unitSymbol"
    )
    
    qudtReference: Optional[str] = Field(
        None,
        alias="qudtReference"
    )
    
    ucumCode: Optional[str] = Field(
        None,
        alias="ucumCode"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    