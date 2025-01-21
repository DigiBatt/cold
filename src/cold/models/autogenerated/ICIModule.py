
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ChronopotentiometryModule import Chronopotentiometry







class ICI(Chronopotentiometry):
    """
    Class representing the `ICI` entity, which inherits from:
    - Chronopotentiometry

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/characterisation-methodology/chameo#ICI'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ICI'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ICI(
    
    class_iri='https://w3id.org/emmo/domain/characterisation-methodology/chameo#ICI',
    
    class_name='ICI',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/characterisation-methodology/chameo#ICI',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ICI',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    