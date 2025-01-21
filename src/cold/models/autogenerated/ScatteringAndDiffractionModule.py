
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CharacterisationTechniqueModule import CharacterisationTechnique







class ScatteringAndDiffraction(CharacterisationTechnique):
    """
    Class representing the `ScatteringAndDiffraction` entity, which inherits from:
    - CharacterisationTechnique

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/characterisation-methodology/chameo#ScatteringAndDiffraction'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ScatteringAndDiffraction'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ScatteringAndDiffraction(
    
    class_iri='https://w3id.org/emmo/domain/characterisation-methodology/chameo#ScatteringAndDiffraction',
    
    class_name='ScatteringAndDiffraction',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/characterisation-methodology/chameo#ScatteringAndDiffraction',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ScatteringAndDiffraction',
        alias="class_name"
    )
    

    
    

    

    