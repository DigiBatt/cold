
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .OneManifoldModule import OneManifold







class Line(OneManifold):
    """
    Class representing the `Line` entity, which inherits from:
    - OneManifold

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_3e309118_e8b7_4021_80f4_642d2df65d94'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Line'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Line(
    
    class_iri='https://w3id.org/emmo#EMMO_3e309118_e8b7_4021_80f4_642d2df65d94',
    
    class_name='Line',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_3e309118_e8b7_4021_80f4_642d2df65d94',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Line',
        alias="class_name"
    )
    

    
    

    

    