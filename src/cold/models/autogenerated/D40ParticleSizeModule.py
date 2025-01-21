
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .DiameterModule import Diameter







class D40ParticleSize(Diameter):
    """
    Class representing the `D40ParticleSize` entity, which inherits from:
    - Diameter

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_c8abaf09_300a_4008_a42a_2f4a3953ca7a'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'D40ParticleSize'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = D40ParticleSize(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_c8abaf09_300a_4008_a42a_2f4a3953ca7a',
    
    class_name='D40ParticleSize',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_c8abaf09_300a_4008_a42a_2f4a3953ca7a',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'D40ParticleSize',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    