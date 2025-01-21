
from pydantic import BaseModel, Field, validator, root_validator
from typing import Optional, List, Union



from .NonSIUnitModule import NonSIUnit



from .LengthTimeTemperatureUnitModule import LengthTimeTemperatureUnit



from .CentiPrefixedUnitModule import CentiPrefixedUnit



from .PrefixedUnitModule import PrefixedUnit








class CentiMetreSecondDegreeCelsius(NonSIUnit, LengthTimeTemperatureUnit, CentiPrefixedUnit, PrefixedUnit):
    """
    Class representing the `CentiMetreSecondDegreeCelsius` entity, which inherits from:
    - NonSIUnit, LengthTimeTemperatureUnit, CentiPrefixedUnit, PrefixedUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#CentiMetreSecondDegreeCelsius'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CentiMetreSecondDegreeCelsius'`
        - **Alias**: `class_name`
    
    - `qudtReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `qudtReference`
    
    - `unitSymbol` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `unitSymbol`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `ucumCode` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `ucumCode`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = CentiMetreSecondDegreeCelsius(
    
    class_iri='https://w3id.org/emmo#CentiMetreSecondDegreeCelsius',
    
    class_name='CentiMetreSecondDegreeCelsius',
    
    qudtReference="example_value",
    
    unitSymbol="example_value",
    
    elucidation="example_value",
    
    ucumCode="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        
            'https://w3id.org/emmo#CentiMetreSecondDegreeCelsius',
        
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        
            'CentiMetreSecondDegreeCelsius',
        
        alias="class_name"
    )
    
    qudtReference: Optional[str] = Field(
        
            None,
        
        alias="qudtReference"
    )
    
    unitSymbol: Optional[str] = Field(
        
            None,
        
        alias="unitSymbol"
    )
    
    elucidation: Optional[str] = Field(
        
            None,
        
        alias="elucidation"
    )
    
    ucumCode: Optional[str] = Field(
        
            None,
        
        alias="ucumCode"
    )
    


    
    

    

    