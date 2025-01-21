
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .TechnologyProcessModule import TechnologyProcess







class MaterialsProcessing(TechnologyProcess):
    """
    Class representing the `MaterialsProcessing` entity, which inherits from:
    - TechnologyProcess

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_71d1c8f0_c6e3_44b5_a4b6_1b74ff35698a'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MaterialsProcessing'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `example` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `example`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = MaterialsProcessing(
    
    class_iri='https://w3id.org/emmo#EMMO_71d1c8f0_c6e3_44b5_a4b6_1b74ff35698a',
    
    class_name='MaterialsProcessing',
    
    elucidation="example_value",
    
    example="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_71d1c8f0_c6e3_44b5_a4b6_1b74ff35698a',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MaterialsProcessing',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    example: Optional[str] = Field(
        None,
        alias="example"
    )
    
    comment: Optional[str] = Field(
        None,
        alias="comment"
    )
    

    
    

    

    