
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ArchetypeJoinModule import ArchetypeJoin



from .FormingFromPlasticModule import FormingFromPlastic







class InjectionMolding(ArchetypeJoin, FormingFromPlastic):
    """
    Class representing the `InjectionMolding` entity, which inherits from:
    - ArchetypeJoin, FormingFromPlastic

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_4d5053a7_273e_495b_8098_5aa5c0f3f925'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'InjectionMolding'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = InjectionMolding(
    
    class_iri='https://w3id.org/emmo#EMMO_4d5053a7_273e_495b_8098_5aa5c0f3f925',
    
    class_name='InjectionMolding',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_4d5053a7_273e_495b_8098_5aa5c0f3f925',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'InjectionMolding',
        alias="class_name"
    )
    

    
    

    

    