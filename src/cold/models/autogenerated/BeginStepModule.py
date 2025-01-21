
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .StepModule import Step



from .BeginTileModule import BeginTile







class BeginStep(Step, BeginTile):
    """
    Class representing the `BeginStep` entity, which inherits from:
    - Step, BeginTile

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_b941e455_2cb1_4c11_93e3_17caa06086b4'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'BeginStep'`
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
    obj = BeginStep(
    
    class_iri='https://w3id.org/emmo#EMMO_b941e455_2cb1_4c11_93e3_17caa06086b4',
    
    class_name='BeginStep',
    
    elucidation="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_b941e455_2cb1_4c11_93e3_17caa06086b4',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'BeginStep',
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
    

    
    

    

    