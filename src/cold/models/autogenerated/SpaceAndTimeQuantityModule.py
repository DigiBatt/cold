
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ISO80000CategorisedModule import ISO80000Categorised







class SpaceAndTimeQuantity(ISO80000Categorised):
    """
    Class representing the `SpaceAndTimeQuantity` entity, which inherits from:
    - ISO80000Categorised

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_a242d3e9_c6d3_411e_a667_71ffbc248a1a'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SpaceAndTimeQuantity'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SpaceAndTimeQuantity(
    
    class_iri='https://w3id.org/emmo#EMMO_a242d3e9_c6d3_411e_a667_71ffbc248a1a',
    
    class_name='SpaceAndTimeQuantity',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_a242d3e9_c6d3_411e_a667_71ffbc248a1a',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SpaceAndTimeQuantity',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    