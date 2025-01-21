
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .DerivedUnitModule import DerivedUnit



from .SIAcceptedModule import SIAccepted







class SIAcceptedDerivedUnit(DerivedUnit, SIAccepted):
    """
    Class representing the `SIAcceptedDerivedUnit` entity, which inherits from:
    - DerivedUnit, SIAccepted

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_ac19c801_bead_4730_8b8c_50020eec45ec'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SIAcceptedDerivedUnit'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SIAcceptedDerivedUnit(
    
    class_iri='https://w3id.org/emmo#EMMO_ac19c801_bead_4730_8b8c_50020eec45ec',
    
    class_name='SIAcceptedDerivedUnit',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_ac19c801_bead_4730_8b8c_50020eec45ec',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SIAcceptedDerivedUnit',
        alias="class_name"
    )
    

    
    

    

    