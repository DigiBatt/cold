
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .BlendedActiveElectrodeModule import BlendedActiveElectrode



from .MetalElectrodeModule import MetalElectrode







class BimetallicElectrode(BlendedActiveElectrode, MetalElectrode):
    """
    Class representing the `BimetallicElectrode` entity, which inherits from:
    - BlendedActiveElectrode, MetalElectrode

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_86be0987_5e21_43ec_b975_8f679999d328'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'BimetallicElectrode'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = BimetallicElectrode(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_86be0987_5e21_43ec_b975_8f679999d328',
    
    class_name='BimetallicElectrode',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_86be0987_5e21_43ec_b975_8f679999d328',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'BimetallicElectrode',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    