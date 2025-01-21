
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .PureNumberQuantityModule import PureNumberQuantity







class MassNumber(PureNumberQuantity):
    """
    Class representing the `MassNumber` entity, which inherits from:
    - PureNumberQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_dc6c8de0_cfc4_4c66_a7dc_8f720e732d54'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MassNumber'`
        - **Alias**: `class_name`
    
    - `definition` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `definition`
    
    - `qudtReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `qudtReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = MassNumber(
    
    class_iri='https://w3id.org/emmo#EMMO_dc6c8de0_cfc4_4c66_a7dc_8f720e732d54',
    
    class_name='MassNumber',
    
    definition="example_value",
    
    qudtReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_dc6c8de0_cfc4_4c66_a7dc_8f720e732d54',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MassNumber',
        alias="class_name"
    )
    
    definition: Optional[str] = Field(
        None,
        alias="definition"
    )
    
    qudtReference: Optional[str] = Field(
        None,
        alias="qudtReference"
    )
    

    
    

    

    