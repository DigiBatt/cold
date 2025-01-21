
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MatterModule import Matter







class AntiMatter(Matter):
    """
    Class representing the `AntiMatter` entity, which inherits from:
    - Matter

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_f13672a3_59cc_40ed_8def_65009a8f74e6'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'AntiMatter'`
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
    obj = AntiMatter(
    
    class_iri='https://w3id.org/emmo#EMMO_f13672a3_59cc_40ed_8def_65009a8f74e6',
    
    class_name='AntiMatter',
    
    elucidation="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_f13672a3_59cc_40ed_8def_65009a8f74e6',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'AntiMatter',
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
    

    
    

    

    