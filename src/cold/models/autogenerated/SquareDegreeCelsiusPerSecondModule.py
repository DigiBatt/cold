
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SIAcceptedDerivedUnitModule import SIAcceptedDerivedUnit



from .SquareTemperaturePerTimeUnitModule import SquareTemperaturePerTimeUnit







class SquareDegreeCelsiusPerSecond(SIAcceptedDerivedUnit, SquareTemperaturePerTimeUnit):
    """
    Class representing the `SquareDegreeCelsiusPerSecond` entity, which inherits from:
    - SIAcceptedDerivedUnit, SquareTemperaturePerTimeUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#SquareDegreeCelsiusPerSecond'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SquareDegreeCelsiusPerSecond'`
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
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SquareDegreeCelsiusPerSecond(
    
    class_iri='https://w3id.org/emmo#SquareDegreeCelsiusPerSecond',
    
    class_name='SquareDegreeCelsiusPerSecond',
    
    unitSymbol="example_value",
    
    qudtReference="example_value",
    
    ucumCode="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#SquareDegreeCelsiusPerSecond',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SquareDegreeCelsiusPerSecond',
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
    

    
    

    

    