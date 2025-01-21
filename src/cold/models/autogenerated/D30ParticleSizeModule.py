
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .DiameterModule import Diameter







class D30ParticleSize(Diameter):
    """
    Class representing the `D30ParticleSize` entity, which inherits from:
    - Diameter

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_0ed0362e_b7ae_482c_a7d0_2ca2eebda648'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'D30ParticleSize'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = D30ParticleSize(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_0ed0362e_b7ae_482c_a7d0_2ca2eebda648',
    
    class_name='D30ParticleSize',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_0ed0362e_b7ae_482c_a7d0_2ca2eebda648',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'D30ParticleSize',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    