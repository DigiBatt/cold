
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ChronopotentiometryModule import Chronopotentiometry







class GalvanostaticIntermittentTitrationTechnique(Chronopotentiometry):
    """
    Class representing the `GalvanostaticIntermittentTitrationTechnique` entity, which inherits from:
    - Chronopotentiometry

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/characterisation-methodology/chameo#GalvanostaticIntermittentTitrationTechnique'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'GalvanostaticIntermittentTitrationTechnique'`
        - **Alias**: `class_name`
    
    - `wikidataReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikidataReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = GalvanostaticIntermittentTitrationTechnique(
    
    class_iri='https://w3id.org/emmo/domain/characterisation-methodology/chameo#GalvanostaticIntermittentTitrationTechnique',
    
    class_name='GalvanostaticIntermittentTitrationTechnique',
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/characterisation-methodology/chameo#GalvanostaticIntermittentTitrationTechnique',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'GalvanostaticIntermittentTitrationTechnique',
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
    

    
    

    

    