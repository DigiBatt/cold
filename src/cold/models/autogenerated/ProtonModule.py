
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .NucleonModule import Nucleon







class Proton(Nucleon):
    """
    Class representing the `Proton` entity, which inherits from:
    - Nucleon

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_8f87e700_99a8_4427_8ffb_e493de05c217'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Proton'`
        - **Alias**: `class_name`
    
    - `hasSpatialSlice` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSpatialSlice`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Proton(
    
    class_iri='https://w3id.org/emmo#EMMO_8f87e700_99a8_4427_8ffb_e493de05c217',
    
    class_name='Proton',
    
    hasSpatialSlice="example_value",
    
    elucidation="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_8f87e700_99a8_4427_8ffb_e493de05c217',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Proton',
        alias="class_name"
    )
    
    hasSpatialSlice: Optional[str] = Field(
        None,
        alias="hasSpatialSlice"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    wikipediaReference: Optional[str] = Field(
        None,
        alias="wikipediaReference"
    )
    

    
    

    

    