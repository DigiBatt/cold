
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ISO80000CategorisedModule import ISO80000Categorised







class CondensedMatterPhysicsQuantity(ISO80000Categorised):
    """
    Class representing the `CondensedMatterPhysicsQuantity` entity, which inherits from:
    - ISO80000Categorised

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_c29603f5_95e8_42f5_ab0c_f3bcf3166d53'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CondensedMatterPhysicsQuantity'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = CondensedMatterPhysicsQuantity(
    
    class_iri='https://w3id.org/emmo#EMMO_c29603f5_95e8_42f5_ab0c_f3bcf3166d53',
    
    class_name='CondensedMatterPhysicsQuantity',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_c29603f5_95e8_42f5_ab0c_f3bcf3166d53',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CondensedMatterPhysicsQuantity',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    