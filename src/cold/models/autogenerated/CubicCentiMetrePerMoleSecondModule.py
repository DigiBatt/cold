
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SINonCoherentDerivedUnitModule import SINonCoherentDerivedUnit



from .VolumePerAmountTimeUnitModule import VolumePerAmountTimeUnit







class CubicCentiMetrePerMoleSecond(SINonCoherentDerivedUnit, VolumePerAmountTimeUnit):
    """
    Class representing the `CubicCentiMetrePerMoleSecond` entity, which inherits from:
    - SINonCoherentDerivedUnit, VolumePerAmountTimeUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#CubicCentiMetrePerMoleSecond'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CubicCentiMetrePerMoleSecond'`
        - **Alias**: `class_name`
    
    - `unitSymbol` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `unitSymbol`
    
    - `qudtReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `qudtReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `hasSIConversionOffset` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSIConversionOffset`
    
    - `hasSIConversionMultiplier` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSIConversionMultiplier`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = CubicCentiMetrePerMoleSecond(
    
    class_iri='https://w3id.org/emmo#CubicCentiMetrePerMoleSecond',
    
    class_name='CubicCentiMetrePerMoleSecond',
    
    unitSymbol="example_value",
    
    qudtReference="example_value",
    
    elucidation="example_value",
    
    hasSIConversionOffset="example_value",
    
    hasSIConversionMultiplier="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#CubicCentiMetrePerMoleSecond',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CubicCentiMetrePerMoleSecond',
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
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    hasSIConversionOffset: Optional[str] = Field(
        None,
        alias="hasSIConversionOffset"
    )
    
    hasSIConversionMultiplier: Optional[str] = Field(
        None,
        alias="hasSIConversionMultiplier"
    )
    

    
    

    

    