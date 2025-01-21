
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .HardeningByFormingModule import HardeningByForming







class HardeningByDrawing(HardeningByForming):
    """
    Class representing the `HardeningByDrawing` entity, which inherits from:
    - HardeningByForming

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_c4ffca76_fb0c_43c7_bc16_8c2430888c83'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'HardeningByDrawing'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = HardeningByDrawing(
    
    class_iri='https://w3id.org/emmo#EMMO_c4ffca76_fb0c_43c7_bc16_8c2430888c83',
    
    class_name='HardeningByDrawing',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_c4ffca76_fb0c_43c7_bc16_8c2430888c83',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'HardeningByDrawing',
        alias="class_name"
    )
    

    
    

    

    