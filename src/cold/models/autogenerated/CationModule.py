
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .IonModule import Ion







class Cation(Ion):
    """
    Class representing the `Cation` entity, which inherits from:
    - Ion

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_dae2320d_be18_44ba_90bd_8176decc4b47'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Cation'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Cation(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_dae2320d_be18_44ba_90bd_8176decc4b47',
    
    class_name='Cation',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_dae2320d_be18_44ba_90bd_8176decc4b47',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Cation',
        alias="class_name"
    )
    

    
    

    

    