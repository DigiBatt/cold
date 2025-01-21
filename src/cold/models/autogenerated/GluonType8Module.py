
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .GluonModule import Gluon







class GluonType8(Gluon):
    """
    Class representing the `GluonType8` entity, which inherits from:
    - Gluon

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_299f6949_6bf2_4ee6_9ec7_fd742881fb27'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'GluonType8'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = GluonType8(
    
    class_iri='https://w3id.org/emmo#EMMO_299f6949_6bf2_4ee6_9ec7_fd742881fb27',
    
    class_name='GluonType8',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_299f6949_6bf2_4ee6_9ec7_fd742881fb27',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'GluonType8',
        alias="class_name"
    )
    

    
    

    

    