
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SulfurBasedElectrodeModule import SulfurBasedElectrode







class ThionylChlorideElectrode(SulfurBasedElectrode):
    """
    Class representing the `ThionylChlorideElectrode` entity, which inherits from:
    - SulfurBasedElectrode

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_4977521c_0438_4659_bc81_1c77fae836bb'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ThionylChlorideElectrode'`
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
    obj = ThionylChlorideElectrode(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_4977521c_0438_4659_bc81_1c77fae836bb',
    
    class_name='ThionylChlorideElectrode',
    
    elucidation="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_4977521c_0438_4659_bc81_1c77fae836bb',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ThionylChlorideElectrode',
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
    

    
    

    

    