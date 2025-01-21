
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .InsertionElectrodeModule import InsertionElectrode







class ProtonInsertionElectrode(InsertionElectrode):
    """
    Class representing the `ProtonInsertionElectrode` entity, which inherits from:
    - InsertionElectrode

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_11a774f3_d20a_4741_bd81_cae53230bd0c'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ProtonInsertionElectrode'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ProtonInsertionElectrode(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_11a774f3_d20a_4741_bd81_cae53230bd0c',
    
    class_name='ProtonInsertionElectrode',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_11a774f3_d20a_4741_bd81_cae53230bd0c',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ProtonInsertionElectrode',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    