
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .IntentionalProcessModule import IntentionalProcess







class ElectrochemicalMethod(IntentionalProcess):
    """
    Class representing the `ElectrochemicalMethod` entity, which inherits from:
    - IntentionalProcess

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_f49b84d4_e1f9_424c_bb22_8cea23c0a7d4'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ElectrochemicalMethod'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ElectrochemicalMethod(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_f49b84d4_e1f9_424c_bb22_8cea23c0a7d4',
    
    class_name='ElectrochemicalMethod',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_f49b84d4_e1f9_424c_bb22_8cea23c0a7d4',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ElectrochemicalMethod',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    