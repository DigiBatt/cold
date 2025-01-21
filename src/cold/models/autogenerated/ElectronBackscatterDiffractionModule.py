
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ScanningElectronMicroscopyModule import ScanningElectronMicroscopy



from .ScatteringAndDiffractionModule import ScatteringAndDiffraction







class ElectronBackscatterDiffraction(ScanningElectronMicroscopy, ScatteringAndDiffraction):
    """
    Class representing the `ElectronBackscatterDiffraction` entity, which inherits from:
    - ScanningElectronMicroscopy, ScatteringAndDiffraction

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/characterisation-methodology/chameo#ElectronBackscatterDiffraction'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ElectronBackscatterDiffraction'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ElectronBackscatterDiffraction(
    
    class_iri='https://w3id.org/emmo/domain/characterisation-methodology/chameo#ElectronBackscatterDiffraction',
    
    class_name='ElectronBackscatterDiffraction',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/characterisation-methodology/chameo#ElectronBackscatterDiffraction',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ElectronBackscatterDiffraction',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    