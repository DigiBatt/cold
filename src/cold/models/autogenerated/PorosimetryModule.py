
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CharacterisationTechniqueModule import CharacterisationTechnique







class Porosimetry(CharacterisationTechnique):
    """
    Class representing the `Porosimetry` entity, which inherits from:
    - CharacterisationTechnique

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/characterisation-methodology/chameo#Porosimetry'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Porosimetry'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Porosimetry(
    
    class_iri='https://w3id.org/emmo/domain/characterisation-methodology/chameo#Porosimetry',
    
    class_name='Porosimetry',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/characterisation-methodology/chameo#Porosimetry',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Porosimetry',
        alias="class_name"
    )
    

    
    

    

    