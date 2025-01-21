
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CharacterisationTechniqueModule import CharacterisationTechnique







class ChargeDistribution(CharacterisationTechnique):
    """
    Class representing the `ChargeDistribution` entity, which inherits from:
    - CharacterisationTechnique

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/characterisation-methodology/chameo#ChargeDistribution'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ChargeDistribution'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ChargeDistribution(
    
    class_iri='https://w3id.org/emmo/domain/characterisation-methodology/chameo#ChargeDistribution',
    
    class_name='ChargeDistribution',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/characterisation-methodology/chameo#ChargeDistribution',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ChargeDistribution',
        alias="class_name"
    )
    

    
    

    

    