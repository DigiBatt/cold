
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .DataSetModule import DataSet







class Record(DataSet):
    """
    Class representing the `Record` entity, which inherits from:
    - DataSet

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_59c041fc_eaa1_40fc_9b3e_1a6aca6119fd'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Record'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Record(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_59c041fc_eaa1_40fc_9b3e_1a6aca6119fd',
    
    class_name='Record',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_59c041fc_eaa1_40fc_9b3e_1a6aca6119fd',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Record',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    