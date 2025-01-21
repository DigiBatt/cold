
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .FormingFromPulpModule import FormingFromPulp







class PorcelainOrCeramicCasting(FormingFromPulp):
    """
    Class representing the `PorcelainOrCeramicCasting` entity, which inherits from:
    - FormingFromPulp

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_d320f878_2be4_4927_aea6_d36a2ae2dd89'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'PorcelainOrCeramicCasting'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = PorcelainOrCeramicCasting(
    
    class_iri='https://w3id.org/emmo#EMMO_d320f878_2be4_4927_aea6_d36a2ae2dd89',
    
    class_name='PorcelainOrCeramicCasting',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_d320f878_2be4_4927_aea6_d36a2ae2dd89',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'PorcelainOrCeramicCasting',
        alias="class_name"
    )
    

    
    

    

    