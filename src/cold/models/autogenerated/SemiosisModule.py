
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SemioticsModule import Semiotics



from .CausalSystemModule import CausalSystem







class Semiosis(Semiotics, CausalSystem):
    """
    Class representing the `Semiosis` entity, which inherits from:
    - Semiotics, CausalSystem

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_008fd3b2_4013_451f_8827_52bceab11841'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Semiosis'`
        - **Alias**: `class_name`
    
    - `example` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `example`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `hasSpatialPart` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSpatialPart`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Semiosis(
    
    class_iri='https://w3id.org/emmo#EMMO_008fd3b2_4013_451f_8827_52bceab11841',
    
    class_name='Semiosis',
    
    example="example_value",
    
    elucidation="example_value",
    
    hasSpatialPart="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_008fd3b2_4013_451f_8827_52bceab11841',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Semiosis',
        alias="class_name"
    )
    
    example: Optional[str] = Field(
        None,
        alias="example"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    hasSpatialPart: Optional[str] = Field(
        None,
        alias="hasSpatialPart"
    )
    

    
    

    

    