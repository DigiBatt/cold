
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MassTemperatureUnitModule import MassTemperatureUnit



from .SIAcceptedDerivedUnitModule import SIAcceptedDerivedUnit







class GramDegreeCelsius(MassTemperatureUnit, SIAcceptedDerivedUnit):
    """
    Class representing the `GramDegreeCelsius` entity, which inherits from:
    - MassTemperatureUnit, SIAcceptedDerivedUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#GramDegreeCelsius'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'GramDegreeCelsius'`
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
    obj = GramDegreeCelsius(
    
    class_iri='https://w3id.org/emmo#GramDegreeCelsius',
    
    class_name='GramDegreeCelsius',
    
    unitSymbol="example_value",
    
    qudtReference="example_value",
    
    ucumCode="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#GramDegreeCelsius',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'GramDegreeCelsius',
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
    

    
    

    

    