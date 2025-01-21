
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CondensedMatterModule import CondensedMatter



from .FluidModule import Fluid







class Liquid(CondensedMatter, Fluid):
    """
    Class representing the `Liquid` entity, which inherits from:
    - CondensedMatter, Fluid

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_7509da43_56b1_4d7f_887a_65d1663df4ba'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Liquid'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Liquid(
    
    class_iri='https://w3id.org/emmo#EMMO_7509da43_56b1_4d7f_887a_65d1663df4ba',
    
    class_name='Liquid',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_7509da43_56b1_4d7f_887a_65d1663df4ba',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Liquid',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    