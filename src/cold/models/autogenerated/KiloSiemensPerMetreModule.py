
from pydantic import BaseModel, Field, validator, root_validator
from typing import Optional, List, Union



from .KiloPrefixedUnitModule import KiloPrefixedUnit



from .SINonCoherentUnitModule import SINonCoherentUnit



from .ElectricConductivityUnitModule import ElectricConductivityUnit



from .PrefixedUnitModule import PrefixedUnit





from .SiemensPerMetreModule import SiemensPerMetre






class KiloSiemensPerMetre(KiloPrefixedUnit, SINonCoherentUnit, ElectricConductivityUnit, PrefixedUnit):
    """
    Class representing the `KiloSiemensPerMetre` entity, which inherits from:
    - KiloPrefixedUnit, SINonCoherentUnit, ElectricConductivityUnit, PrefixedUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#KiloSiemensPerMetre'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'KiloSiemensPerMetre'`
        - **Alias**: `class_name`
    
    - `hasUnitSymbol` (`Optional[SiemensPerMetre]`): 
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
    obj = KiloSiemensPerMetre(
    
    class_iri='https://w3id.org/emmo#KiloSiemensPerMetre',
    
    class_name='KiloSiemensPerMetre',
    
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
        
            'https://w3id.org/emmo#KiloSiemensPerMetre',
        
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        
            'KiloSiemensPerMetre',
        
        alias="class_name"
    )
    
    hasUnitSymbol: Optional[SiemensPerMetre] = Field(
        
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
        if value is not None and not isinstance(value, SiemensPerMetre):
            raise ValueError(f"Field 'hasUnitSymbol' must be an instance of 'SiemensPerMetre' or its subclass.")
        return value
    
    

    

    