
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MatterModule import Matter







class HybridMatter(Matter):
    """
    Class representing the `HybridMatter` entity, which inherits from:
    - Matter

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_1c16bb7f_5400_4498_8ef2_54392908da4e'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'HybridMatter'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = HybridMatter(
    
    class_iri='https://w3id.org/emmo#EMMO_1c16bb7f_5400_4498_8ef2_54392908da4e',
    
    class_name='HybridMatter',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_1c16bb7f_5400_4498_8ef2_54392908da4e',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'HybridMatter',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    