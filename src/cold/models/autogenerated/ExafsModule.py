
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SpectroscopyModule import Spectroscopy







class Exafs(Spectroscopy):
    """
    Class representing the `Exafs` entity, which inherits from:
    - Spectroscopy

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/characterisation-methodology/chameo#Exafs'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Exafs'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Exafs(
    
    class_iri='https://w3id.org/emmo/domain/characterisation-methodology/chameo#Exafs',
    
    class_name='Exafs',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/characterisation-methodology/chameo#Exafs',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Exafs',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    