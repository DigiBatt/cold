
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MicroscopyModule import Microscopy







class FieldEmissionScanningElectronMicroscopy(Microscopy):
    """
    Class representing the `FieldEmissionScanningElectronMicroscopy` entity, which inherits from:
    - Microscopy

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/characterisation-methodology/chameo#FieldEmissionScanningElectronMicroscopy'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'FieldEmissionScanningElectronMicroscopy'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = FieldEmissionScanningElectronMicroscopy(
    
    class_iri='https://w3id.org/emmo/domain/characterisation-methodology/chameo#FieldEmissionScanningElectronMicroscopy',
    
    class_name='FieldEmissionScanningElectronMicroscopy',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/characterisation-methodology/chameo#FieldEmissionScanningElectronMicroscopy',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'FieldEmissionScanningElectronMicroscopy',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    