
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .NonAqueousElectrolyteModule import NonAqueousElectrolyte







class NonAqueousInorganicElectrolyte(NonAqueousElectrolyte):
    """
    Class representing the `NonAqueousInorganicElectrolyte` entity, which inherits from:
    - NonAqueousElectrolyte

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_addf91e1_ba8c_4a3e_b1e9_092e3e1cc2b3'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'NonAqueousInorganicElectrolyte'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = NonAqueousInorganicElectrolyte(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_addf91e1_ba8c_4a3e_b1e9_092e3e1cc2b3',
    
    class_name='NonAqueousInorganicElectrolyte',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_addf91e1_ba8c_4a3e_b1e9_092e3e1cc2b3',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'NonAqueousInorganicElectrolyte',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    