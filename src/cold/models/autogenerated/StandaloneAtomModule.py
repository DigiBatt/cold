
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .AtomModule import Atom







class StandaloneAtom(Atom):
    """
    Class representing the `StandaloneAtom` entity, which inherits from:
    - Atom

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_2fd3f574_5e93_47fe_afca_ed80b0a21ab4'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'StandaloneAtom'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = StandaloneAtom(
    
    class_iri='https://w3id.org/emmo#EMMO_2fd3f574_5e93_47fe_afca_ed80b0a21ab4',
    
    class_name='StandaloneAtom',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_2fd3f574_5e93_47fe_afca_ed80b0a21ab4',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'StandaloneAtom',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    