
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SpaceAndTimeQuantityModule import SpaceAndTimeQuantity



from .ReciprocalLengthModule import ReciprocalLength







class Attenuation(SpaceAndTimeQuantity, ReciprocalLength):
    """
    Class representing the `Attenuation` entity, which inherits from:
    - SpaceAndTimeQuantity, ReciprocalLength

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_ecf938f1_bc37_4897_841d_092cd37f74de'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Attenuation'`
        - **Alias**: `class_name`
    
    - `iupacReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `iupacReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `ISO80000Reference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `ISO80000Reference`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Attenuation(
    
    class_iri='https://w3id.org/emmo#EMMO_ecf938f1_bc37_4897_841d_092cd37f74de',
    
    class_name='Attenuation',
    
    iupacReference="example_value",
    
    elucidation="example_value",
    
    ISO80000Reference="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_ecf938f1_bc37_4897_841d_092cd37f74de',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Attenuation',
        alias="class_name"
    )
    
    iupacReference: Optional[str] = Field(
        None,
        alias="iupacReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    ISO80000Reference: Optional[str] = Field(
        None,
        alias="ISO80000Reference"
    )
    
    wikipediaReference: Optional[str] = Field(
        None,
        alias="wikipediaReference"
    )
    

    
    

    

    