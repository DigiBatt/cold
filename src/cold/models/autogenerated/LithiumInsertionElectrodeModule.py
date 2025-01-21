
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .InsertionElectrodeModule import InsertionElectrode







class LithiumInsertionElectrode(InsertionElectrode):
    """
    Class representing the `LithiumInsertionElectrode` entity, which inherits from:
    - InsertionElectrode

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_4c3ee364_829b_41a4_b895_ca4a041efb2a'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'LithiumInsertionElectrode'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = LithiumInsertionElectrode(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_4c3ee364_829b_41a4_b895_ca4a041efb2a',
    
    class_name='LithiumInsertionElectrode',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_4c3ee364_829b_41a4_b895_ca4a041efb2a',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'LithiumInsertionElectrode',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    