
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .GluonModule import Gluon







class GluonType1(Gluon):
    """
    Class representing the `GluonType1` entity, which inherits from:
    - Gluon

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_311ba558_6444_4de1_9c68_5009b9dfb80c'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'GluonType1'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = GluonType1(
    
    class_iri='https://w3id.org/emmo#EMMO_311ba558_6444_4de1_9c68_5009b9dfb80c',
    
    class_name='GluonType1',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_311ba558_6444_4de1_9c68_5009b9dfb80c',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'GluonType1',
        alias="class_name"
    )
    

    
    

    

    