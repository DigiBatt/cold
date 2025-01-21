
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SINonCoherentDerivedUnitModule import SINonCoherentDerivedUnit



from .ElectricCurrentPerMassUnitModule import ElectricCurrentPerMassUnit







class AmperePerGram(SINonCoherentDerivedUnit, ElectricCurrentPerMassUnit):
    """
    Class representing the `AmperePerGram` entity, which inherits from:
    - SINonCoherentDerivedUnit, ElectricCurrentPerMassUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#AmperePerGram'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'AmperePerGram'`
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
    obj = AmperePerGram(
    
    class_iri='https://w3id.org/emmo#AmperePerGram',
    
    class_name='AmperePerGram',
    
    hasSIConversionMultiplier="example_value",
    
    elucidation="example_value",
    
    hasSIConversionOffset="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#AmperePerGram',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'AmperePerGram',
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
    

    
    

    

    