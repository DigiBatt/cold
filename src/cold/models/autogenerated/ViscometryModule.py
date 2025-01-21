
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CharacterisationTechniqueModule import CharacterisationTechnique







class Viscometry(CharacterisationTechnique):
    """
    Class representing the `Viscometry` entity, which inherits from:
    - CharacterisationTechnique

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/characterisation-methodology/chameo#Viscometry'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Viscometry'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Viscometry(
    
    class_iri='https://w3id.org/emmo/domain/characterisation-methodology/chameo#Viscometry',
    
    class_name='Viscometry',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/characterisation-methodology/chameo#Viscometry',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Viscometry',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    