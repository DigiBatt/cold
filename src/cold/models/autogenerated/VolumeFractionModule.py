
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .IntensiveModule import Intensive



from .ChemicalCompositionQuantityModule import ChemicalCompositionQuantity



from .RatioQuantityModule import RatioQuantity







class VolumeFraction(Intensive, ChemicalCompositionQuantity, RatioQuantity):
    """
    Class representing the `VolumeFraction` entity, which inherits from:
    - Intensive, ChemicalCompositionQuantity, RatioQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_a8eb87b5_4d10_4137_a75c_e04ee59ca095'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'VolumeFraction'`
        - **Alias**: `class_name`
    
    - `iupacReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `iupacReference`
    
    - `qudtReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `qudtReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `ISO80000Reference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `ISO80000Reference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = VolumeFraction(
    
    class_iri='https://w3id.org/emmo#EMMO_a8eb87b5_4d10_4137_a75c_e04ee59ca095',
    
    class_name='VolumeFraction',
    
    iupacReference="example_value",
    
    qudtReference="example_value",
    
    elucidation="example_value",
    
    ISO80000Reference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_a8eb87b5_4d10_4137_a75c_e04ee59ca095',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'VolumeFraction',
        alias="class_name"
    )
    
    iupacReference: Optional[str] = Field(
        None,
        alias="iupacReference"
    )
    
    qudtReference: Optional[str] = Field(
        None,
        alias="qudtReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    ISO80000Reference: Optional[str] = Field(
        None,
        alias="ISO80000Reference"
    )
    

    
    

    

    