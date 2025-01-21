
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectrochemicalDeviceModule import ElectrochemicalDevice







class FlowCell(ElectrochemicalDevice):
    """
    Class representing the `FlowCell` entity, which inherits from:
    - ElectrochemicalDevice

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_95e4aa95_b7e9_40d7_b78e_4d7dcc31093d'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'FlowCell'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = FlowCell(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_95e4aa95_b7e9_40d7_b78e_4d7dcc31093d',
    
    class_name='FlowCell',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_95e4aa95_b7e9_40d7_b78e_4d7dcc31093d',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'FlowCell',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    