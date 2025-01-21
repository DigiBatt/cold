
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .AtomModule import Atom







class BondedAtom(Atom):
    """
    Class representing the `BondedAtom` entity, which inherits from:
    - Atom

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_8303a247_f9d9_4616_bdcd_f5cbd7b298e3'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'BondedAtom'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = BondedAtom(
    
    class_iri='https://w3id.org/emmo#EMMO_8303a247_f9d9_4616_bdcd_f5cbd7b298e3',
    
    class_name='BondedAtom',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_8303a247_f9d9_4616_bdcd_f5cbd7b298e3',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'BondedAtom',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    