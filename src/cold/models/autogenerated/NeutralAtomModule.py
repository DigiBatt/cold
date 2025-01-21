
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .StandaloneAtomModule import StandaloneAtom







class NeutralAtom(StandaloneAtom):
    """
    Class representing the `NeutralAtom` entity, which inherits from:
    - StandaloneAtom

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_4588526f_8553_4f4d_aa73_a483e88d599b'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'NeutralAtom'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = NeutralAtom(
    
    class_iri='https://w3id.org/emmo#EMMO_4588526f_8553_4f4d_aa73_a483e88d599b',
    
    class_name='NeutralAtom',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_4588526f_8553_4f4d_aa73_a483e88d599b',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'NeutralAtom',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    