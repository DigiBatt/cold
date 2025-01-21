
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .PassivationLayerModule import PassivationLayer







class SolidElectrolyteInterphase(PassivationLayer):
    """
    Class representing the `SolidElectrolyteInterphase` entity, which inherits from:
    - PassivationLayer

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_ecf136cb_2584_4cb1_98b7_2d2b3d22e40d'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SolidElectrolyteInterphase'`
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
    obj = SolidElectrolyteInterphase(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_ecf136cb_2584_4cb1_98b7_2d2b3d22e40d',
    
    class_name='SolidElectrolyteInterphase',
    
    elucidation="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_ecf136cb_2584_4cb1_98b7_2d2b3d22e40d',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SolidElectrolyteInterphase',
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
    

    
    

    

    