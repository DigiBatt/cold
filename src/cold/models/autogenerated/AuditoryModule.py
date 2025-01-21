
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .PerceptualModule import Perceptual







class Auditory(Perceptual):
    """
    Class representing the `Auditory` entity, which inherits from:
    - Perceptual

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_4b3afb22_27cf_4ce3_88bc_492bfccb546b'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Auditory'`
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
    obj = Auditory(
    
    class_iri='https://w3id.org/emmo#EMMO_4b3afb22_27cf_4ce3_88bc_492bfccb546b',
    
    class_name='Auditory',
    
    elucidation="example_value",
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_4b3afb22_27cf_4ce3_88bc_492bfccb546b',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Auditory',
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
    

    
    

    

    