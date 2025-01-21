
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SymbolicModule import Symbolic







class Language(Symbolic):
    """
    Class representing the `Language` entity, which inherits from:
    - Symbolic

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_d8d2144e_5c8d_455d_a643_5caf4d8d9df8'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Language'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Language(
    
    class_iri='https://w3id.org/emmo#EMMO_d8d2144e_5c8d_455d_a643_5caf4d8d9df8',
    
    class_name='Language',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_d8d2144e_5c8d_455d_a643_5caf4d8d9df8',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Language',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    