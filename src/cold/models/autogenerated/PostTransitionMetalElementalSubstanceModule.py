
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElementalSubstanceModule import ElementalSubstance







class PostTransitionMetalElementalSubstance(ElementalSubstance):
    """
    Class representing the `PostTransitionMetalElementalSubstance` entity, which inherits from:
    - ElementalSubstance

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_b978912b_19ef_4d46_8c91_2e3578b12670'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'PostTransitionMetalElementalSubstance'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = PostTransitionMetalElementalSubstance(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_b978912b_19ef_4d46_8c91_2e3578b12670',
    
    class_name='PostTransitionMetalElementalSubstance',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_b978912b_19ef_4d46_8c91_2e3578b12670',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'PostTransitionMetalElementalSubstance',
        alias="class_name"
    )
    

    
    

    

    