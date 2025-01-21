
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SpectroscopyModule import Spectroscopy







class FourierTransformInfraredSpectroscopy(Spectroscopy):
    """
    Class representing the `FourierTransformInfraredSpectroscopy` entity, which inherits from:
    - Spectroscopy

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/characterisation-methodology/chameo#FourierTransformInfraredSpectroscopy'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'FourierTransformInfraredSpectroscopy'`
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
    obj = FourierTransformInfraredSpectroscopy(
    
    class_iri='https://w3id.org/emmo/domain/characterisation-methodology/chameo#FourierTransformInfraredSpectroscopy',
    
    class_name='FourierTransformInfraredSpectroscopy',
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/characterisation-methodology/chameo#FourierTransformInfraredSpectroscopy',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'FourierTransformInfraredSpectroscopy',
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
    

    
    

    

    