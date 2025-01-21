
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .StandaloneAtomModule import StandaloneAtom







class IonAtom(StandaloneAtom):
    """
    Class representing the `IonAtom` entity, which inherits from:
    - StandaloneAtom

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_db03061b_db31_4132_a47a_6a634846578b'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'IonAtom'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = IonAtom(
    
    class_iri='https://w3id.org/emmo#EMMO_db03061b_db31_4132_a47a_6a634846578b',
    
    class_name='IonAtom',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_db03061b_db31_4132_a47a_6a634846578b',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'IonAtom',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    