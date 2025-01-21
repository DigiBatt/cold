
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .OrdinaryMatterModule import OrdinaryMatter



from .SubstanceModule import Substance







class Material(OrdinaryMatter, Substance):
    """
    Class representing the `Material` entity, which inherits from:
    - OrdinaryMatter, Substance

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_4207e895_8b83_4318_996a_72cfb32acd94'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Material'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Material(
    
    class_iri='https://w3id.org/emmo#EMMO_4207e895_8b83_4318_996a_72cfb32acd94',
    
    class_name='Material',
    
    elucidation="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_4207e895_8b83_4318_996a_72cfb32acd94',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Material',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    comment: Optional[str] = Field(
        None,
        alias="comment"
    )
    

    
    

    

    