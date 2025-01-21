
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .GasSolidSuspensionModule import GasSolidSuspension







class Dust(GasSolidSuspension):
    """
    Class representing the `Dust` entity, which inherits from:
    - GasSolidSuspension

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_e4281979_2b07_4a43_a772_4903fb3696fe'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Dust'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Dust(
    
    class_iri='https://w3id.org/emmo#EMMO_e4281979_2b07_4a43_a772_4903fb3696fe',
    
    class_name='Dust',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_e4281979_2b07_4a43_a772_4903fb3696fe',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Dust',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    