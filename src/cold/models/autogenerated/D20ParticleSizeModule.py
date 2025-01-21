
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .DiameterModule import Diameter







class D20ParticleSize(Diameter):
    """
    Class representing the `D20ParticleSize` entity, which inherits from:
    - Diameter

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_62e03250_8987_497b_85d5_1399aca9a0aa'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'D20ParticleSize'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = D20ParticleSize(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_62e03250_8987_497b_85d5_1399aca9a0aa',
    
    class_name='D20ParticleSize',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_62e03250_8987_497b_85d5_1399aca9a0aa',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'D20ParticleSize',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    