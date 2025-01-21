
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MoleculeModule import Molecule







class Heteronuclear(Molecule):
    """
    Class representing the `Heteronuclear` entity, which inherits from:
    - Molecule

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_50967f46_51f9_462a_b1e4_e63365b4a184'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Heteronuclear'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `example` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `example`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Heteronuclear(
    
    class_iri='https://w3id.org/emmo#EMMO_50967f46_51f9_462a_b1e4_e63365b4a184',
    
    class_name='Heteronuclear',
    
    elucidation="example_value",
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_50967f46_51f9_462a_b1e4_e63365b4a184',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Heteronuclear',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    example: Optional[str] = Field(
        None,
        alias="example"
    )
    

    
    

    

    