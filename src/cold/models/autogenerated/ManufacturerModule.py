
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .WholeModule import Whole



from .StrictFundamentalModule import StrictFundamental



from .ObjectModule import Object







class Manufacturer(Whole, StrictFundamental, Object):
    """
    Class representing the `Manufacturer` entity, which inherits from:
    - Whole, StrictFundamental, Object

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_c0afb341_7d31_4883_a307_ae4606df2a1b'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Manufacturer'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Manufacturer(
    
    class_iri='https://w3id.org/emmo#EMMO_c0afb341_7d31_4883_a307_ae4606df2a1b',
    
    class_name='Manufacturer',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_c0afb341_7d31_4883_a307_ae4606df2a1b',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Manufacturer',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    