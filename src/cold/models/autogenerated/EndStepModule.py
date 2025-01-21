
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .StepModule import Step



from .EndTileModule import EndTile







class EndStep(Step, EndTile):
    """
    Class representing the `EndStep` entity, which inherits from:
    - Step, EndTile

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_8a2a1cbc_dfc3_4e6c_b337_00ee56fd438a'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'EndStep'`
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
    obj = EndStep(
    
    class_iri='https://w3id.org/emmo#EMMO_8a2a1cbc_dfc3_4e6c_b337_00ee56fd438a',
    
    class_name='EndStep',
    
    elucidation="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_8a2a1cbc_dfc3_4e6c_b337_00ee56fd438a',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'EndStep',
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
    

    
    

    

    