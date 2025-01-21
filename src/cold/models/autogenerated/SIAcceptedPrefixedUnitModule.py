
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .PrefixedUnitModule import PrefixedUnit



from .SIAcceptedModule import SIAccepted







class SIAcceptedPrefixedUnit(PrefixedUnit, SIAccepted):
    """
    Class representing the `SIAcceptedPrefixedUnit` entity, which inherits from:
    - PrefixedUnit, SIAccepted

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_93170bc8_d3b2_45bd_8cad_20aad08462ef'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SIAcceptedPrefixedUnit'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SIAcceptedPrefixedUnit(
    
    class_iri='https://w3id.org/emmo#EMMO_93170bc8_d3b2_45bd_8cad_20aad08462ef',
    
    class_name='SIAcceptedPrefixedUnit',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_93170bc8_d3b2_45bd_8cad_20aad08462ef',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SIAcceptedPrefixedUnit',
        alias="class_name"
    )
    

    
    

    

    