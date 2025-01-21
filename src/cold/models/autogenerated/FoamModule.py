
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ColloidModule import Colloid







class Foam(Colloid):
    """
    Class representing the `Foam` entity, which inherits from:
    - Colloid

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_1f5e3e7e_72c9_40d4_91dd_ae432d7b7018'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Foam'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Foam(
    
    class_iri='https://w3id.org/emmo#EMMO_1f5e3e7e_72c9_40d4_91dd_ae432d7b7018',
    
    class_name='Foam',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_1f5e3e7e_72c9_40d4_91dd_ae432d7b7018',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Foam',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    