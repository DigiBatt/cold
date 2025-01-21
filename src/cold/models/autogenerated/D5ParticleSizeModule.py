
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .DiameterModule import Diameter







class D5ParticleSize(Diameter):
    """
    Class representing the `D5ParticleSize` entity, which inherits from:
    - Diameter

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_2e2d92f4_9fd5_4965_b15a_30b43c68e3e5'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'D5ParticleSize'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = D5ParticleSize(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_2e2d92f4_9fd5_4965_b15a_30b43c68e3e5',
    
    class_name='D5ParticleSize',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_2e2d92f4_9fd5_4965_b15a_30b43c68e3e5',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'D5ParticleSize',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    