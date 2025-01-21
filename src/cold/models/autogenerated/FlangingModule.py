
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .FormingJoinModule import FormingJoin







class Flanging(FormingJoin):
    """
    Class representing the `Flanging` entity, which inherits from:
    - FormingJoin

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_3086e6a8_edd9_4592_b33c_66d818835951'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Flanging'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Flanging(
    
    class_iri='https://w3id.org/emmo#EMMO_3086e6a8_edd9_4592_b33c_66d818835951',
    
    class_name='Flanging',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_3086e6a8_edd9_4592_b33c_66d818835951',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Flanging',
        alias="class_name"
    )
    

    
    

    

    