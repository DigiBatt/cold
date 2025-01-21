
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .GluonModule import Gluon







class GluonType5(Gluon):
    """
    Class representing the `GluonType5` entity, which inherits from:
    - Gluon

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_8a83b7bd_85bd_48e4_a4ac_bb2eb97d3014'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'GluonType5'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = GluonType5(
    
    class_iri='https://w3id.org/emmo#EMMO_8a83b7bd_85bd_48e4_a4ac_bb2eb97d3014',
    
    class_name='GluonType5',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_8a83b7bd_85bd_48e4_a4ac_bb2eb97d3014',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'GluonType5',
        alias="class_name"
    )
    

    
    

    

    