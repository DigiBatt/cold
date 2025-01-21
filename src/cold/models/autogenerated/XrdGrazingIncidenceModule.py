
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ScatteringAndDiffractionModule import ScatteringAndDiffraction







class XrdGrazingIncidence(ScatteringAndDiffraction):
    """
    Class representing the `XrdGrazingIncidence` entity, which inherits from:
    - ScatteringAndDiffraction

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/characterisation-methodology/chameo#XrdGrazingIncidence'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'XrdGrazingIncidence'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = XrdGrazingIncidence(
    
    class_iri='https://w3id.org/emmo/domain/characterisation-methodology/chameo#XrdGrazingIncidence',
    
    class_name='XrdGrazingIncidence',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/characterisation-methodology/chameo#XrdGrazingIncidence',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'XrdGrazingIncidence',
        alias="class_name"
    )
    

    
    

    

    