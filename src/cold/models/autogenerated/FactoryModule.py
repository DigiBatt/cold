
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .HolisticSystemModule import HolisticSystem







class Factory(HolisticSystem):
    """
    Class representing the `Factory` entity, which inherits from:
    - HolisticSystem

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_02122e58_e0b3_4274_bdd4_745f64a61645'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Factory'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Factory(
    
    class_iri='https://w3id.org/emmo#EMMO_02122e58_e0b3_4274_bdd4_745f64a61645',
    
    class_name='Factory',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_02122e58_e0b3_4274_bdd4_745f64a61645',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Factory',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    