
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SpectrometryModule import Spectrometry







class GammaSpectrometry(Spectrometry):
    """
    Class representing the `GammaSpectrometry` entity, which inherits from:
    - Spectrometry

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/characterisation-methodology/chameo#GammaSpectrometry'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'GammaSpectrometry'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = GammaSpectrometry(
    
    class_iri='https://w3id.org/emmo/domain/characterisation-methodology/chameo#GammaSpectrometry',
    
    class_name='GammaSpectrometry',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/characterisation-methodology/chameo#GammaSpectrometry',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'GammaSpectrometry',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    