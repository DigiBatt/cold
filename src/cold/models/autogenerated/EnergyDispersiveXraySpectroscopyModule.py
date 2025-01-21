
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SpectroscopyModule import Spectroscopy







class EnergyDispersiveXraySpectroscopy(Spectroscopy):
    """
    Class representing the `EnergyDispersiveXraySpectroscopy` entity, which inherits from:
    - Spectroscopy

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/characterisation-methodology/chameo#EnergyDispersiveXraySpectroscopy'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'EnergyDispersiveXraySpectroscopy'`
        - **Alias**: `class_name`
    
    - `wikidataReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikidataReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = EnergyDispersiveXraySpectroscopy(
    
    class_iri='https://w3id.org/emmo/domain/characterisation-methodology/chameo#EnergyDispersiveXraySpectroscopy',
    
    class_name='EnergyDispersiveXraySpectroscopy',
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/characterisation-methodology/chameo#EnergyDispersiveXraySpectroscopy',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'EnergyDispersiveXraySpectroscopy',
        alias="class_name"
    )
    
    wikidataReference: Optional[str] = Field(
        None,
        alias="wikidataReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    wikipediaReference: Optional[str] = Field(
        None,
        alias="wikipediaReference"
    )
    

    
    

    

    