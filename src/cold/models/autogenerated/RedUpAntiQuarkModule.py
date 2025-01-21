
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .UpAntiQuarkModule import UpAntiQuark



from .RedAntiQuarkModule import RedAntiQuark







class RedUpAntiQuark(UpAntiQuark, RedAntiQuark):
    """
    Class representing the `RedUpAntiQuark` entity, which inherits from:
    - UpAntiQuark, RedAntiQuark

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_da9e740a_6056_4fa5_a663_c6622e1972d8'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'RedUpAntiQuark'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = RedUpAntiQuark(
    
    class_iri='https://w3id.org/emmo#EMMO_da9e740a_6056_4fa5_a663_c6622e1972d8',
    
    class_name='RedUpAntiQuark',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_da9e740a_6056_4fa5_a663_c6622e1972d8',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'RedUpAntiQuark',
        alias="class_name"
    )
    

    
    

    

    