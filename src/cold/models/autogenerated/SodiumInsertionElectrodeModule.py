
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .InsertionElectrodeModule import InsertionElectrode







class SodiumInsertionElectrode(InsertionElectrode):
    """
    Class representing the `SodiumInsertionElectrode` entity, which inherits from:
    - InsertionElectrode

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_d936c767_1530_419c_93f4_59e08f0d702c'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SodiumInsertionElectrode'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SodiumInsertionElectrode(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_d936c767_1530_419c_93f4_59e08f0d702c',
    
    class_name='SodiumInsertionElectrode',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_d936c767_1530_419c_93f4_59e08f0d702c',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SodiumInsertionElectrode',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    