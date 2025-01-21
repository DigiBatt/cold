
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .InsertionElectrodeModule import InsertionElectrode







class ZincInsertionElectrode(InsertionElectrode):
    """
    Class representing the `ZincInsertionElectrode` entity, which inherits from:
    - InsertionElectrode

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_245c9442_ca1d_4070_a624_182b92d30b10'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ZincInsertionElectrode'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ZincInsertionElectrode(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_245c9442_ca1d_4070_a624_182b92d30b10',
    
    class_name='ZincInsertionElectrode',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_245c9442_ca1d_4070_a624_182b92d30b10',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ZincInsertionElectrode',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    