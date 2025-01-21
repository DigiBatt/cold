
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SampleModule import Sample







class IntermediateSample(Sample):
    """
    Class representing the `IntermediateSample` entity, which inherits from:
    - Sample

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/characterisation-methodology/chameo#IntermediateSample'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'IntermediateSample'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = IntermediateSample(
    
    class_iri='https://w3id.org/emmo/domain/characterisation-methodology/chameo#IntermediateSample',
    
    class_name='IntermediateSample',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/characterisation-methodology/chameo#IntermediateSample',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'IntermediateSample',
        alias="class_name"
    )
    

    
    

    

    