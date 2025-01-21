
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElementalSubstanceModule import ElementalSubstance







class TransitionMetalElementalSubstance(ElementalSubstance):
    """
    Class representing the `TransitionMetalElementalSubstance` entity, which inherits from:
    - ElementalSubstance

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_2fc3e95b_6f48_47ea_a366_bcc26336239a'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'TransitionMetalElementalSubstance'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = TransitionMetalElementalSubstance(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_2fc3e95b_6f48_47ea_a366_bcc26336239a',
    
    class_name='TransitionMetalElementalSubstance',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_2fc3e95b_6f48_47ea_a366_bcc26336239a',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'TransitionMetalElementalSubstance',
        alias="class_name"
    )
    

    
    

    

    