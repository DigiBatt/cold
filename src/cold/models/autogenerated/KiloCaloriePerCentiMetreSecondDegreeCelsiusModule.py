
from pydantic import BaseModel, Field, validator, root_validator
from typing import Optional, List, Union



from .ThermalConductivityUnitModule import ThermalConductivityUnit



from .NonSIUnitModule import NonSIUnit



from .KiloPrefixedUnitModule import KiloPrefixedUnit



from .PrefixedUnitModule import PrefixedUnit








class KiloCaloriePerCentiMetreSecondDegreeCelsius(ThermalConductivityUnit, NonSIUnit, KiloPrefixedUnit, PrefixedUnit):
    """
    Class representing the `KiloCaloriePerCentiMetreSecondDegreeCelsius` entity, which inherits from:
    - ThermalConductivityUnit, NonSIUnit, KiloPrefixedUnit, PrefixedUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#KiloCaloriePerCentiMetreSecondDegreeCelsius'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'KiloCaloriePerCentiMetreSecondDegreeCelsius'`
        - **Alias**: `class_name`
    
    - `hasSIConversionMultiplier` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSIConversionMultiplier`
    
    - `qudtReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `qudtReference`
    
    - `hasSIConversionOffset` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSIConversionOffset`
    
    - `unitSymbol` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `unitSymbol`
    
    - `ucumCode` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `ucumCode`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = KiloCaloriePerCentiMetreSecondDegreeCelsius(
    
    class_iri='https://w3id.org/emmo#KiloCaloriePerCentiMetreSecondDegreeCelsius',
    
    class_name='KiloCaloriePerCentiMetreSecondDegreeCelsius',
    
    hasSIConversionMultiplier="example_value",
    
    qudtReference="example_value",
    
    hasSIConversionOffset="example_value",
    
    unitSymbol="example_value",
    
    ucumCode="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        
            'https://w3id.org/emmo#KiloCaloriePerCentiMetreSecondDegreeCelsius',
        
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        
            'KiloCaloriePerCentiMetreSecondDegreeCelsius',
        
        alias="class_name"
    )
    
    hasSIConversionMultiplier: Optional[str] = Field(
        
            None,
        
        alias="hasSIConversionMultiplier"
    )
    
    qudtReference: Optional[str] = Field(
        
            None,
        
        alias="qudtReference"
    )
    
    hasSIConversionOffset: Optional[str] = Field(
        
            None,
        
        alias="hasSIConversionOffset"
    )
    
    unitSymbol: Optional[str] = Field(
        
            None,
        
        alias="unitSymbol"
    )
    
    ucumCode: Optional[str] = Field(
        
            None,
        
        alias="ucumCode"
    )
    


    
    

    

    