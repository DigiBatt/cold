
from pydantic import BaseModel, Field, validator, root_validator
from typing import Optional, List, Union



from .PicoPrefixedUnitModule import PicoPrefixedUnit



from .SINonCoherentUnitModule import SINonCoherentUnit



from .PrefixedUnitModule import PrefixedUnit



from .ElectricCurrentUnitModule import ElectricCurrentUnit





from .AmpereModule import Ampere






class PicoAmpere(PicoPrefixedUnit, SINonCoherentUnit, PrefixedUnit, ElectricCurrentUnit):
    """
    Class representing the `PicoAmpere` entity, which inherits from:
    - PicoPrefixedUnit, SINonCoherentUnit, PrefixedUnit, ElectricCurrentUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#PicoAmpere'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'PicoAmpere'`
        - **Alias**: `class_name`
    
    - `hasSIConversionOffset` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSIConversionOffset`
    
    - `ucumCode` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `ucumCode`
    
    - `qudtReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `qudtReference`
    
    - `unitSymbol` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `unitSymbol`
    
    - `hasSIConversionMultiplier` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSIConversionMultiplier`
    
    - `hasUnitSymbol` (`Optional[Ampere]`): 
        - **Default Value**: `None`
        - **Alias**: `hasUnitSymbol`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = PicoAmpere(
    
    class_iri='https://w3id.org/emmo#PicoAmpere',
    
    class_name='PicoAmpere',
    
    hasSIConversionOffset="example_value",
    
    ucumCode="example_value",
    
    qudtReference="example_value",
    
    unitSymbol="example_value",
    
    hasSIConversionMultiplier="example_value",
    
    hasUnitSymbol="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        
            'https://w3id.org/emmo#PicoAmpere',
        
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        
            'PicoAmpere',
        
        alias="class_name"
    )
    
    hasSIConversionOffset: Optional[str] = Field(
        
            None,
        
        alias="hasSIConversionOffset"
    )
    
    ucumCode: Optional[str] = Field(
        
            None,
        
        alias="ucumCode"
    )
    
    qudtReference: Optional[str] = Field(
        
            None,
        
        alias="qudtReference"
    )
    
    unitSymbol: Optional[str] = Field(
        
            None,
        
        alias="unitSymbol"
    )
    
    hasSIConversionMultiplier: Optional[str] = Field(
        
            None,
        
        alias="hasSIConversionMultiplier"
    )
    
    hasUnitSymbol: Optional[Ampere] = Field(
        
            None,
        
        alias="hasUnitSymbol"
    )
    


    
    @validator("hasUnitSymbol", pre=True, always=True)
    def validate_hasUnitSymbol(cls, value):
        if value is not None and not isinstance(value, Ampere):
            raise ValueError(f"Field 'hasUnitSymbol' must be an instance of 'Ampere' or its subclass.")
        return value
    
    

    

    