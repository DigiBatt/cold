
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SINonCoherentDerivedUnitModule import SINonCoherentDerivedUnit



from .SIAcceptedDerivedUnitModule import SIAcceptedDerivedUnit



from .PressurePerTimeUnitModule import PressurePerTimeUnit







class WattPerLitre(SINonCoherentDerivedUnit, SIAcceptedDerivedUnit, PressurePerTimeUnit):
    """
    Class representing the `WattPerLitre` entity, which inherits from:
    - SINonCoherentDerivedUnit, SIAcceptedDerivedUnit, PressurePerTimeUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#WattPerLitre'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'WattPerLitre'`
        - **Alias**: `class_name`
    
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
    obj = WattPerLitre(
    
    class_iri='https://w3id.org/emmo#WattPerLitre',
    
    class_name='WattPerLitre',
    
    elucidation="example_value",
    
    hasSIConversionOffset="example_value",
    
    hasSIConversionMultiplier="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#WattPerLitre',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'WattPerLitre',
        alias="class_name"
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
    

    
    

    

    