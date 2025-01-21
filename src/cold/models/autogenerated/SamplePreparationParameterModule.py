
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ParameterModule import Parameter







class SamplePreparationParameter(Parameter):
    """
    Class representing the `SamplePreparationParameter` entity, which inherits from:
    - Parameter

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/characterisation-methodology/chameo#SamplePreparationParameter'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SamplePreparationParameter'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SamplePreparationParameter(
    
    class_iri='https://w3id.org/emmo/domain/characterisation-methodology/chameo#SamplePreparationParameter',
    
    class_name='SamplePreparationParameter',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/characterisation-methodology/chameo#SamplePreparationParameter',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SamplePreparationParameter',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    