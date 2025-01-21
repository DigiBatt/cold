
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .DataProcessingModule import DataProcessing







class DataPostProcessing(DataProcessing):
    """
    Class representing the `DataPostProcessing` entity, which inherits from:
    - DataProcessing

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/characterisation-methodology/chameo#DataPostProcessing'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'DataPostProcessing'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = DataPostProcessing(
    
    class_iri='https://w3id.org/emmo/domain/characterisation-methodology/chameo#DataPostProcessing',
    
    class_name='DataPostProcessing',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/characterisation-methodology/chameo#DataPostProcessing',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'DataPostProcessing',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    