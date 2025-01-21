
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SampleModule import Sample







class PreparedSample(Sample):
    """
    Class representing the `PreparedSample` entity, which inherits from:
    - Sample

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/characterisation-methodology/chameo#PreparedSample'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'PreparedSample'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = PreparedSample(
    
    class_iri='https://w3id.org/emmo/domain/characterisation-methodology/chameo#PreparedSample',
    
    class_name='PreparedSample',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/characterisation-methodology/chameo#PreparedSample',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'PreparedSample',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    