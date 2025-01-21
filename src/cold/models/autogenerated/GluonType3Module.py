
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .GluonModule import Gluon







class GluonType3(Gluon):
    """
    Class representing the `GluonType3` entity, which inherits from:
    - Gluon

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_ebb26c39_dbbc_4363_b784_88d9110e4d5b'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'GluonType3'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = GluonType3(
    
    class_iri='https://w3id.org/emmo#EMMO_ebb26c39_dbbc_4363_b784_88d9110e4d5b',
    
    class_name='GluonType3',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_ebb26c39_dbbc_4363_b784_88d9110e4d5b',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'GluonType3',
        alias="class_name"
    )
    

    
    

    

    