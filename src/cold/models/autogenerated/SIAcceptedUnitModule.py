
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SpecialUnitModule import SpecialUnit



from .SIAcceptedModule import SIAccepted







class SIAcceptedUnit(SpecialUnit, SIAccepted):
    """
    Class representing the `SIAcceptedUnit` entity, which inherits from:
    - SpecialUnit, SIAccepted

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_6795a4b8_ffd0_4588_a581_a9413fe49cac'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SIAcceptedUnit'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SIAcceptedUnit(
    
    class_iri='https://w3id.org/emmo#EMMO_6795a4b8_ffd0_4588_a581_a9413fe49cac',
    
    class_name='SIAcceptedUnit',
    
    elucidation="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_6795a4b8_ffd0_4588_a581_a9413fe49cac',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SIAcceptedUnit',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    wikipediaReference: Optional[str] = Field(
        None,
        alias="wikipediaReference"
    )
    

    
    

    

    