
from pydantic import BaseModel, Field, validator, root_validator
from typing import Optional, List, Union



from .ElectricChargePerMassUnitModule import ElectricChargePerMassUnit



from .KiloPrefixedUnitModule import KiloPrefixedUnit



from .SINonCoherentUnitModule import SINonCoherentUnit



from .PrefixedUnitModule import PrefixedUnit





from .RoentgenModule import Roentgen






class KiloRoentgen(ElectricChargePerMassUnit, KiloPrefixedUnit, SINonCoherentUnit, PrefixedUnit):
    """
    Class representing the `KiloRoentgen` entity, which inherits from:
    - ElectricChargePerMassUnit, KiloPrefixedUnit, SINonCoherentUnit, PrefixedUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#KiloRoentgen'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'KiloRoentgen'`
        - **Alias**: `class_name`
    
    - `hasUnitSymbol` (`Optional[Roentgen]`): 
        - **Default Value**: `None`
        - **Alias**: `hasUnitSymbol`
    
    - `hasSIConversionOffset` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSIConversionOffset`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `qudtReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `qudtReference`
    
    - `unitSymbol` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `unitSymbol`
    
    - `ucumCode` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `ucumCode`
    
    - `hasSIConversionMultiplier` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSIConversionMultiplier`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = KiloRoentgen(
    
    class_iri='https://w3id.org/emmo#KiloRoentgen',
    
    class_name='KiloRoentgen',
    
    hasUnitSymbol="example_value",
    
    hasSIConversionOffset="example_value",
    
    elucidation="example_value",
    
    qudtReference="example_value",
    
    unitSymbol="example_value",
    
    ucumCode="example_value",
    
    hasSIConversionMultiplier="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        
            'https://w3id.org/emmo#KiloRoentgen',
        
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        
            'KiloRoentgen',
        
        alias="class_name"
    )
    
    hasUnitSymbol: Optional[Roentgen] = Field(
        
            None,
        
        alias="hasUnitSymbol"
    )
    
    hasSIConversionOffset: Optional[str] = Field(
        
            None,
        
        alias="hasSIConversionOffset"
    )
    
    elucidation: Optional[str] = Field(
        
            None,
        
        alias="elucidation"
    )
    
    qudtReference: Optional[str] = Field(
        
            None,
        
        alias="qudtReference"
    )
    
    unitSymbol: Optional[str] = Field(
        
            None,
        
        alias="unitSymbol"
    )
    
    ucumCode: Optional[str] = Field(
        
            None,
        
        alias="ucumCode"
    )
    
    hasSIConversionMultiplier: Optional[str] = Field(
        
            None,
        
        alias="hasSIConversionMultiplier"
    )
    


    
    @validator("hasUnitSymbol", pre=True, always=True)
    def validate_hasUnitSymbol(cls, value):
        if value is not None and not isinstance(value, Roentgen):
            raise ValueError(f"Field 'hasUnitSymbol' must be an instance of 'Roentgen' or its subclass.")
        return value
    
    

    

    