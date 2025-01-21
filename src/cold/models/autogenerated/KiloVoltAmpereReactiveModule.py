
from pydantic import BaseModel, Field, validator, root_validator
from typing import Optional, List, Union



from .NonSIUnitModule import NonSIUnit



from .KiloPrefixedUnitModule import KiloPrefixedUnit



from .PrefixedUnitModule import PrefixedUnit



from .PowerUnitModule import PowerUnit





from .VoltAmpereReactiveModule import VoltAmpereReactive






class KiloVoltAmpereReactive(NonSIUnit, KiloPrefixedUnit, PrefixedUnit, PowerUnit):
    """
    Class representing the `KiloVoltAmpereReactive` entity, which inherits from:
    - NonSIUnit, KiloPrefixedUnit, PrefixedUnit, PowerUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#KiloVoltAmpereReactive'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'KiloVoltAmpereReactive'`
        - **Alias**: `class_name`
    
    - `hasSIConversionMultiplier` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSIConversionMultiplier`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `hasUnitSymbol` (`Optional[VoltAmpereReactive]`): 
        - **Default Value**: `None`
        - **Alias**: `hasUnitSymbol`
    
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
    obj = KiloVoltAmpereReactive(
    
    class_iri='https://w3id.org/emmo#KiloVoltAmpereReactive',
    
    class_name='KiloVoltAmpereReactive',
    
    hasSIConversionMultiplier="example_value",
    
    elucidation="example_value",
    
    hasUnitSymbol="example_value",
    
    qudtReference="example_value",
    
    hasSIConversionOffset="example_value",
    
    unitSymbol="example_value",
    
    ucumCode="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        
            'https://w3id.org/emmo#KiloVoltAmpereReactive',
        
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        
            'KiloVoltAmpereReactive',
        
        alias="class_name"
    )
    
    hasSIConversionMultiplier: Optional[str] = Field(
        
            None,
        
        alias="hasSIConversionMultiplier"
    )
    
    elucidation: Optional[str] = Field(
        
            None,
        
        alias="elucidation"
    )
    
    hasUnitSymbol: Optional[VoltAmpereReactive] = Field(
        
            None,
        
        alias="hasUnitSymbol"
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
    


    
    @validator("hasUnitSymbol", pre=True, always=True)
    def validate_hasUnitSymbol(cls, value):
        if value is not None and not isinstance(value, VoltAmpereReactive):
            raise ValueError(f"Field 'hasUnitSymbol' must be an instance of 'VoltAmpereReactive' or its subclass.")
        return value
    
    

    

    