
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .GluonModule import Gluon







class GluonType6(Gluon):
    """
    Class representing the `GluonType6` entity, which inherits from:
    - Gluon

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_e2000aeb_e3ab_41b7_a790_7c8bd02d0b6e'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'GluonType6'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = GluonType6(
    
    class_iri='https://w3id.org/emmo#EMMO_e2000aeb_e3ab_41b7_a790_7c8bd02d0b6e',
    
    class_name='GluonType6',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_e2000aeb_e3ab_41b7_a790_7c8bd02d0b6e',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'GluonType6',
        alias="class_name"
    )
    

    
    

    

    