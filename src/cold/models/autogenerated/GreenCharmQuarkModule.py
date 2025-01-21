
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CharmQuarkModule import CharmQuark



from .GreenQuarkModule import GreenQuark







class GreenCharmQuark(CharmQuark, GreenQuark):
    """
    Class representing the `GreenCharmQuark` entity, which inherits from:
    - CharmQuark, GreenQuark

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_891d1351_3843_4da3_906b_3b30411bd512'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'GreenCharmQuark'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = GreenCharmQuark(
    
    class_iri='https://w3id.org/emmo#EMMO_891d1351_3843_4da3_906b_3b30411bd512',
    
    class_name='GreenCharmQuark',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_891d1351_3843_4da3_906b_3b30411bd512',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'GreenCharmQuark',
        alias="class_name"
    )
    

    
    

    

    