
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MergingManufacturingModule import MergingManufacturing







class JoinManufacturing(MergingManufacturing):
    """
    Class representing the `JoinManufacturing` entity, which inherits from:
    - MergingManufacturing

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_6ab555fd_5803_4f03_82e8_127c01aabfea'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'JoinManufacturing'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = JoinManufacturing(
    
    class_iri='https://w3id.org/emmo#EMMO_6ab555fd_5803_4f03_82e8_127c01aabfea',
    
    class_name='JoinManufacturing',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_6ab555fd_5803_4f03_82e8_127c01aabfea',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'JoinManufacturing',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    