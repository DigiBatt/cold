
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SeparatorModule import Separator







class AsymmetricMembrane(Separator):
    """
    Class representing the `AsymmetricMembrane` entity, which inherits from:
    - Separator

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_b2d11f0d_c1b0_4476_8d17_03b73d31e01f'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'AsymmetricMembrane'`
        - **Alias**: `class_name`
    
    - `wikidataReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikidataReference`
    
    - `iupacReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `iupacReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = AsymmetricMembrane(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_b2d11f0d_c1b0_4476_8d17_03b73d31e01f',
    
    class_name='AsymmetricMembrane',
    
    wikidataReference="example_value",
    
    iupacReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_b2d11f0d_c1b0_4476_8d17_03b73d31e01f',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'AsymmetricMembrane',
        alias="class_name"
    )
    
    wikidataReference: Optional[str] = Field(
        None,
        alias="wikidataReference"
    )
    
    iupacReference: Optional[str] = Field(
        None,
        alias="iupacReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    