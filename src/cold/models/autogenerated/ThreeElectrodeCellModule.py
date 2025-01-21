
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectrochemicalCellModule import ElectrochemicalCell







class ThreeElectrodeCell(ElectrochemicalCell):
    """
    Class representing the `ThreeElectrodeCell` entity, which inherits from:
    - ElectrochemicalCell

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_b9bece97_a511_4cb9_88a2_b5bd5c5e5d74'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ThreeElectrodeCell'`
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
    obj = ThreeElectrodeCell(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_b9bece97_a511_4cb9_88a2_b5bd5c5e5d74',
    
    class_name='ThreeElectrodeCell',
    
    elucidation="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_b9bece97_a511_4cb9_88a2_b5bd5c5e5d74',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ThreeElectrodeCell',
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
    

    
    

    

    