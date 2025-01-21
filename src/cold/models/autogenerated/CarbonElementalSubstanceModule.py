
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElementalSubstanceModule import ElementalSubstance







class CarbonElementalSubstance(ElementalSubstance):
    """
    Class representing the `CarbonElementalSubstance` entity, which inherits from:
    - ElementalSubstance

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_6c0cc397_d8c4_4473_a09f_1e5de568e0dd'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CarbonElementalSubstance'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = CarbonElementalSubstance(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_6c0cc397_d8c4_4473_a09f_1e5de568e0dd',
    
    class_name='CarbonElementalSubstance',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_6c0cc397_d8c4_4473_a09f_1e5de568e0dd',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CarbonElementalSubstance',
        alias="class_name"
    )
    

    
    

    

    