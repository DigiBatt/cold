
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .GaugeBosonModule import GaugeBoson







class Photon(GaugeBoson):
    """
    Class representing the `Photon` entity, which inherits from:
    - GaugeBoson

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_25f8b804_9a0b_4387_a3e7_b35bce5365ee'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Photon'`
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
    obj = Photon(
    
    class_iri='https://w3id.org/emmo#EMMO_25f8b804_9a0b_4387_a3e7_b35bce5365ee',
    
    class_name='Photon',
    
    elucidation="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_25f8b804_9a0b_4387_a3e7_b35bce5365ee',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Photon',
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
    

    
    

    

    