
from pydantic import BaseModel, Field, validator, root_validator
from typing import Optional, List, Union



from .NonSIUnitModule import NonSIUnit



from .MegaPrefixedUnitModule import MegaPrefixedUnit



from .PrefixedUnitModule import PrefixedUnit



from .ForcePerLengthUnitModule import ForcePerLengthUnit





from .PascalSquareRootMeterModule import PascalSquareRootMeter






class MegaPascalSquareRootMeter(NonSIUnit, MegaPrefixedUnit, PrefixedUnit, ForcePerLengthUnit):
    """
    Class representing the `MegaPascalSquareRootMeter` entity, which inherits from:
    - NonSIUnit, MegaPrefixedUnit, PrefixedUnit, ForcePerLengthUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#MegaPascalSquareRootMeter'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MegaPascalSquareRootMeter'`
        - **Alias**: `class_name`
    
    - `hasSIConversionMultiplier` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSIConversionMultiplier`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `hasUnitSymbol` (`Optional[PascalSquareRootMeter]`): 
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
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = MegaPascalSquareRootMeter(
    
    class_iri='https://w3id.org/emmo#MegaPascalSquareRootMeter',
    
    class_name='MegaPascalSquareRootMeter',
    
    hasSIConversionMultiplier="example_value",
    
    elucidation="example_value",
    
    hasUnitSymbol="example_value",
    
    qudtReference="example_value",
    
    hasSIConversionOffset="example_value",
    
    unitSymbol="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        
            'https://w3id.org/emmo#MegaPascalSquareRootMeter',
        
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        
            'MegaPascalSquareRootMeter',
        
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
    
    hasUnitSymbol: Optional[PascalSquareRootMeter] = Field(
        
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
    


    
    @validator("hasUnitSymbol", pre=True, always=True)
    def validate_hasUnitSymbol(cls, value):
        if value is not None and not isinstance(value, PascalSquareRootMeter):
            raise ValueError(f"Field 'hasUnitSymbol' must be an instance of 'PascalSquareRootMeter' or its subclass.")
        return value
    
    

    

    