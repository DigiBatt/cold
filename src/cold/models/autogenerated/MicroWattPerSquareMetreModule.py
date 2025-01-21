
from pydantic import BaseModel, Field, validator, root_validator
from typing import Optional, List, Union



from .PowerDensityUnitModule import PowerDensityUnit



from .SINonCoherentUnitModule import SINonCoherentUnit



from .MicroPrefixedUnitModule import MicroPrefixedUnit



from .PrefixedUnitModule import PrefixedUnit





from .WattPerSquareMetreModule import WattPerSquareMetre






class MicroWattPerSquareMetre(PowerDensityUnit, SINonCoherentUnit, MicroPrefixedUnit, PrefixedUnit):
    """
    Class representing the `MicroWattPerSquareMetre` entity, which inherits from:
    - PowerDensityUnit, SINonCoherentUnit, MicroPrefixedUnit, PrefixedUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#MicroWattPerSquareMetre'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MicroWattPerSquareMetre'`
        - **Alias**: `class_name`
    
    - `hasUnitSymbol` (`Optional[WattPerSquareMetre]`): 
        - **Default Value**: `None`
        - **Alias**: `hasUnitSymbol`
    
    - `qudtReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `qudtReference`
    
    - `hasSIConversionMultiplier` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSIConversionMultiplier`
    
    - `unitSymbol` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `unitSymbol`
    
    - `hasSIConversionOffset` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSIConversionOffset`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `ucumCode` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `ucumCode`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = MicroWattPerSquareMetre(
    
    class_iri='https://w3id.org/emmo#MicroWattPerSquareMetre',
    
    class_name='MicroWattPerSquareMetre',
    
    hasUnitSymbol="example_value",
    
    qudtReference="example_value",
    
    hasSIConversionMultiplier="example_value",
    
    unitSymbol="example_value",
    
    hasSIConversionOffset="example_value",
    
    elucidation="example_value",
    
    ucumCode="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        
            'https://w3id.org/emmo#MicroWattPerSquareMetre',
        
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        
            'MicroWattPerSquareMetre',
        
        alias="class_name"
    )
    
    hasUnitSymbol: Optional[WattPerSquareMetre] = Field(
        
            None,
        
        alias="hasUnitSymbol"
    )
    
    qudtReference: Optional[str] = Field(
        
            None,
        
        alias="qudtReference"
    )
    
    hasSIConversionMultiplier: Optional[str] = Field(
        
            None,
        
        alias="hasSIConversionMultiplier"
    )
    
    unitSymbol: Optional[str] = Field(
        
            None,
        
        alias="unitSymbol"
    )
    
    hasSIConversionOffset: Optional[str] = Field(
        
            None,
        
        alias="hasSIConversionOffset"
    )
    
    elucidation: Optional[str] = Field(
        
            None,
        
        alias="elucidation"
    )
    
    ucumCode: Optional[str] = Field(
        
            None,
        
        alias="ucumCode"
    )
    


    
    @validator("hasUnitSymbol", pre=True, always=True)
    def validate_hasUnitSymbol(cls, value):
        if value is not None and not isinstance(value, WattPerSquareMetre):
            raise ValueError(f"Field 'hasUnitSymbol' must be an instance of 'WattPerSquareMetre' or its subclass.")
        return value
    
    

    

    