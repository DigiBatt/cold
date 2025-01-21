
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CoatedElectrodeModule import CoatedElectrode







class DoubleCoatedElectrode(CoatedElectrode):
    """
    Class representing the `DoubleCoatedElectrode` entity, which inherits from:
    - CoatedElectrode

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_56f85b19_1384_4e88_b130_cb8e7984db83'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'DoubleCoatedElectrode'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = DoubleCoatedElectrode(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_56f85b19_1384_4e88_b130_cb8e7984db83',
    
    class_name='DoubleCoatedElectrode',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_56f85b19_1384_4e88_b130_cb8e7984db83',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'DoubleCoatedElectrode',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    