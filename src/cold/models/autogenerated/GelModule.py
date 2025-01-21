
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ColloidModule import Colloid



from .SolidMixtureModule import SolidMixture



from .SolidModule import Solid







class Gel(Colloid, SolidMixture, Solid):
    """
    Class representing the `Gel` entity, which inherits from:
    - Colloid, SolidMixture, Solid

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_3995e22d_5720_4dcf_ba3b_d0ce03f514c6'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Gel'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Gel(
    
    class_iri='https://w3id.org/emmo#EMMO_3995e22d_5720_4dcf_ba3b_d0ce03f514c6',
    
    class_name='Gel',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_3995e22d_5720_4dcf_ba3b_d0ce03f514c6',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Gel',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    