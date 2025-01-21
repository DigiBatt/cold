
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectricChargePerMassUnitModule import ElectricChargePerMassUnit



from .SIAcceptedDerivedUnitModule import SIAcceptedDerivedUnit







class AmpereHourPerKilogram(ElectricChargePerMassUnit, SIAcceptedDerivedUnit):
    """
    Class representing the `AmpereHourPerKilogram` entity, which inherits from:
    - ElectricChargePerMassUnit, SIAcceptedDerivedUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#AmpereHourPerKilogram'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'AmpereHourPerKilogram'`
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
    obj = AmpereHourPerKilogram(
    
    class_iri='https://w3id.org/emmo#AmpereHourPerKilogram',
    
    class_name='AmpereHourPerKilogram',
    
    hasSIConversionMultiplier="example_value",
    
    elucidation="example_value",
    
    hasSIConversionOffset="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#AmpereHourPerKilogram',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'AmpereHourPerKilogram',
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
    

    
    

    

    