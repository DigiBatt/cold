
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ManufacturedProductModule import ManufacturedProduct







class Device(ManufacturedProduct):
    """
    Class representing the `Device` entity, which inherits from:
    - ManufacturedProduct

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_494b372c_cfdf_47d3_a4de_5e037c540de8'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Device'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Device(
    
    class_iri='https://w3id.org/emmo#EMMO_494b372c_cfdf_47d3_a4de_5e037c540de8',
    
    class_name='Device',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_494b372c_cfdf_47d3_a4de_5e037c540de8',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Device',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    