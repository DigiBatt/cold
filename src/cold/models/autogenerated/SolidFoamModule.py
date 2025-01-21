
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .FoamModule import Foam



from .SolidMixtureModule import SolidMixture



from .SolidModule import Solid







class SolidFoam(Foam, SolidMixture, Solid):
    """
    Class representing the `SolidFoam` entity, which inherits from:
    - Foam, SolidMixture, Solid

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_9bed5d66_805a_4b3a_9153_beaf67143848'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SolidFoam'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `example` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `example`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SolidFoam(
    
    class_iri='https://w3id.org/emmo#EMMO_9bed5d66_805a_4b3a_9153_beaf67143848',
    
    class_name='SolidFoam',
    
    elucidation="example_value",
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_9bed5d66_805a_4b3a_9153_beaf67143848',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SolidFoam',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    example: Optional[str] = Field(
        None,
        alias="example"
    )
    

    
    

    

    