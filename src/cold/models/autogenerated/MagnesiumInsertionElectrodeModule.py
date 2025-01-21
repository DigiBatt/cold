
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .InsertionElectrodeModule import InsertionElectrode







class MagnesiumInsertionElectrode(InsertionElectrode):
    """
    Class representing the `MagnesiumInsertionElectrode` entity, which inherits from:
    - InsertionElectrode

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_d9888f1f_2226_4ce3_9cb3_91fd9bd1bf22'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MagnesiumInsertionElectrode'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = MagnesiumInsertionElectrode(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_d9888f1f_2226_4ce3_9cb3_91fd9bd1bf22',
    
    class_name='MagnesiumInsertionElectrode',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_d9888f1f_2226_4ce3_9cb3_91fd9bd1bf22',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MagnesiumInsertionElectrode',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    