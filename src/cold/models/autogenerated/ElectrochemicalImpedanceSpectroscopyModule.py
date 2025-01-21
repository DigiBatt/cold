
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ImpedimetryModule import Impedimetry







class ElectrochemicalImpedanceSpectroscopy(Impedimetry):
    """
    Class representing the `ElectrochemicalImpedanceSpectroscopy` entity, which inherits from:
    - Impedimetry

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/characterisation-methodology/chameo#ElectrochemicalImpedanceSpectroscopy'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ElectrochemicalImpedanceSpectroscopy'`
        - **Alias**: `class_name`
    
    - `iupacReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `iupacReference`
    
    - `wikidataReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikidataReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ElectrochemicalImpedanceSpectroscopy(
    
    class_iri='https://w3id.org/emmo/domain/characterisation-methodology/chameo#ElectrochemicalImpedanceSpectroscopy',
    
    class_name='ElectrochemicalImpedanceSpectroscopy',
    
    iupacReference="example_value",
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/characterisation-methodology/chameo#ElectrochemicalImpedanceSpectroscopy',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ElectrochemicalImpedanceSpectroscopy',
        alias="class_name"
    )
    
    iupacReference: Optional[str] = Field(
        None,
        alias="iupacReference"
    )
    
    wikidataReference: Optional[str] = Field(
        None,
        alias="wikidataReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    