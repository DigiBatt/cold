
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .GluonModule import Gluon







class GluonType4(Gluon):
    """
    Class representing the `GluonType4` entity, which inherits from:
    - Gluon

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_4eb4cb62_10e3_41ef_9226_a53462d52357'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'GluonType4'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = GluonType4(
    
    class_iri='https://w3id.org/emmo#EMMO_4eb4cb62_10e3_41ef_9226_a53462d52357',
    
    class_name='GluonType4',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_4eb4cb62_10e3_41ef_9226_a53462d52357',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'GluonType4',
        alias="class_name"
    )
    

    
    

    

    