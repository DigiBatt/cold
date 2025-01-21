
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .JoinManufacturingModule import JoinManufacturing







class FormingJoin(JoinManufacturing):
    """
    Class representing the `FormingJoin` entity, which inherits from:
    - JoinManufacturing

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_78284835_f4ed_4a7c_914f_a7fdb460ed8e'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'FormingJoin'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = FormingJoin(
    
    class_iri='https://w3id.org/emmo#EMMO_78284835_f4ed_4a7c_914f_a7fdb460ed8e',
    
    class_name='FormingJoin',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_78284835_f4ed_4a7c_914f_a7fdb460ed8e',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'FormingJoin',
        alias="class_name"
    )
    

    
    

    

    