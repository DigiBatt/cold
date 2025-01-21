
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .FormingFromPowderModule import FormingFromPowder







class SandMolds(FormingFromPowder):
    """
    Class representing the `SandMolds` entity, which inherits from:
    - FormingFromPowder

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_2bf617c6_e57b_430b_9f37_fcf2cfda719e'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SandMolds'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SandMolds(
    
    class_iri='https://w3id.org/emmo#EMMO_2bf617c6_e57b_430b_9f37_fcf2cfda719e',
    
    class_name='SandMolds',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_2bf617c6_e57b_430b_9f37_fcf2cfda719e',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SandMolds',
        alias="class_name"
    )
    

    
    

    

    