
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .PressureUnitModule import PressureUnit



from .SIAcceptedDerivedUnitModule import SIAcceptedDerivedUnit







class WattHourPerLitre(PressureUnit, SIAcceptedDerivedUnit):
    """
    Class representing the `WattHourPerLitre` entity, which inherits from:
    - PressureUnit, SIAcceptedDerivedUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#WattHourPerLitre'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'WattHourPerLitre'`
        - **Alias**: `class_name`
    
    - `hasSIConversionMultiplier` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSIConversionMultiplier`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `hasSIConversionOffset` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSIConversionOffset`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = WattHourPerLitre(
    
    class_iri='https://w3id.org/emmo#WattHourPerLitre',
    
    class_name='WattHourPerLitre',
    
    hasSIConversionMultiplier="example_value",
    
    elucidation="example_value",
    
    hasSIConversionOffset="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#WattHourPerLitre',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'WattHourPerLitre',
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
    
    hasSIConversionOffset: Optional[str] = Field(
        None,
        alias="hasSIConversionOffset"
    )
    

    
    

    

    