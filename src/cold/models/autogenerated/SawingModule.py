
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MachiningModule import Machining







class Sawing(Machining):
    """
    Class representing the `Sawing` entity, which inherits from:
    - Machining

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_c7d004db_59fa_5ae3_adb1_e75736aa721a'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Sawing'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Sawing(
    
    class_iri='https://w3id.org/emmo#EMMO_c7d004db_59fa_5ae3_adb1_e75736aa721a',
    
    class_name='Sawing',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_c7d004db_59fa_5ae3_adb1_e75736aa721a',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Sawing',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    