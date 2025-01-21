
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MicroscopyModule import Microscopy







class EnvironmentalScanningElectronMicroscopy(Microscopy):
    """
    Class representing the `EnvironmentalScanningElectronMicroscopy` entity, which inherits from:
    - Microscopy

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/characterisation-methodology/chameo#EnvironmentalScanningElectronMicroscopy'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'EnvironmentalScanningElectronMicroscopy'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = EnvironmentalScanningElectronMicroscopy(
    
    class_iri='https://w3id.org/emmo/domain/characterisation-methodology/chameo#EnvironmentalScanningElectronMicroscopy',
    
    class_name='EnvironmentalScanningElectronMicroscopy',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/characterisation-methodology/chameo#EnvironmentalScanningElectronMicroscopy',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'EnvironmentalScanningElectronMicroscopy',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    