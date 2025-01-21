
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ChromatographyModule import Chromatography







class CriticalAndSupercriticalChromatography(Chromatography):
    """
    Class representing the `CriticalAndSupercriticalChromatography` entity, which inherits from:
    - Chromatography

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/characterisation-methodology/chameo#CriticalAndSupercriticalChromatography'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CriticalAndSupercriticalChromatography'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = CriticalAndSupercriticalChromatography(
    
    class_iri='https://w3id.org/emmo/domain/characterisation-methodology/chameo#CriticalAndSupercriticalChromatography',
    
    class_name='CriticalAndSupercriticalChromatography',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/characterisation-methodology/chameo#CriticalAndSupercriticalChromatography',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CriticalAndSupercriticalChromatography',
        alias="class_name"
    )
    

    
    

    

    