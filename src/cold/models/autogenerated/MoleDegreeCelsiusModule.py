
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .NonSIUnitModule import NonSIUnit



from .AmountTemperatureUnitModule import AmountTemperatureUnit



from .SIAcceptedDerivedUnitModule import SIAcceptedDerivedUnit



from .NonPrefixedUnitModule import NonPrefixedUnit







class MoleDegreeCelsius(NonSIUnit, AmountTemperatureUnit, SIAcceptedDerivedUnit, NonPrefixedUnit):
    """
    Class representing the `MoleDegreeCelsius` entity, which inherits from:
    - NonSIUnit, AmountTemperatureUnit, SIAcceptedDerivedUnit, NonPrefixedUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#MoleDegreeCelsius'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MoleDegreeCelsius'`
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
    obj = MoleDegreeCelsius(
    
    class_iri='https://w3id.org/emmo#MoleDegreeCelsius',
    
    class_name='MoleDegreeCelsius',
    
    unitSymbol="example_value",
    
    qudtReference="example_value",
    
    ucumCode="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#MoleDegreeCelsius',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MoleDegreeCelsius',
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
    

    
    

    

    