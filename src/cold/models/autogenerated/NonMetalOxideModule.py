
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .InorganicCompoundModule import InorganicCompound







class NonMetalOxide(InorganicCompound):
    """
    Class representing the `NonMetalOxide` entity, which inherits from:
    - InorganicCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_de2123d1_7ba2_4d3a_837d_a51a5c9170b8'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'NonMetalOxide'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = NonMetalOxide(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_de2123d1_7ba2_4d3a_837d_a51a5c9170b8',
    
    class_name='NonMetalOxide',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_de2123d1_7ba2_4d3a_837d_a51a5c9170b8',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'NonMetalOxide',
        alias="class_name"
    )
    

    
    

    

    