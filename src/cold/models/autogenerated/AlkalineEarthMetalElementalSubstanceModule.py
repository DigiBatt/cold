
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElementalSubstanceModule import ElementalSubstance







class AlkalineEarthMetalElementalSubstance(ElementalSubstance):
    """
    Class representing the `AlkalineEarthMetalElementalSubstance` entity, which inherits from:
    - ElementalSubstance

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_a4a5b239_d88e_4e03_a763_0bf2a3dd0f47'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'AlkalineEarthMetalElementalSubstance'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = AlkalineEarthMetalElementalSubstance(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_a4a5b239_d88e_4e03_a763_0bf2a3dd0f47',
    
    class_name='AlkalineEarthMetalElementalSubstance',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_a4a5b239_d88e_4e03_a763_0bf2a3dd0f47',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'AlkalineEarthMetalElementalSubstance',
        alias="class_name"
    )
    

    
    

    

    