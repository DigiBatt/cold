
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .QuarkModule import Quark







class UpQuarkType(Quark):
    """
    Class representing the `UpQuarkType` entity, which inherits from:
    - Quark

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_fc47b76f_ad01_4cd0_8fc6_55532000e7c8'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'UpQuarkType'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = UpQuarkType(
    
    class_iri='https://w3id.org/emmo#EMMO_fc47b76f_ad01_4cd0_8fc6_55532000e7c8',
    
    class_name='UpQuarkType',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_fc47b76f_ad01_4cd0_8fc6_55532000e7c8',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'UpQuarkType',
        alias="class_name"
    )
    

    
    

    

    