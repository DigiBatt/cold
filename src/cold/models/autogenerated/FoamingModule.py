
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .FormingFromLiquidModule import FormingFromLiquid







class Foaming(FormingFromLiquid):
    """
    Class representing the `Foaming` entity, which inherits from:
    - FormingFromLiquid

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_865a1a70_02e8_40b2_948d_078e636c8701'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Foaming'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Foaming(
    
    class_iri='https://w3id.org/emmo#EMMO_865a1a70_02e8_40b2_948d_078e636c8701',
    
    class_name='Foaming',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_865a1a70_02e8_40b2_948d_078e636c8701',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Foaming',
        alias="class_name"
    )
    

    
    

    

    