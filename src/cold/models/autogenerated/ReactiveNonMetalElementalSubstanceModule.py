
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElementalSubstanceModule import ElementalSubstance







class ReactiveNonMetalElementalSubstance(ElementalSubstance):
    """
    Class representing the `ReactiveNonMetalElementalSubstance` entity, which inherits from:
    - ElementalSubstance

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_78400dc0_97b0_4d59_8ea6_30bb703f428c'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ReactiveNonMetalElementalSubstance'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ReactiveNonMetalElementalSubstance(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_78400dc0_97b0_4d59_8ea6_30bb703f428c',
    
    class_name='ReactiveNonMetalElementalSubstance',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_78400dc0_97b0_4d59_8ea6_30bb703f428c',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ReactiveNonMetalElementalSubstance',
        alias="class_name"
    )
    

    
    

    

    