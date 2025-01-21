
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MaterialModule import Material







class NaturalMaterial(Material):
    """
    Class representing the `NaturalMaterial` entity, which inherits from:
    - Material

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_75fe4fd1_0f7e_429b_b91d_59d248561bae'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'NaturalMaterial'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = NaturalMaterial(
    
    class_iri='https://w3id.org/emmo#EMMO_75fe4fd1_0f7e_429b_b91d_59d248561bae',
    
    class_name='NaturalMaterial',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_75fe4fd1_0f7e_429b_b91d_59d248561bae',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'NaturalMaterial',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    