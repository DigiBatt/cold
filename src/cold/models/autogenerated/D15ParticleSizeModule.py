
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .DiameterModule import Diameter







class D15ParticleSize(Diameter):
    """
    Class representing the `D15ParticleSize` entity, which inherits from:
    - Diameter

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_92fc0dba_6f11_4019_a8cb_db2a5b1634f5'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'D15ParticleSize'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = D15ParticleSize(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_92fc0dba_6f11_4019_a8cb_db2a5b1634f5',
    
    class_name='D15ParticleSize',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_92fc0dba_6f11_4019_a8cb_db2a5b1634f5',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'D15ParticleSize',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    