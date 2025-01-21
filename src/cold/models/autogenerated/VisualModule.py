
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .PerceptualModule import Perceptual







class Visual(Perceptual):
    """
    Class representing the `Visual` entity, which inherits from:
    - Perceptual

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_c5ae6d8e_6b39_431f_8de4_ae4e357abc04'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Visual'`
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
    obj = Visual(
    
    class_iri='https://w3id.org/emmo#EMMO_c5ae6d8e_6b39_431f_8de4_ae4e357abc04',
    
    class_name='Visual',
    
    elucidation="example_value",
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_c5ae6d8e_6b39_431f_8de4_ae4e357abc04',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Visual',
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
    

    
    

    

    