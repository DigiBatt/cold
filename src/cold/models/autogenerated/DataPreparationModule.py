
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .DataProcessingModule import DataProcessing







class DataPreparation(DataProcessing):
    """
    Class representing the `DataPreparation` entity, which inherits from:
    - DataProcessing

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/characterisation-methodology/chameo#DataPreparation'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'DataPreparation'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = DataPreparation(
    
    class_iri='https://w3id.org/emmo/domain/characterisation-methodology/chameo#DataPreparation',
    
    class_name='DataPreparation',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/characterisation-methodology/chameo#DataPreparation',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'DataPreparation',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    