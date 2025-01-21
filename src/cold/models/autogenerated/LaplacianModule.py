
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .DifferentialOperatorModule import DifferentialOperator







class Laplacian(DifferentialOperator):
    """
    Class representing the `Laplacian` entity, which inherits from:
    - DifferentialOperator

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_048a14e3_65fb_457d_8695_948965c89492'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Laplacian'`
        - **Alias**: `class_name`
    
    - `hasSymbolValue` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSymbolValue`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Laplacian(
    
    class_iri='https://w3id.org/emmo#EMMO_048a14e3_65fb_457d_8695_948965c89492',
    
    class_name='Laplacian',
    
    hasSymbolValue="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_048a14e3_65fb_457d_8695_948965c89492',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Laplacian',
        alias="class_name"
    )
    
    hasSymbolValue: Optional[str] = Field(
        None,
        alias="hasSymbolValue"
    )
    

    
    

    

    