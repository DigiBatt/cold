
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .PorosimetryModule import Porosimetry







class MercuryPorosimetry(Porosimetry):
    """
    Class representing the `MercuryPorosimetry` entity, which inherits from:
    - Porosimetry

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/characterisation-methodology/chameo#MercuryPorosimetry'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MercuryPorosimetry'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = MercuryPorosimetry(
    
    class_iri='https://w3id.org/emmo/domain/characterisation-methodology/chameo#MercuryPorosimetry',
    
    class_name='MercuryPorosimetry',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/characterisation-methodology/chameo#MercuryPorosimetry',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MercuryPorosimetry',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    