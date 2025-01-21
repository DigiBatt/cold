
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .DataPreparationModule import DataPreparation







class DataFiltering(DataPreparation):
    """
    Class representing the `DataFiltering` entity, which inherits from:
    - DataPreparation

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/characterisation-methodology/chameo#DataFiltering'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'DataFiltering'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = DataFiltering(
    
    class_iri='https://w3id.org/emmo/domain/characterisation-methodology/chameo#DataFiltering',
    
    class_name='DataFiltering',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/characterisation-methodology/chameo#DataFiltering',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'DataFiltering',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    