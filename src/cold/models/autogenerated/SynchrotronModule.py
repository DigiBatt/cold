
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ScatteringAndDiffractionModule import ScatteringAndDiffraction







class Synchrotron(ScatteringAndDiffraction):
    """
    Class representing the `Synchrotron` entity, which inherits from:
    - ScatteringAndDiffraction

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/characterisation-methodology/chameo#Synchrotron'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Synchrotron'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Synchrotron(
    
    class_iri='https://w3id.org/emmo/domain/characterisation-methodology/chameo#Synchrotron',
    
    class_name='Synchrotron',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/characterisation-methodology/chameo#Synchrotron',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Synchrotron',
        alias="class_name"
    )
    

    
    

    

    