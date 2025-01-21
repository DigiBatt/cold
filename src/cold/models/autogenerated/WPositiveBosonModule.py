
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .WBosonModule import WBoson







class WPositiveBoson(WBoson):
    """
    Class representing the `WPositiveBoson` entity, which inherits from:
    - WBoson

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_e5728eea_e805_433e_a426_56c4fe811e67'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'WPositiveBoson'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = WPositiveBoson(
    
    class_iri='https://w3id.org/emmo#EMMO_e5728eea_e805_433e_a426_56c4fe811e67',
    
    class_name='WPositiveBoson',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_e5728eea_e805_433e_a426_56c4fe811e67',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'WPositiveBoson',
        alias="class_name"
    )
    

    
    

    

    