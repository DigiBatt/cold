
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .NetworkModule import Network







class SupplyChain(Network):
    """
    Class representing the `SupplyChain` entity, which inherits from:
    - Network

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_0c7ad550_00ae_45ff_a4e2_58d6a61f48eb'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SupplyChain'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SupplyChain(
    
    class_iri='https://w3id.org/emmo#EMMO_0c7ad550_00ae_45ff_a4e2_58d6a61f48eb',
    
    class_name='SupplyChain',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_0c7ad550_00ae_45ff_a4e2_58d6a61f48eb',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SupplyChain',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    